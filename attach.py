
"""

This script adds the the containing package as a valid debug adapter in the Debugger's settings

"""

from os.path import join, abspath, dirname
import sublime


adapter_name = "Template"
adapter_type = "template"  # NOTE: type must be unique (used as key when storing adapters and to find correct config)
package_path = join(dirname(abspath(__file__)), "adapter")

debugger_entry = {  # The entry used by the Debugger to run this adapter
    "command": ["python", package_path],
    "type": adapter_type
}

default_config = {  # Default settings for this adapter to use
    "name": "Template (Do not use)",  # how the config appears in Sublime
    "request": "attach",  # can only be attach or launch
    "type": adapter_type
}  # Feel free to add any other keys. The provided ones are the minimum required


def plugin_loaded():

    # Add adapter to debugger settings for it to be recognized
    debugger_settings = sublime.load_settings('debugger.sublime-settings')
    adapters_custom = debugger_settings.get('adapters_custom', {})

    adapters_custom[adapter_type] = debugger_entry

    debugger_settings.set('adapters_custom', adapters_custom)
    sublime.save_settings('debugger.sublime-settings')

    # Add configuration to debug configurations
    data = sublime.active_window().project_data()
    if data:
        data.setdefault('settings', {}).setdefault('debug.configurations', [])
        configs = data["settings"]["debug.configurations"]

        for index, config in enumerate(configs):
            if config["name"] == default_config["name"]:
                return  # The config is already in the project settings. Just return

        configs.append(default_config)
        sublime.active_window().set_project_data(data)


def plugin_unloaded():
    """This is all done every unload just in case this adapter is being uninstalled"""

    # Remove entry from debugger settings
    debugger_settings = sublime.load_settings('debugger.sublime-settings')
    adapters_custom = debugger_settings.get('adapters_custom', {})

    adapters_custom.pop(adapter_name, "")

    debugger_settings.set('adapters_custom', adapters_custom)
    sublime.save_settings('debugger.sublime-settings')

    # Remove configuration from debug configurations
    data = sublime.active_window().project_data()
    if data:
        data.setdefault('settings', {}).setdefault('debug.configurations', [])
        configs = data["settings"]["debug.configurations"]
        index = -1

        for index, config in enumerate(configs):
            if config["name"] == default_config["name"]:
                break

        if index >= 0:
            configs.pop(index)

        sublime.active_window().set_project_data(data)
