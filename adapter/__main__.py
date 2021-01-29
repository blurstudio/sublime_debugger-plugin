
"""

This script communicates with the Debugger over stdin/stdout following
the Debug Adapter Protocol (https://microsoft.github.io/debug-adapter-protocol/)

"""

from interface import debugger_queue, start_response_thread, read_debugger_input
from util import log, json, run_in_new_thread
import time


def main():
    """
    First function to be called. Launches necessary threads to read/write to stdin/stdout
    """

    log("--- WARNING --- : Adapter not set up")

    # Call this function at the start of main. It starts the thread that will send queued 
    # messages to the debugger through stdout
    start_response_thread()

    # Call this function at the end of main, with your callback function as the argument
    read_debugger_input(callback)


def callback(message: str):
    """
    Gets called every time a new message is received from the debugger.
    The callback is run in the same thread as the recieving loop, so make sure it is non-blocking.
    """

    # All dap messages are in json format, so you will probably want to convert them 
    # to dictionaries for convenience.
    dap_msg = json.loads(message)
    
    # Respond to debugger requests by making/formatting responses and putting them
    # in the debugger queue in their string/dumped form
    tmp = {'request_seq': dap_msg['seq']}
    res_msg = json.dumps(tmp)
    debugger_queue.put(res_msg)

    # If you need to do heavier processing, need blocking statements, 
    # or want controlled infinite loops, run an external function in a new thread.
    # Arguments can be passed as shown
    run_in_new_thread(blocking_function, args=("hello", "world"))


def blocking_function(arg1: str, arg2: str):
    
    while True:
        log(arg1 + " " + arg2 + "!")
        time.sleep(1)


if __name__ == '__main__':
    main()
