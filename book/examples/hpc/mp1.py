"""mp1.py: A simple example of multiprocessing's threading API."""

import os
from multiprocessing import Process

def f():
    print "Hi from pid:", os.getpid()
    print "My parent pid is:", os.getppid()

if __name__ == '__main__':
    print "Parent pid is:", os.getpid()
    p = Process(target=f)
    p.start()
    p.join()
