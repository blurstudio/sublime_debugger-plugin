# Debug Adapter Plugin

A template repository that provides the basics for connecting a debug adapter to Sublime's Debugger plugin.

attach.py is what lets the Debugger know this adapter exists and how to run it,
minimal modifications should be reuired. 

The code in adapter/ is where you can develop your DAP implementation.