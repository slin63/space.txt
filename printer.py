import sys
import time


def cprint(string, t=0.04):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(t)
    print ''



