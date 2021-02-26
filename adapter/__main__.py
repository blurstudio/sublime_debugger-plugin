
"""

This script communicates with the Debugger over stdin/stdout following
the Debug Adapter Protocol (https://microsoft.github.io/debug-adapter-protocol/)

"""

from util import log, json, run_in_new_thread
from interface import DebuggerInterface
import time

interface = None


def main():
    """
    First function to be called. Creates a DebuggerInterface instance and starts it
    """

    global interface
    log("--- WARNING --- : Adapter not set up")

    # Create a DebuggerInterface instance in main, optionally passing a function 
    # to call when a message is recieved from the debugger
    interface = DebuggerInterface(on_receive=on_receive)

    # Now all you have to do is:
    interface.start()

    # And if you want a nonblocking statement:
    # interface.start_nonblocking()
    # 
    # But make sure main remains blocked, otherwise the adapter will stop.


def on_receive(message):
    """
    Gets called every time a new message is received from the debugger.
    This function is run in the same thread as the message-recieving loop, so make sure it is non-blocking.
    """

    # All dap messages are in json format, so you will probably want to convert them 
    # to dictionaries for convenience.
    dap_msg = json.loads(message)
    
    # Respond to debugger requests by making/formatting responses and putting them
    # in the debugger queue in their string/dumped form
    tmp = {'request_seq': dap_msg['seq']}
    res_msg = json.dumps(tmp)
    interface.send(res_msg)

    # If you need to do heavier processing, need blocking statements, 
    # or want controlled infinite loops, run an external function in a new thread.
    # Arguments can be passed as shown
    run_in_new_thread(blocking_function, args=("hello", "world"))


def blocking_function(arg1, arg2):
    
    while True:
        log(arg1 + " " + arg2 + "!")
        time.sleep(1)


if __name__ == '__main__':
    main()
