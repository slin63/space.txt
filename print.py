import sys
import time

def cprint(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.03)


string = 'Formless, yet lovingly shaped . . .'

cprint(string)
