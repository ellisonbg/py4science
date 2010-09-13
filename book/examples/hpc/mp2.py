"""mp3.py: A simple example of multiprocessing's pool API."""

from multiprocessing import Pool
import os
import time

def f(x):
    return x**10

def g(x):
    time.sleep(x)
    return "I just woke up!"

if __name__ == '__main__':
    p = Pool()

    print p.apply(f, (10,))

    print p.map(f, xrange(10))

    result = p.apply_async(g, (1.0,))
    print result.ready()
    print result.get(timeout=2.0)

    result = p.map_async(f, xrange(10))
    result.wait()
    assert result.successful(), "exception was raised."
    print result.get()

    p.close()
    p.join()