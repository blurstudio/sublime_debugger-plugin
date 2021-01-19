
from os.path import abspath, join, dirname
from threading import Timer
from datetime import datetime
import json

#  Debugging this adapter
debug = True
log_file = abspath(join(dirname(__file__), '..', 'log.txt'))

if debug:
    open(log_file, 'w+').close()  # Creates and/or clears the file


# --- Utility functions --- #

def log(msg, json_msg=None):
    if debug:

        if json_msg:
            msg += '\n' + json.dumps(json.loads(json_msg), indent=4)  # indent the json for readability

        with open(log_file, 'a+') as f:
            f.write('\n' + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - " + msg + '\n')


def run_in_new_thread(func, args=None):
    Timer(0.01, func, args=args).start()


