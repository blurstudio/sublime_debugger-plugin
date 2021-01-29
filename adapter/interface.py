
from sys import stdin, stdout
from queue import Queue
from util import CONTENT_HEADER, run_in_new_thread, log


debugger_queue = Queue()


def read_debugger_input(callback: function):
    """
    Reads DAP messages sent from the debugger through stdin and calls the
    function passed in as the callback with the message recieved.
    """

    while True:
        try:
            content_length = 0
            while True:
                header = stdin.readline()
                if header:
                    header = header.strip()
                if not header:
                    break
                if header.startswith(CONTENT_HEADER):
                    content_length = int(header[len(CONTENT_HEADER):])

            if content_length > 0:
                total_content = ""
                while content_length > 0:
                    content = stdin.read(content_length)
                    content_length -= len(content)
                    total_content += content

                if content_length == 0:
                    message = total_content
                    callback(message)

        except Exception as e:
            log("Failure reading stdin: " + str(e))
            return


def _debugger_send_loop():
    """
    Waits for items to show in the send queue and prints them.
    Blocks until an item is present
    """

    while True:
        msg: str = debugger_queue.get()
        if msg is None:
            return
        else:
            try:
                stdout.write('Content-Length: {}\r\n\r\n'.format(len(msg)))
                stdout.write(msg)
                stdout.flush()
                log('Sent to Debugger:', msg)
            except Exception as e:
                log("Failure writing to stdout (normal on exit):" + str(e))
                return


def start_response_thread():
    """
    Simple wrapper to start the debugger send loop below in a new thread
    """

    run_in_new_thread(_debugger_send_loop)

