
"""

This script adds the the containing package as a valid debug adapter in the Debugger's settings

"""

import sublime

if sublime.version() < '4000':
	raise Exception('This version of the template adapter requires Sublime Text 4. Use the st3 version instead.')

# Import your adapter here. This allows it to be recognized by Sublime and
# lets your adapter subclass be recognized and added to the Debugger.
from .adapter.template import TemplateAdapter
