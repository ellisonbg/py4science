.. _serial_fast:

===============================
Making the serial versions fast
===============================

Donald Knuth:

    Premature optimization is the root of all evils

Corollary:

    Premature parallelization is no exception.

Remember, your main goal is to speed up your computation. Parallelization is 
one possible route to this end. There are other routes. The other option
to speedup your program is to simply make your serial version faster!

Why is this important?

* Maybe, if you are lucky, you won't need to parallelize after all.
* Speeding up a serial code is often very easy. Parallelization is almost
  always difficult.
* Parallelization will have the tendency to amplify the sub-optimal parts
  of your program.
* If your parallel code doesn't show good speedup, it will be difficult to
  discern why if the serial version is inefficient.

Here are some thing to try when speeding up the serial version of your code.

Techniques
==========

Time your code
--------------

First, you should know about IPython's ``%timeit`` magic, which is easy to use
and will suffice in most cases:

.. sourcecode:: ipython

    In [1]: import numpy as np

    In [2]: a = np.random.rand(1000,1000)

    In [3]: %timeit np.linalg.eigvals(a)
    1 loops, best of 3: 2.12 s per loop

If you have a standalone script that you want to run with timing, you can 
use IPython's ``%run`` magic with the ``-t`` flag:

.. sourcecode:: ipython

    In [1]: %run -t pool.py

    IPython CPU timings (estimated):
      User  :   0.001133 s.
      System:   0.000113 s.

Finally, if you cannot use IPython for timing code, you can use the
:func:`time` or :func:`clock` functions in the standard library's
:mod:`time` `module
<http://docs.python.org/library/time.html#module-time>`_. Which of these
should you use? The Python docs are actually quite confusing on this issue,
but the following code in the :mod:`timeit` module is quite clear::

    if sys.platform == "win32":
        # On Windows, the best timer is time.clock()
        default_timer = time.clock
    else:
        # On most other platforms the best timer is time.time()
        default_timer = time.time

Here is an example of how to use this in a cross platform manner:

.. sourcecode:: ipython

    In [10]: from timeit import default_timer as timer

    In [11]: t1 = timer()

    In [12]: t2 = timer()

    In [13]: print "Elapsed time in seconds: ", t2-t1
    Elapsed time in seconds:  0.003032

Profile your code
-----------------

Profiling your code will help you to find where the bottlenecks are. Some
things to look at:

* IPython's ``%run -p myscript.py``.
* The :mod:`profile` and :mod:`cProfile` 
  `modules <http://docs.python.org/library/profile.html#module-cProfile>`_ 
  of the standard library.
* Robert Kern's line_profiler and kernprof 
  `packages <http://packages.python.org/line_profiler/>`_.

Make sure the algorithm you are using is optimal
------------------------------------------------

If you are using an algorithm that scales as :math:`O(n^3)` and there is
another algorithm that scales as :math:`O(n\log{n})`, first rewrite your
program to use the better algorithm. Do this before anything else!

Use NumPy rather than lists or tuples
-------------------------------------

If have large lists or tuples, especially if they are multidimensional and
have simple element types (int, float, double, etc.), you should be using
`NumPy <http://numpy.scipy.org/>`_ arrays. Just by doing this and using
NumPy's optimized functions and methods, you could get a significant speedup.

Try numexpr to improve array based expressions
----------------------------------------------

The `numexpr <http://code.google.com/p/numexpr/>`_ package uses a just in time
compiler (JIT) to compile array expressions on the fly. It eliminates
temporary arrays makes uses a variety of techniques to make computations cache
friendly.  Here is a simple example:

.. sourcecode:: ipython

    In [1]: import numpy as np

    In [2]: import numexpr as ne

    In [3]: a = np.random.rand(1e6)

    In [4]: b = np.random.rand(1e6)

    In [5]: %timeit a**2 + b**2 + 2*a*b
    10 loops, best of 3: 74.5 ms per loop

    In [6]: %timeit ne.evaluate('a**2 + b**2 + 2*a*b')
    10 loops, best of 3: 23 ms per loop

    In [7]: 74.5/23

    Out[7]: 3.2391304347826089  # speedup

Furthermore, if you compile numexpr with support for Intel MKL (Math Kernel
Library) you will also get parallel multicore support.

Rewrite critical sections in a compiled language
------------------------------------------------

If your program is written in pure Python, you can likely speed it up by
a factor of 2-100 by identifying the critical sections and rewriting them
in a compiled language.  Then you can wrap the compiled code and call it from
Python using a number of different tools:

* `Cython <http://www.cython.org/>`_
* `ctypes <http://docs.python.org/library/ctypes.html#module-ctypes>`_
* `SWIG <http://www.swig.org/>`_
* `f2py <http://www.scipy.org/F2py>`_
* `Boost.Python <http://www.boost.org/doc/libs/1_43_0/libs/python/doc/index.html>`_

If you have not tried any of these I recommend starting with Cython.

Learn more about the Python language and computer architecture
--------------------------------------------------------------

* Sometimes, simple Python 
  `performance tips <http://wiki.python.org/moin/PythonSpeed/PerformanceTips>`_ 
  go a long ways.
* Randall Hyde's "Write Great Code", Volumes 
  `I <http://nostarch.com/greatcode.htm>`_ and 
  `II <http://nostarch.com/greatcode2.htm>`_ provide fantastic descriptions
  of how to write high level code while taking into consideration the low
  level details of computer architecture.

Examples
========

Now let's see if we can speed up our examples.

Prime numbers
-------------

To speed up our prime number examples, we will use Cython. This is not meant
to be a Cython tutorial, so we simply show how this is done:

.. literalinclude:: /code/prime2.pyx
   :language: cython

To import this into IPython you can use the :mod:`pyximport` module that
comes with Cython:

.. sourcecode:: ipython

    In [1]: import pyximport

    In [2]: pyximport.install()

    In [3]: import prime2

Exercise:

* Benchmark the Cythonized :func:`isprime` and :func:`sum_primes` functions
  in :mod:`prime2`.
* Compute the speedup you got from simply using Cython.

Solution:

.. sourcecode:: ipython

    In [5]: %timeit map(prime2.isprime, xrange(20000))
    100 loops, best of 3: 9.72 ms per loop

    In [6]: 86.8/9.72 # prime1.isprime took 86.8 ms

    Out[6]: 8.9300411522633745


    In [7]: %timeit map(prime2.sum_primes, xrange(1000,2000))
    10 loops, best of 3: 178 ms per loop

    In [8]: 4020/178. # prime1.sum_primes took 4.02 s

    Out[8]: 22.584269662921347

Keep in mind that we would have to work very hard to get that type of speedup
using parallelization.

Random matrices
---------------
