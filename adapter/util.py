
from os.path import abspath, join, dirname, basename, split
from threading import Timer
from datetime import datetime
now = datetime.now()

#  Debugging this adapter
debug = True
log_file = abspath(join(dirname(__file__), '..', 'log.txt'))
open(log_file, 'w+').close()  # Creates and clears the file

ptvsd_path = join(abspath(dirname(__file__)), "python")


# --- Utility functions --- #

def log(msg):
    if debug:
        with open(log_file, 'a+') as f:
            f.write('\n' + now.strftime("%Y-%m-%d %H:%M:%S") + " - " + msg + '\n')


def run_in_new_thread(func, args=None):
    Timer(0.01, func, args=args).start()


