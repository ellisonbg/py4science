.. _multiprocessing:

===============
Multiprocessing
===============

The :mod:`multiprocessing` `package
<http://docs.python.org/library/multiprocessing.html>`_ is in the standard
library of Python in versions 2.6 and later. It provides a couple of different
APIs that are useful in parallel and distributed computing. More specifically,
multiprocessing includes:

* A clone of the threading API that uses processes rather than threads, and 
  thus does not suffer from the restrictions of the GIL.
* A high level process pool class.
* A message oriented socket API.
* Server processes for managing shared objects.

In this tutorial, I will focus on how the threading API and process pool class
of multiprocessing can be used to parallelize code on a multicore CPU.

.. warning::
    Parts of the multiprocessing API, such as :class:`multiprocessing.Pool`
    won't work in an interactive python or IPython shell. These parts require
    you to write your code in a standalone script in the ``if __name__ ==
    '__main__':`` block. Examples will follow.

Threading API
=============

The basic idea of multiprocessing's threading API is that it provides classes
that have the same API as those in the :mod:`threading` and :mod:`Queue`
modules, but that use processes rather than threads. Thus, you should be able
to use the following import statements::

    from multiprocessing import Process as Thread
    from multiprocessing import JoinableQueue a Queue
    from Queue import Empty

and have all of your threading code magically use processes rather than
threads. The idea of this is brilliant! Multiprocessing also has process based
classes for semphores, condition variables, events, locks, etc. However,
multiprocessing's threading API is not 100% compatible, so in practice, you
may have to change parts of your threaded code to make the transition to
multiprocessing.

To show you that this really does work, let's see how we can adapt our
:class:`SimpleThreadPool` class in :mod:`pool` to use multiprocessing
instead:

.. literalinclude:: /code/pool.py
   :language: python
   :pyobject: SimpleProcessPool
   :linenos:

Notice that not much has changed other than the usage of
:class:`multiprocessing.Process` and :class:`multiprocessing.JoinableQueue`.
The main change is is in how the results are extracted from ``out_queue``.
This additional logic is required because :class:`multiprocessing.Queue` does
not have a fully cross platform :meth:`qsize` method.

Exercise:

* Write a simple function that uses :func:`os.getpid` and :func:`os.getppid`
  to print the pid of the process running the function and its parent.
* Use :class:`multiprocessing.Process` to run the function in a separate
  process.

Solution:

.. literalinclude:: /code/mp1.py
   :language: python
   :linenos:

The Pool API
============

Because the thread pool pattern is such a common and useful pattern,
multiprocessing comes with a very nice process pool implementation, in the
:class:`multiprocessing.Pool` class. Because it is more robust and powerful
that the :class:`SimpleProcessPool` implementation of this tutorial, 
:class:`multiprocessing.Pool` should be used in production code.

Here is the basic API of the :class:`multiprocessing.Pool` class:

:class:`Pool(processes=cpu_count(), initializer=None, initargs=None)`
    Create a pool of size ``processes``.

:attr:`Pool.apply(func, args=None, kwds=None)`
    Perform ``func(*args, **kwds)`` in the pool and return the result.

:attr:`Pool.apply_async(func, args=None, kwds=None, callback=None)`
    Same as :meth:`Pool.apply`, but asynchronously.

:attr:`Pool.map(func, iterable, chunksize=1)`
    A parallel version of Python's built-in :func:`map` function.

:attr:`Pool.map_async(func, iterable, chunksize=1, callback=None)`
    Same as :meth:`Pool.map`, but asynchronously.

:attr:`Pool.close()`
    Prevent any further tasks from being submitted to the pool and exit
    the worker processes when they finish.

:attr:`Pool.terminate()`
    Terminate all of the processes in the pool without finishing remaining
    work.

:attr:`Pool.join()`
    Wait for all of the worker processes to exit. One must first call
    :meth:`Pool.terminate` or :meth:`Pool.close`.

Once you create a :class:`Pool` instance, you can use :func:`Pool.apply` and
:func:`Pool.apply_async` to execute a function a single time on one of the
workers in the pool. Similarly, you can use :func:`Pool.map` and
:func:`Pool.map_async` to call a function with multiple times in parallel. The
``*_async`` variants of the functions return an :class:`AsyncResult` instance
that can be used to retrieve the result at a later time:

:attr:`AsyncResult.get(timeout=None)`
    Get the result with a timeout.

:attr:`AsyncResult.wait(timeout=None)`
    Wait until the result is ready

:attr:`AsyncResult.ready()`
    Is the result ready?

:attr:`AsyncResult.successful()`
    Did the task complete without an exception.

Consult the `official documentation 
<http://docs.python.org/library/multiprocessing.html#module-multiprocessing.pool>`_
of :class:`multiprocessing.Pool` for a more complete description of its APIs.

Exercise:

* In a standalone script, create a simple function of one argument.
* In that script, create a ``if __name__ == '__main__':`` block that
  uses a :class:`multiprocessing.Pool` instance to call the simple function
  using the various methods of the pool.
* Experiment with the ``*_async`` variants of these methods and the
  :class:`AsyncResult` API. For this it might be helpful to create a second 
  function that simply calls :func:`time.sleep`.

Solution:

.. literalinclude:: /code/mp2.py
   :language: python
   :linenos:

Warnings and caveats
====================

There are a number of things to be aware of when using multiprocessing:

* Not everything will work interactively.
* The threading API is not 100% compatible with :mod:`Queue` and 
  :mod:`threading`.
* There are numerous platform inconsistencies, especially on Windows.
* On Linux and OS X, multiprocessing uses :func:`os.fork` and not everything
  likes to be forked (threads, GUIs).

The multiprocessing documentation has a more complete set of 
`programming guidelines 
<http://docs.python.org/library/multiprocessing.html#programming-guidelines>`_
that should be consulted.

When to use multiprocessing
===========================

* You want to run your code primarily on multicore CPUs, not clusters or 
  supercomputers.
* You are enthusiastic about the threading API.
* You don't want any dependencies other than Python's standard library.
* You don't need high level message passing constructs such as those provided by
  the Message Passing Interface (MPI).
* You are not dealing with things that don't like to be forked.
* You can live with higher communication overhead than threads. My tests show
  that with a pool size of two, the communication overhead of
  :class:`SimpleProcessPool` is about three times that of
  :class:`SimpleThreadPool`.
* You want to write pure Python code and not mess with C/C++.

Examples
========

Let's try to parallelize our examples using multiprocessing.

Prime numbers
-------------

Because multiprocessing uses processes, it does not have the limitations of
the GIL that thwarted our using the :mod:`threading` module to parallelize
pure Python code.

Exercise:

* Use :class:`multiprocessing.Pool` to parallelize the slower, pure Python
  version of :func:`isprime` and :func:`sum_primes` in :mod:`prime1`. Remember
  that you will need to put this code into a standalone script with a 
  ``if __name__ == '__main__'`` block.
* Time the code using :func:`time.clock` and determine its parallel speedup.
* Try to speedup the code further by increasing the ``chunksize`` in calls
  to :meth:`Pool.map`.

Solution:

.. literalinclude:: /code/prime1_mp.py
   :language: python
   :linenos:

Running this code on two cores, I get:

.. code-block:: bash

    $ python prime1_mp.py
    Serial isprime time:  0.0892119407654
    Serial sum_primes time:  38.4743008614
    Parallel isprime time:  0.0569860935211
    Parallel sum_primes time:  21.6022059917
    Speedup of isprime on 2 cores: 1.565504
    Speedup of sum_primes on 2 cores: 1.781036


Exercise:

* Repeat the previous exercise for the faster Cython versions of
  :func:`isprime` and :func:`sum_primes` in :mod:`prime2`.

Solution:

.. literalinclude:: /code/prime2_mp.py
   :language: python
   :linenos:

Running this code on two cores, I get:

.. code-block:: bash

    $ python prime2_mp.py
    Serial isprime time:  0.0113651752472
    Serial sum_primes time:  1.69273495674
    Parallel isprime time:  0.00905704498291
    Parallel sum_primes time:  1.05797791481
    Speedup of isprime on 2 cores: 1.254844
    Speedup of sum_primes on 2 cores: 1.599972

Here is summary of the speedups of :func:`sum_primes` we have achieved 
using Cython and multiprocessing:

* A speedup of 23x by rewriting in Cython.
* A speedup of 1.5x by using multiprocessing.
* Total speedup of 23*1.5 = 34.5x.

Random matrices
---------------
