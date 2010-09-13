.. _picloud:

=======
PiCloud
=======

Overview
========

PiCloud is a commercial startup that offers parallel computing for Python "in
the cloud".

.. image:: picloud_screen.jpg
   :width: 500
   :height: 384

The basic idea is that you give PiCloud a Python function and arguments and it
will apply the function to the arguments in its high-performance, scalable
cloud. By doing this many times (PiCloud has a :func:`map` interface) you
can parallelize your code.

While PiCloud is not entirely open source, Enthought and PiCloud have an
agreement that makes the usage of PiCloud quite nice for users of EPD. This
agreement means that:

1. PiCloud's :mod:`cloud` client package ships with EPD.
2. PiCloud servers have EPD (NumPy, SciPy, matplotlib, etc.) installed on
   them, so your PiCloud jobs (functions) can use these libraries out of the 
   box.

Thus, for many of us, it is worth looking at. Here are some highlights of
PiCloud:

* PiCloud has a scalable cluster of servers running on Amazon Web Services
  (that is the "the cloud" in this case). The server infrastructure is
  not open source, but...
* You use their open source client library (:mod:`cloud`) to connect to
  their cloud and run jobs.
* Jobs are simply Python functions with arguments.
* You pay by the millisecond of CPU time, but right now they have a free
  limited registration beta.
* They have a very slick web interface for monitoring and managing your jobs.
* They do lots of cool magic to to detect which Python modules your function
  needs and then automagically transfer them to their servers.
* They have a multiprocessing based simulator that allows you to use the same
  cloud API on your multicore CPU.

The cloud API
=============

Here is an overview of the :mod:`cloud` package. This package is installed
on your local host and is used to submit jobs to the PiCloud cloud or
your local host.

Configuration
-------------

When using the :mod:`cloud` package, you first need to decide where you want
to run your jobs.  There are two options:

1. On your own multicore CPU.  This is called "simulator mode". 
2. The real PiCloud cloud.

The following two function allow you to make this choice:

:attr:`cloud.start_simulator(force_restart=False)`
    Run the cloud locally using multiprocessing. Lower latency, but not
    as many core as the cloud.

:attr:`cloud.setkey(api_key, api_secretkey)`
    Configure your PiCloud account. Higher latency, but lots of cores.

I have a PiCloud account, so I will run on the PiCloud cloud:

.. sourcecode:: ipython

    In [1]: import cloud

    In [2]: cloud.is_simulated()

    Out[2]: False

If you don't have a PiCloud account and want to try the examples, you can 
start the multiprocessing based simulator.

.. sourcecode:: ipython

    In [1]: import cloud

    In [2]: cloud.start_simulator()

    In [3]: cloud.is_simulated()

    Out[3]: True


Job submission and control
--------------------------

The core of the :mod:`cloud` API consists of functions for submitting 
and managing jobs. In PiCloud, a job is simply a Python function
along with its arguments. In the current API, you can only pass positional
arguments to functions and not keyword arguments.

The :func:`call` and :func:`result` functions are the starting point for
executing code and getting the result:

:attr:`cloud.call(func, *args, **kwargs)`
    Call ``func(*args)`` on the cloud and return a job id. The job id
    is used in other function to monitor and manage the job.

:attr:`cloud.result(jids, timeout=None)`
    Return the result of job or jobs. Calls :func:`cloud.join` internally.

.. sourcecode:: ipython

    In [15]: def f(x):
       ....:     return x**2
       ....: 

    In [16]: cloud.call(f, 2**16)

    Out[16]: 14


    In [17]: cloud.result(14)

    Out[17]: 4294967296L

Like the other tools covered in this tutorial, :mod:`cloud` also has a 
parallel :func:`map` implementation:

:attr:`cloud.map(func, *sequences)`
    A parallel version of Python's built-in :func:`map` function.

.. sourcecode:: ipython

    In [14]: cloud.map(f, range(10))

    Out[14]: [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

The following provide additional ways of managing jobs and getting their
results.

:attr:`cloud.iresult(jids, timeout=None)`
    Like :func:`cloud.result` but returns an iterable.

:attr:`cloud.status(jids)`
    Get the status of the job or jobs.

:attr:`cloud.kill(jids)`
    Kill the job or jobs.

:attr:`cloud.join(jids, timeout=None)`
    Wait for the job or jobs to complete.

Files
-----

PiCloud also has a cloud filesystem. The :mod:`cloud.files` sub-module has
functions for moving files between your local host and the cloud filesystem.
This API does not work in simulation mode.

:attr:`cloud.files.put(file_path)`
    Send a local file to the cloud filesystem. Works from the cloud as well.

:attr:`cloud.files.get(file_name)`
    Retrieve a file from the cloud filesystem. Works from the cloud as well.

:attr:`cloud.files.delete(file_name)`
    Delete a file by name from the cloud filesystem.

When to use PiCloud
===================

* You don't own a cluster, supercomputer or cloud and don't want to purchase
  or maintain one.
* You want to *scale*.
* You do have money to spend.
* You don't mind using a partially proprietary solution.
* You want something that "just works" with EPD.
* You can live with high latency (your tasks take well over 1 second).
* You can get your modules and packages uploaded and running on their servers.

Examples
========

Prime numbers
-------------

Let's try out PiCloud with our slower :mod:`prime1.sum_primes` function. We
will use this so we don't have to deal with installing the Cython based
:mod:`prime2` on PiCloud's servers (this is possible, but we want to keep
this example simple).

The following example is run on PiCloud's real cloud. For small integers, the
latency of PiCloud makes it impossible for us to get a parallel speedup:

.. sourcecode:: ipython

    In [1]: import cloud

    In [2]: cloud.is_simulated()

    Out[2]: False


    In [3]: import prime1

    In [4]: %timeit map(prime1.sum_primes, range(1000,1010))
    10 loops, best of 3: 25.9 ms per loop

    In [5]: %timeit cloud.map(prime1.sum_primes, range(1000,1010))
    1 loops, best of 3: 600 ms per loop

As we look at increasingly larger integers, PiCloud starts to show promise:

.. sourcecode:: ipython

    In [6]: %timeit map(prime1.sum_primes, range(10000,10010))
    1 loops, best of 3: 367 ms per loop

    In [7]: %timeit cloud.map(prime1.sum_primes, range(10000,10010))
    1 loops, best of 3: 451 ms per loop

    In [8]: %timeit map(prime1.sum_primes, range(100000,100010))
    1 loops, best of 3: 6.44 s per loop

    In [9]: %timeit cloud.map(prime1.sum_primes, range(100000,100010))
    1 loops, best of 3: 509 ms per loop

    In [10]: 6.44/0.509

    Out[11]: 12.652259332023576

This shows that with PiCloud, you have to make sure your functions take 
significantly longer than the overhead of moving things onto the cloud.
But, the good news is that if you are in that regime, PiCloud provides a very
simple and easy way to parallelize your Python code.

Random matrices
---------------
