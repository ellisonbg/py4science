.. _ipython:

=======
IPython
=======

Overview
========

IPython is an interactive computing environment for Python. You may already be
familiar with its enhanced interactive Python shell that has been used
throughout this tutorial:

.. sourcecode:: ipython

    $ ipython
    Enthought Python Distribution -- http://code.enthought.com

    Python 2.6.5 |EPD 6.2-1 (32-bit)| (r265:79063, May 28 2010, 15:13:03) 
    Type "copyright", "credits" or "license" for more information.

    IPython 0.10 -- An enhanced Interactive Python.
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object'. ?object also works, ?? prints more.

    In [1]: import math

    In [2]: math.sqrt?
    Type:		builtin_function_or_method
    Base Class:	<type 'builtin_function_or_method'>
    String Form:	<built-in function sqrt>
    Namespace:	Interactive
    Docstring:
        sqrt(x)
    
        Return the square root of x.

The IPython interactive shell has a number of popular features including:

* Tab completion.
* Access to previous results (``_10``).
* Magic command system (``%magic``).
* Easy access to the system shell (``!ls``).
* Easy access to documentation (``foo?``) and source code (``foo??``).

IPython also includes a framework for interactive parallel computing. This
section of the tutorial describes that aspect of IPython.

Architecture description
========================

Like multiprocessing, IPython uses processes for parallelism. IPython's 
parallel computing framework consists of three main components:

Engine
    IPython processes that execute Python code received over a network.
Controller
    A central process that manages a set of engines, presenting those engines
    to clients through a variety of interfaces.
Client
    A high-level class used to parallelize code by interacting with the
    engines through different interfaces.

Here are some other highlights of IPython's parallel computing framework:

* Full support for message passing using `MPI
  <http://www.mcs.anl.gov/research/projects/mpi/>`_ or `ØMQ
  <http://www.zeromq.org/>`_. But MPI is not a dependency.
* Extensible integration with popular batch systems (ssh, PBS, mpiexec,
  Windows HPC Server 2008 (upcoming release), SGE (upcoming release)).
* Rock solid, capabilities based security model that has been audited by the
  DoD.
* Designed for and tested on traditional clusters and supercomputer with 
  highly restricted access and firewalls.
* Lots of dependencies, but they come with EPD.

To perform a parallel computation using IPython, you will need to:

1. Start an IPython cluster (1 controller + multiple engines) using the
   :command:`ipcluster` command.
2. In the code you want to parallelize, create a
   :class:`MultiEngineClient` or
   :class:`TaskClient` class to connect to and interact with
   the cluster.

I now describe these steps in more detail.

Startup an IPython cluster
==========================

For the purposes of this tutorial, we will focus on running an IPython cluster
on a local host with a multicore CPU. In this context, you can start a
cluster with a controller and two engines using the :command:`ipcluster`
command as follows:

.. code-block:: bash

    $ ipcluster local -n 2

Once this is done, you can open a second terminal, startup IPython and begin
to interact with the cluster:

.. sourcecode:: ipython

    In [1]: from IPython.kernel import client

    In [2]: mec = client.MultiEngineClient()

    In [3]: mec.get_ids()

    Out[3]: [0, 1]


    In [4]: mec.execute('print "Hello world!"')

    Out[4]: 
    <Results List>
    [0] In [1]: print "Hello world!"
    [0] Out[1]: Hello world!

    [1] In [1]: print "Hello world!"
    [1] Out[1]: Hello world!

Full details about how to start the IPython controller and engines can be
found in the IPython documentation `here
<http://ipython.scipy.org/doc/nightly/html/parallel/parallel_process.html>`_.

.. note::
    If you are using a recent version of EPD, you may see a series of warnings
    when you run the examples in this tutorial. This is due to a minor API
    change in the Foolscap library, which IPython uses. The examples should
    still work fine however.

.. note::
    The only thing that changes when running IPython on a cluster or
    supercomputer is how the controller and engines are started by
    :command:`ipcluster` (simple process, ssh, PBS, mpirun, etc.). But the
    client API that you will use to parallelize your code is the same,
    regardless of method :command:`ipcluster` uses. This allows you to write
    your code once, and then run it on multicore CPUs, cluster and
    supercomputers.

.. warning::
    If there are Python modules you want to use on the engines, those modules
    need to be on your ``sys.path`` or you need to start :command:`ipcluster`
    from the directory containing those modules.

There are currently two clients for working with an IPython cluster:

:class:`IPython.kernel.client.MultiEngineClient`
    This client gives direct, explicit access to each engine managed by a
    controller. When using this client, the user has full control over which
    engine executes code or receives a Python object.

:class:`IPython.kernel.client.TaskClient`
    This client hides the identities of the engines from the user behind
    a dynamic load balancing queue.

We now give a brief overview of these interfaces and show examples of their
usage.

Multiengine interface
=====================

Here is an overview of the API for
:class:`IPython.kernel.client.MultiEngineClient`:

Creation
--------

:class:`MultiEngineClient(furl_or_file='')`
    Create a multiengine client by a FURL or a FURL containing file.

:attr:`MultiEngineClient.get_ids()`
    Get the ids of the active engines.

.. sourcecode:: ipython

    In [1]: from IPython.kernel import client

    In [3]: mec = client.MultiEngineClient()

    In [4]: mec.get_ids()

    Out[4]: [0, 1]

Code execution
--------------

:attr:`MultiEngineClient.execute(lines, targets=None, block=None)`
    Execute lines of Python code (as strings) on target engines.

:attr:`MultiEngineClient.map(func, *sequences)`
    Parallel version of Python's builtin map. No load balancing is performed
    but calls are batched/chunked.

These methods are used to execute Python code on the engines:

.. sourcecode:: ipython

    In [7]: mec.execute('a=10')

    Out[7]: 
    <Results List>
    [0] In [1]: a=10
    [1] In [1]: a=10


    In [8]: mec.map(lambda x: x**2, xrange(10))

    Out[8]: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

Another way of executing code interactively on the engines is to use the 
``%px`` magic:

.. sourcecode:: ipython

    In [9]: mec.activate()  # Activate this MultiEngineClient for %px

    In [10]: %px print a
    Parallel execution on engines: all

    Out[10]: 
    <Results List>
    [0] In [3]: print a
    [0] Out[3]: 10

    [1] In [3]: print a
    [1] Out[3]: 10

Data movement
-------------

The :attr:`push` and :attr:`pull` methods move data between the client
and the engines:

:attr:`MultiEngineClient.push(namespace, targets=None, block=None)`
    Push a dict of keys and values into the namespace of target engines.

:attr:`MultiEngineClient.pull(keys, targets=None, block=None)`
    Pull values by keys from the namespace of target engines.

.. sourcecode:: ipython

    In [14]: mec.push(dict(a=30,b='to the engines!'))

    Out[14]: [None, None]


    In [15]: mec.pull('a')

    Out[15]: [30, 30]


    In [16]: mec.pull('b')

    Out[16]: ['to the engines!', 'to the engines!']

Likewise :attr:`push_function` and :attr:`pull_function` do the same
thing for functions:

:attr:`MultiEngineClient.push_function(namespace, targets=None, block=None)`
    Push a function to the engines using a dict.

:attr:`MultiEngineClient.puLL_function(keys, targets=None, block=None)`
    Pull a function from the engines by name.

.. sourcecode:: ipython

    In [17]: def f(x):
       ....:     import math
       ....:     return math.sqrt(x)
       ....: 

    In [18]: mec.push_function(dict(enginef=f))

    Out[18]: [None, None]


    In [19]: mec.execute('y = enginef(2)')

    Out[19]: 
    <Results List>
    [0] In [4]: y = enginef(2)
    [1] In [4]: y = enginef(2)


    In [20]: px print y
    Parallel execution on engines: all

    Out[20]: 
    <Results List>
    [0] In [5]: print y
    [0] Out[5]: 1.41421356237

    [1] In [5]: print y
    [1] Out[5]: 1.41421356237

:attr:`scatter` and :attr:`gather` send or retrieve the partitions of a 
sequence from the clients to the engines:

:attr:`MultiEngineClient.scatter(key, sequence, targets=None, block=None)`
    Scatter the sequence to target engines as key.

:attr:`MultiEngineClient.gather(key, targets=None, block=None)`
    Gather the sequence named key from the target engines.

.. sourcecode:: ipython

    In [3]: import numpy

    In [4]: a = numpy.arange(0,100)

    In [5]: a

    Out[5]: 
    array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
           17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
           34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
           51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67,
           68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84,
           85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])


    In [6]: mec.scatter('a',a)

    Out[6]: [None, None]


    In [7]: mec.activate()

    In [8]: px print a
    Parallel execution on engines: all

    Out[8]: 
    <Results List>
    [0] In [1]: print a
    [0] Out[1]: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
     25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49]

    [1] In [1]: print a
    [1] Out[1]: [50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74
     75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99]


    In [9]: px import numpy
    Parallel execution on engines: all

    Out[9]: 
    <Results List>
    [0] In [2]: import numpy
    [1] In [2]: import numpy


    In [10]: px f = 2.0*numpy.cos(a) - 4.0*numpy.sin(a)
    Parallel execution on engines: all

    Out[10]: 
    <Results List>
    [0] In [3]: f = 2.0*numpy.cos(a) - 4.0*numpy.sin(a)
    [1] In [3]: f = 2.0*numpy.cos(a) - 4.0*numpy.sin(a)


    In [11]: f = mec.gather('f')

    In [12]: f

    Out[12]: 
    array([ 2.        , -2.28527933, -4.46948338, -2.54446503,  1.71992274,
            4.40302147,  3.03800257, -1.12014189, -4.24843305, -3.47073446,
            0.49794139,  4.00881222,  3.83399959,  0.13422542, -3.68895499,
           -4.12052719, -0.76370569,  3.29526329,  4.3245824 ,  1.3779004 ,
           -2.83561688, -4.44208107, -1.96451642,  2.31921558,  4.47067146,
            2.51181262, -1.75639516, -4.40978133, -3.00883489,  1.15842048,
            4.2606294 ,  3.4456353 , -0.53726   , -4.02620093, -3.81347129,
           -0.09465373,  3.71118803,  4.10498064,  0.72467297, -3.32189568,
           -4.31432877, -1.34018788,  2.86611556,  4.43732557,  1.92887892,
           -2.35297012, -4.47150928, -2.47896343,  1.79272997,  4.4161957 ,
            2.97943147, -1.19660831, -4.27249193, -3.42026617,  0.57653653,
            4.04327421,  3.79264422,  0.05507463, -3.73313032, -4.08911247,
           -0.68558348,  3.34826781,  4.30373711,  1.30237036, -2.89638969,
           -4.43222242, -1.8930903 ,  2.38654032,  4.47199677,  2.44592001,
           -1.82892432, -4.42226407, -2.94979463,  1.23470239,  4.28401973,
            3.39462908, -0.61576789, -4.0600307 , -3.77152001, -0.01549122,
            3.75478013,  4.07292394,  0.64644027, -3.37437761, -4.29280827,
           -1.26445081,  2.9264369 ,  4.42677202,  1.85715336, -2.41992353,
           -4.47213389, -2.41268497,  1.86497538,  4.42798597,  2.91992668,
           -1.27269974, -4.29521188, -3.36872603,  0.654951  ,  4.0764691 ])



:attr:`targets` and :attr:`block`
---------------------------------

:attr:`MultiEngineClient.targets`
    The target engines to apply all commands to (an integer id, a list of ids,
    or the string ``'all'``).

:attr:`MultiEngineClient.block`
    Should all commands block or not.

The :attr:`targets` attribute controls which engine are used for commands and
has a default of ``'all'``:

.. sourcecode:: ipython

    In [26]: mec.targets

    Out[26]: 'all'


    In [27]: mec.targets = 0

    In [28]: mec.execute('pi = 3')

    Out[28]: 
    <Results List>
    [0] In [67]: pi = 3

    In [29]: mec.targets = 1

    In [31]: mec.execute('pi = 3.14')

    Out[31]: 
    <Results List>
    [1] In [38]: pi = 3.14


    In [32]: mec.targets = 'all'

    In [33]: mec.pull('pi')

    Out[33]: [3, 3.1400000000000001]

The :attr:`block` attribute determines if commands will block. If set to
``False`` all commands will return a :class:`PendingResult` object, which can
be used to retrieve the result later.

.. sourcecode:: ipython

    In [34]: mec.block

    Out[34]: True


    In [35]: px import time
    Parallel execution on engines: all

    Out[35]: 
    <Results List>
    [0] In [68]: import time
    [1] In [39]: import time


    In [36]: mec.block = False

    In [37]: r = mec.execute('time.sleep(10)')

    In [38]: r.
    r.add_callback  r.called        r.get_result    r.raised
    r.callbacks     r.client        r.r             r.result_id

    In [38]: r.get_result(block=True)

    Out[38]: 
    <Results List>
    [0] In [69]: time.sleep(10)
    [1] In [40]: time.sleep(10)

Task interface
==============

The task client uses a FIFO queue to load balance tasks amongst the engines.
Because of this, it does not explicitly expose the engine ids in its
interface.

Task client
-----------

:class:`IPython.kernel.client.TaskClient(furl_or_file='')`
    Create a task client for a FURL or file containing a FURL.

:class:`IPython.kernel.client.map(func, *sequences)`
    A parallel and load balanced version of map.

:attr:`TaskClient.run(task, block=False)`
    Run a task on the cluster and return its task id.

:attr:`TaskClient.get_task_result(taskid, block=False)`
    Get a task's result by task id.

:attr:`TaskClient.barrier(taskids)`
    Wait for a set of tasks to complete.

Task objects
------------

:class:`IPython.kernel.client.MapTask(func, args=None, kwargs=None)`
    Create a task by a function and its arguments. The task result
    is simply ``func(*args, **kwargs)``.

:class:`IPython.kernel.client.StringTask(code, pull=None, push=None)`
    Create a task using lines of python code and data to push as
    input and pull as results.

Examples
--------

The simplest way of using the :class:`TaskClient` is through the :meth:`map`
method:

.. sourcecode:: ipython

    In [1]: tc = client.TaskClient()

    In [2]: tc.map(lambda x:x**10, range(16))

    Out[2]: 
    [0,
     1,
     1024,
     59049,
     1048576,
     9765625,
     60466176,
     282475249,
     1073741824,
     3486784401L,
     10000000000L,
     25937424601L,
     61917364224L,
     137858491849L,
     289254654976L,
     576650390625L]

The only difference between :meth:`MultiEngineClient.map` and
:meth:`TaskClient.map` is that the former does not do any load balancing.
However, the load balancing of the :class:`TaskClient` does add a small amount
of overhead, so :meth:`MultiEngineClient.map` may perform better for smaller
tasks.

You can also create a :class:`MapTask` by hand and run it using :meth:`TaskClient.run`:

.. sourcecode:: ipython

    In [14]: def f(x):
       ....:     return x**2
       ....: 

    In [15]: t = client.MapTask(f, args=(10,))

    In [16]: tc.run(t)

    Out[16]: 4032  # The task id


    In [17]: tc.barrier(4032)  # Wait for this task to complete

    In [18]: tc.get_task_result(4032)

    Out[18]: 100

A :class:`StringTask` allow the task to be specified as a string of Python 
code instead of a function. See its docstring for details.

When to use IPython
===================

* You want to scale from multicore CPUs to cluster and supercomputers.
* You want to run on systems with batch systems.
* You want a high level API, but still want MPI integration.
* You don't mind the extra dependencies of IPython.
* You want everything to be usable interactively.
* You have the time and effort to learn a complex API.
* All your objects are pickleable.

Examples
========

Let's see how to parallelize our examples using IPython.

Prime numbers
-------------

Exercise:

* Try to parallelize the :func:`prime1.sum_primes` function using IPython's
  :class:`MultiEngineClient` class.
* You can write this code interactively or in a standalone script.
* Make sure you start :command:`ipcluster` in the :file:`code` subdirectory
  so the engines can import the :mod:`prime1` module.
* Calculate the parallel speedup you got using IPython (conpare to our
  earlier serial runs.)
* Is there any way so improve the performance.  Hint: you can fake load
  balance in this case.

Solution:

.. literalinclude:: /code/prime1_mec.py
   :language: python
   :linenos:

Here is what I get when running this example:

.. code-block:: bash

    $ python prime1_mec.py
    Serial sum_primes time:  37.5719628334
    Parallel sum_primes time:  21.3599839211
    Speedup of sum_primes on 2 cores: 1.758988

Exercise:

* Repeat the same steps for the faster :func:`prime1.sum_primes` function.
* Because this function is written in C++, it cannot be pickled, so you can't
  call :meth:`MultiEngineClient.map` as before. Remember, the
  :meth:`MultiEngineClient.execute` method can take code as strings.
* Also remember that you will need to use :mod:`pyximport` when importing
  :mod:`prime2`.

Solution:

.. literalinclude:: /code/prime2_mec.py
   :language: python
   :linenos:

Here is what I get when running this example:

.. code-block:: bash

   $ python prime2_mec.py
   Serial sum_primes time:  1.67170882225
   Parallel sum_primes time:  0.98609495163
   Speedup of sum_primes on 2 cores: 1.695282

Random matrices
---------------
