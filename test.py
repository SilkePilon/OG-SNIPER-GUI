#!/usr/bin/env python

# taken from: http://stackoverflow.com/questions/7039114/waiting-animation-in-command-prompt-python

import threading
import time
import os

class CursorAnimation(threading.Thread):
    def __init__(self):
        self.flag = True
        self.animation_char = "|/-\\"
        self.idx = 0
        threading.Thread.__init__(self)

    def run(self):
        while self.flag:
            os.system("cls")
            print(self.animation_char[self.idx % len(self.animation_char)] + "\r",)
            self.idx += 1
            time.sleep(0.1)

    def stop(self):
        self.flag = False

if __name__ == '__main__':
    spin = CursorAnimation()

    # Start Animation
    spin.start()

    # Do something here
    # Example: sleep
    time.sleep(5)

    # Stop Animation
    spin.stop()