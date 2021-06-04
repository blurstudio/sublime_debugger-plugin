
"""

This script adds the the containing package as a valid debug adapter in the Debugger's settings

"""

from Debugger.modules.debugger.adapter.adapters import Adapters
from .adapter.template import TemplateAdapter

import sublime


if sublime.version() < '4000':
	raise Exception('This version of the template adapter requires Sublime Text 4. Use the st3 version instead.')


def plugin_loaded():
    """
    This function is called when the plugin is loaded.
    We use it to inject the custom adapter into the adapters 
    list, but more initialization can be done.
    """
    Adapters.all.append(TemplateAdapter())


def plugin_unloaded():
    """
    This is called every time the plugin is uninstalled or sublime is closed.
    Use it to stop threads or remove temporary directories, etc.
    """
    pass
