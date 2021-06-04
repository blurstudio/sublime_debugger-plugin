
from Debugger.modules.typecheck import *
import Debugger.modules.debugger.adapter as adapter

import sublime


# This is the id of your adapter. It must be unique and match no 
# other existing adapters.
adapter_type = 'template'


class TemplateAdapter(adapter.AdapterConfiguration):

	@property
	def type(self): return adapter_type

	async def start(self, log, configuration):
		"""
		start() is called when the play button is pressed in the debugger.
		
		The configuration is passed in, allowing you to get necessary settings
		to use when setting up the adapter as it starts up (such as getting the 
		desired host/port to connect to, show below)

		The configuration will be chosen by the user from the 
		configuration_snippets function below, and its contents are the contents 
		of "body:". However, the user can change the configurations manually so 
		make sure to account for unexpected changes. 
		"""

		# This function must return one of two types of Transports. 
		# 
		# The first is an StdioTransport, which communicates with the adapter 
		# via DAP through standard input/output. A command must be given so 
		# that the transport can spawn the process and communicate with it. 
		# 
		# return adapter.StdioTransport(log, ["python", "my_adapter.py"])
		# 
		# The second is a SocketTransport, which communicates with the 
		# adapter through a socket connection via DAP.

		host = configuration.get('host', 'localhost')
		port = int(configuration.get('port', 9000))
		
		return adapter.SocketTransport(log, host, port)

	async def install(self, log):
		"""
		When someone installs your adapter, they will also have to install it 
		through the debugger itself. That is when this function is called. It
		allows you to download any extra files or resources, or install items
		to other parts of the device to prepare for debugging in the future
		"""
		
		pass

	@property
	def installed_version(self) -> Optional[str]:
		# The version is only used for display in the UI
		return '0.0.1'

	@property
	def configuration_snippets(self) -> Optional[list]:
		"""
		You can have several configurations here depending on your adapter's 
		offered functionalities, but they all need a "label", "description", 
		and "body"
		"""

		return [
			{
				"label": "Template Adapter",
				"description": "A template debug adapter to show how to connect to the debugger",
				"body": {
					"name": "Template Adapter",
					"type": adapter_type,
					"request": "attach",  # can only be attach or launch
					"host": "localhost",
					"port": 9000,
				}
			},
		]

	@property
	def configuration_schema(self) -> Optional[dict]:
		"""
		I am not completely sure what this function is used for. However, 
		it must be present.
		"""

		return None

	async def configuration_resolve(self, configuration):
		"""
		In this function, you can take a currently existing configuration and 
		resolve various variables in it before it gets passed to start().

		Therefore, configurations where values are stated as {my_var} can 
		then be filled out before being used to start the adapter.
		"""

		return configuration
