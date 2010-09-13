.. _mpi4py:

==============
MPI for Python
==============

The previous tools have all focused on executing Python code in a thread
or process. Some times, the code running in those threads or processes
needs to send messages to each other. This is called message passing and
the next two chapters cover two tools for message passing in Python:

In this chapter we describe the Message Passing Interface (`MPI
<http://www.mcs.anl.gov/research/projects/mpi/>`_) and a high quality Python
wrapper to it, called `MPI For Python <http://code.google.com/p/mpi4py/>`_,
or :mod:`mpi4py`.

MPI
===

* MPI is a C and Fortran library API specification for message passing.
* It is the traditional workhorse in parallel computing.
* It is very fast and can use high speed interconnects like Infiniband.
* There are many MPI implementations (MPICH, OpenMPI, etc.)
* MPI is very inflexible, has a large and complex API and is difficult to
  program to and use.

mpi4py
======

* mpi4py is a Cython based wrapper for MPI.
* Runs on every platform, every MPI implementation, every Python version.
* Extremely well tested.
* For large messages, nearly matches the performance of raw C MPI.
* For small messages, a small amount of Python overhead shows up.
* Handles Python objects, NumPy arrays.
* One of the highest quality open source libraries around.
* mpi4py is integrated into IPython's :command:`ipcluster` command and
  :class:`MultiEngineClient` interface.  Allows the IPython engines to 
  execute code that uses :mod:`mpi4py`.