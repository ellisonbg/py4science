.. _threading:

=========
Threading
=========

Overview
========

* Threads are semi-independent execution paths contained in a process 
  that can execute concurrently and in parallel on a multicore CPU.
* Threads are a universal OS/hardware level abstraction for concurrency and
  parallelism.
* Different threads in a process have a shared memory space, which allows 
  them to communicate very quickly.  Processes, on the other hand, can
  only communicate using slower interprocess communication (IPC) techniques 
  (pipes, sockets, files).
* Threaded programming has a bad name because of the difficulty of managing
  shared resources, such as memory using conditions, locks, semaphores, etc.
  However, queues allow you to pass messages between threads without sharing
  resources.
* There is some evidence that threads that share resources will perform very
  poorly on many core architectures.

For some interesting points about threads, see Edwards Lee's
`The Problem with Threads <http://www.eecs.berkeley.edu/Pubs/TechRpts/2006/EECS-2006-1.pdf>`_.

The Global Interpreter Lock (GIL)
=================================

The standard C implementation of Python (CPython) has full support for POSIX
and Windows threads in the :mod:`threading` `module 
<http://docs.python.org/library/threading.html#module-threading>`_ of the
standard library. This allows Python programs to utilize threads for
*concurrency*. However, because of the Global Interpreter Lock (GIL), threads
running Python code cannot be used for *parallelism*.

What is the GIL and why does it prevent the usage of threads for parallelism?

From the `Python docs <http://docs.python.org/c-api/init.html?highlight=gil#thread-state-and-the-global-interpreter-lock>`_:

    The Python interpreter is not fully thread safe. In order to support
    multi-threaded Python programs, there’s a global lock, called the global
    interpreter lock or GIL, that must be held by the current thread before it can
    safely access Python objects

This means that Python threads only *appear* to run at the same time.
Underneath the hood, the Python interpreter makes sure that only one thread
executes at a time. For a detailed explanation of how the GIL works in
CPython, see these excellent `talks <http://www.dabeaz.com/talks.html>`_ by 
David Beazley. Because only one thread can actually run at a time, this 
prevents true parallelism on multicore CPUs.

Here are some additional points about the GIL:

* It is considered an implementation detail of the Python language and is not
  part of its official specification.
* The GIL is present in some implementations of the Python language (CPython,
  Stackless, PyPy, Unladen Swallow) but not in others (Jython, IronPython).
* The GIL does make it easier to write extensions for CPython.
* Many people, including myself, would like to see the GIL removed.
* Some people want to keep the GIL on philosophical grounds 
  ("threads are evil").
* Some people have successfully removed the GIL, but at the cost of worsened
  single threaded performance.

Using threads for parallelism in Python
=======================================

Even with the restrictions of the GIL, there are a couple of clever ways to
use threads in your Python program for true parallelism on a multicore CPU.
The general idea is the following:

* The relevant code must be written in pure C/C++ and can contain no calls
  to the Python/C API.
* The relevant code must be wrapped into Python and called in way that
  releases the GIL before the C/C++ code is called. If you don't release the
  GIL, the Python interpreter will completely halt while your C/C++ code 
  runs to completion. You also have to convert all Python objects into
  appropriate C/C++ data types and pass those to the C/C++ code.

This also means that if you have a C/C++ library that uses threads, and you
call that library while releasing the GIL, you will get parallelism on
a multicore CPU.

Using Cython
------------

The simplest way of implementing this technique is to use `Cython
<http://www.cython.org/>`_, which has a ``nogil`` keyword that allows you to
easily manage the GIL when calling C/C++ code.

First, You can call a C/C++ function contained in an external C/C++ library
and release the GIL while doing so, using the ``with nogil:`` construct:

.. sourcecode:: cython

    cdef extern from "my_library.h":
        void my_c_function(double *, double *, double *, int)
    # ...
    with nogil:
        # a, b, c, n are C data types
        my_c_function(&a, &b, &c, n)

When this code is called in a thread, the function :func:`my_c_function` can
run in parallel with other Python code.

Second, you can write a function in Cython that will release the GIL
during critical sections:

.. literalinclude:: /code/vector_add.pyx
   :language: cython
   :lines: 15-

When the :func:`vector_add` function is run in a thread, the ``with nogil:``
section can run in parallel with other Python code. 

There are a number of downsides to this approach:

* You have to choose between parallelism and Python. The parts of your code
  that run in parallel can't be written in Python. Cython does ease the pain
  a bit however.
* The resulting code will only work on a multicore CPU, not on a cluster or
  supercomputer.
* If your program is memory bandwidth limited, you probably won't see a
  significant speedup on a multicore CPU anyways. You may even see a slow
  down if cache contention becomes an issue.

Intel MKL
---------

Some C/C++ libraries already have built-in multithreading support. If you
simply call these libraries from Python you might magically get a speedup 
on a multicore CPU. A great example of this is Intel's 
`Math Kernel Library <http://software.intel.com/en-us/intel-mkl/>`_ 
(MKL) that recent releases of 
`Enthought Python Distribution <http://www.enthought.com/products/epd.php>`_ 
(EPD) are `linked against <http://www.enthought.com/epd/mkl/>`_.

Here is an example that shows how to use a multithreaded Intel MKL function
through ``numpy.linalg``:

.. sourcecode:: ipython

    In [1]: import numpy as np

    In [2]: a = np.random.rand(2000,2000)

    In [3]: import mkl

    In [4]: mkl.get_max_threads()
    Out[4]: 4

    In [5]: %timeit np.linalg.eigvals(a)
    1 loops, best of 3: 6.77 s per loop

    In [6]: mkl.set_num_threads(1)

    In [7]: mkl.get_max_threads()
    Out[7]: 1

    In [8]: %timeit np.linalg.eigvals(a)
    1 loops, best of 3: 9.05 s per loop

This example was run on a Quad Core, Intel Core i7 860 CPU running Ubuntu
10.04. The 32 bit version of EPD 6.2 was used. Other functions in
:mod:`numpy.linalg` that use MKL include :func:`det`, :func:`eig`, 
:func:`eigh`, :func:`eigvalsh`, :func:`inv` and :func:`svd`.

Exercise:

* If you have EPD 6.1 or 6.2, try benchmarking another function in
  :mod:`numpy.linalg` that uses the multithreaded MKL.
* Import :mod:`mkl` and see if changing the number of threads affects the
  performance of the function.
* Do some functions in :mod:`numpy.linalg` get a better parallel speedup than
  others when running on multiple cores?
* Look at the NumPy and SciPy source code to see if you can determine which
  functions and methods use the Intel MKL. Also, look at the Intel MKL
  documentation to see which MKL routines are multithreaded.

The `numexpr <http://code.google.com/p/numexpr/>`_ package also has the
ability to use the multithreaded Intel MKL routines, but as of June 2010,
numexpr does not come with EPD. Furthermore, because EPD does not seem to ship
with the MKL header files, you can't build numexpr against the MKL in EPD.
Thus to get an MKL enabled numexpr you will have to purchase a license for MKL
and build numexpr yourself. Maybe EPD could ship an MKL linked numexpr?

The threading API
=================

To run code in parallel using threads, you will need to use the
:class:`threading.Thread` class from the :mod:`threading` `module
<http://docs.python.org/library/threading.html#module-threading>`_ of the
standard library. While threads can share memory, your life will be most
pleasant if you don't utilize this capability. The easiest way of using
threads without sharing memory is to use the :class:`~Queue.Queue` class of the
:mod:`Queue` `module 
<http://docs.python.org/library/queue.html#module-Queue>`_ to pass messages
between threads. This is the approach that is described here.

First, let's look at the API for :class:`Queue.Queue` and
:class:`threading.Thread`. Here is a description of the core methods of the 
:class:`~Queue.Queue` class, which is a "first in first out" (FIFO) queue:

:class:`Queue(maxsize=0)`
    Create a queue object with a maximum size.

:attr:`Queue.put(foo==bar)`
    Put an item on the queue.

:attr:`Queue.get(a =10)`
    Get an item from the queue.

:attr:`Queue.full()`
    Is the queue full?

:attr:`Queue.empty()`
    Is the queue empty?

Likewise, here are the core methods and attributes of the 
:class:`threading.Thread` class:

:class:`Thread(group=None, target=None, name=None, args=(), kwargs={})`
    Create a thread with name that runs ``target(*args, **kwargs)``.

:attr:`Thread.start()`
    Start the thread's activity by calling its target.

:attr:`Thread.join(timeout=None)`
    Wait until the thread terminates.

:attr:`Thread.is_alive()`
    Is the thread still running

:attr:`Thread.name`
    The name the thread.

:attr:`Thread.daemon`
    Boolean to indicate if the thread is a daemon.

Exercise:

* Write a simple function with no argument and call it in a thread.
* Create a :class:`Queue.Queue` instance and play around with
  :meth:`Queue.put` and :meth:`Queue.get`. What happens if you call 
  :meth:`Queue.get` while the queue is empty? What do the ``block`` and
  ``timeout`` arguments to :meth:`Queue.put` and :meth:`Queue.get` do?

Solution:

.. sourcecode:: ipython

    In [1]: from threading import Thread, current_thread

    In [2]: def f():
       ...:     print "Hello from thread: ", current_thread().name
       ...:     
       ...:     

    In [3]: t = Thread(target=f, name='f')

    In [4]: t.daemon = True

    In [5]: t.start()
    Hello from thread:  f

    In [6]: t.join()

    In [7]: t.is_alive()

    Out[7]: False

Thread pools
============

To use threads for parallelism, it is often helpful to use a thread pool. A
thread pool creates a small number of worker threads and then distributes
tasks to the worker threads using a queue. There are two reasons a thread
pool is helpful:

* The overhead of thread creation only happens once when the pool is created.
* The pool will dynamically load balance the tasks amongst the worker threads,
  which is more efficient if the tasks take different amounts of time to 
  complete.

The :mod:`pool` module of this tutorial contains a very basic thread pool 
implementation that uses :class:`Queue.Queue` and :class:`threading.Thread`:

.. literalinclude:: /code/pool.py
   :language: python
   :pyobject: SimpleThreadPool
   :linenos:

Exercise:

* Import :mod:`pool.SimpleThreadPool` and use its :meth:`map` method to
  execute a single argument Python function over a range of arguments.
* Benchmark this calculation and compare it with a serial calculation
  that uses Python's built-in :func:`map` function.
* Do you see a parallel speedup?  Should you?

For a more powerful thread pool implementation, see Christopher Arndt's
`Threadpool <http://chrisarndt.de/projects/threadpool/>`_ package.

When to use threads
===================

* You want very low communication overhead. You can't beat threads in this
  respect.
* It is easy to write the parallel code in pure C/C++ by hand or using Cython.
* You already have a C/C++ library that you can call with ``nogil``.

Examples
========

Prime numbers
-------------

Now, let's revisit our prime number example and see if we can get a speedup
using threads. Remember, we will only get a speedup if a critical section 
of code i) is written in pure C/C++ and ii) releases the GIL. This is done
in the fast Cython version of :func:`isprime` and :func:`sum_primes` in
:mod:`prime2`.  Note the usage of the ``nogil`` keyword:

.. literalinclude:: /code/prime2.pyx
   :language: cython
   :linenos:

In principle, we should be able to observe a parallel speedup on a multicore
CPU if this code is called for multiple arguments using a thread pool.

Exercise:

* Create a :class:`SimpleThreadPool` and use :meth:`SimpleThreadPool.map` to
  run :func:`prime2.isprime` for multiple arguments in parallel. Time the
  calculation and play with the arguments so that the calculation takes a
  significant amount of time (at least one second).
* Now perform and time a serial calculation using :func:`prime2.isprime` and
  Python's built-in :func:`map` function using the same arguments. Calculate
  the parallel speedup.
* Repeat this proceedure to find the parallel speedup of
  :func:`prime2.sum_primes`. For which function is the parallel speedup
  better?  Why?
* Repeat this for the slower versions of these functions in :mod:`prime1`.
  What do you observe?

Solution:

Here is what I observe for :func:`prime2.isprime`:

.. sourcecode:: ipython

    In [1]: import pyximport

    In [2]: pyximport.install()

    In [3]: import prime2

    In [4]: import pool

    In [5]: tp = pool.SimpleThreadPool(2)

    In [6]: %timeit tp.map(prime2.isprime, xrange(0,20000))
    1 loops, best of 3: 1.24 s per loop

    In [7]: %timeit map(prime2.isprime, xrange(0,20000))
    100 loops, best of 3: 11.7 ms per loop

    In [8]: 11.7/1240

    Out[8]: 0.0094354838709677421  # anti-speedup!

Here is what I observe for :func:`prime2.sum_primes`:

.. sourcecode:: ipython

    In [12]: %timeit tp.map(prime2.sum_primes, xrange(0,5000))
    1 loops, best of 3: 932 ms per loop

    In [13]: %timeit map(prime2.sum_primes, xrange(0,5000))
    1 loops, best of 3: 1.8 s per loop

    In [14]: 1.8/0.932

    Out[14]: 1.9313304721030042  # a speedup of almost 2x

Why do we observe a good speedup for :func:`prime2.sum_primes`, but a severe
*slowdown* for :func:`prime2.isprime`? This is because :func:`prime2.isprime`
does substantially less work per call. Each time the function is called using
the thread pool there is *communication overhead* (getting and putting from
the queues). If a function doesn't take very long to execute that overhead 
will dominates the calculation and eliminate the speedup.

Let's see if we can estimate what the overhead is for calling a function a
single time using our thread pool.

.. sourcecode:: ipython

    In [16]: def f(x): pass
    ....: 

    In [18]: %timeit tp.map(f, xrange(1000))
    10 loops, best of 3: 55.7 ms per loop

Thus, the communication overhead per function call in our thread pool is 55.7
microseconds. This overhead is *much* greater than the time it takes to execute
:func:`prime2.isprime` a single time:

.. sourcecode:: ipython

    In [20]: %timeit prime2.isprime(10000)
    1000000 loops, best of 3: 381 ns per loop

and much shorter than the time it takes to execute :func:`prime2.sum_primes`
a single time:

.. sourcecode:: ipython

    In [21]: %timeit prime2.sum_primes(2500)
    1000 loops, best of 3: 314 us per loop

This explains the observed speedups that we are seeing and provides us with
a general rule for parallel computing:

To observe a good parallel speedup, the execution time of your code must
be significantly larger than the communication overhead of the parallelization
strategy.

Exercise:

One way of beating the communication overhead is to batch the calls to the
function. In other words, write a new version of your function that operates
in multiple operands, and then parallelize that function instead by passing
it batches of arguments. This will reduce the overall communication overhead
by paying the price once for each batch of arguments, rather than once for
each argument.

* Based on our above study of the communication overhead of our thread pool,
  estimate the minimum batch size of arguments we expect to need to observe a
  parallel speedup of :func:`prime2.isprime`?
* Try to get a parallel speedup of the function :func:`prime2.isprime` by 
  using batching.

Random matrices
---------------
