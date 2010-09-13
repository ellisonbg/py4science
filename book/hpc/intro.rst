.. _intro:

============
Introduction
============

Parallel computing defined
==========================

This document is a tutorial about high performance computing, or "HPC", in the
Python programming language. The focus is on maximizing performance through 
parallel computing. What do we mean by parallel computing?

Concurrent Computing
    A programming model that allows multiple tasks to be *seemingly* executed
    at the same time. Depending on the implementation, the tasks may or may
    not actually be executed at the same time. Examples: Erlang, Go,
    Stackless, Scala, Clojure, threads, coroutines, Twisted. Concurrency is
    somewhat trendy right now.

Distributed Computing
    A computation that is executed on multiple hosts that communicate over a
    network. The goal might be something other than speeding up the 
    computation. Example: the Internet.

Parallel Computing
    A computation that is executed on multiple cores/processors/hosts with
    the primary goal of speeding up the computation. Hardware used in a 
    parallel computation is called "parallel hardware" and includes 
    multicore CPUs, clusters, supercomputers and GPUs. Examples: traditional
    MPI codes on a supercomputer, Google's Map/Reduce, Seti@Home, etc.

Under these definitions:

* All parallel computations are concurrent. Not all concurrent computations
  are parallel.
* Some parallel computations are distributed.

.. warning::
    These are my definitions and they differ from those of other people (see
    their Wikipedia definitions for more discussion.) These days, many people
    use the terms  "concurrent", "parallel" and "distributed" interchangeably. 
    Don't let the definitions of the terms distract you from the goal of this 
    tutorial: to make computations go faster using parallel hardware.

This tutorial is about *parallel computing*.

.. note::
    For many people, "parallel computing" has a lot of connotations: MPI,
    compiled languages, cluster or supercomputers (head node, batch
    system and shared file system), input files, output files, etc. This
    tutorial provides a very different take on parallel computing, one that
    emphasizes interactive work and ease of use.

Goals of this tutorial
======================

This tutorial assumes that:

* You have a program that you want to run and you have its source code.
* You have parallel hardware (multicore CPU, cluster or supercomputer) at 
  your disposal.
* You want to "parallelize" your program to run on and take advantage of 
  the parallel hardware.

If you are in this situation, there are two main reasons reasons you might
want to "parallelize" your program:

1. Speed up the execution time of your program. Your program takes an hour
   to run, but you would like it to take 1 second.
2. Run a "bigger" version of your program that requires more resources 
   (memory, disk space, etc.). Your program uses 10,000 by 10,000 matrices
   and you want to increase that to 100,000 by 100,000. In this case you
   may or may not care if the execution time decreases.

There are other possible motivations for parallelizing a program, but these
are the ones that I will focus on in this tutorial.

Idealism
========

If you want to make your program bigger and faster, you are probably using
your program to solve some problem. You want to focus on solving that problem,
not on the many intricacies and details of parallel computing. You want a
magic library, switch, knob, button, or pill that will simply make your
program faster.

In 2010, this doesn't exist. Not even close.

I feel your pain.

Realism
=======

Speeding up a program through parallelism is difficult. Furthermore, there
is no guarantee that your efforts will be successful. After much hard work,
you may end up with parallel version of your program that not much faster
(or even slower!) than the serial version. In fact, as Amdahl's law
shows, in some cases, you are guaranteed to achieve minimal success.

Even if you are successful in speeding up your program, you will likely
have to:

* Think about your program, problem or algorithm in different ways.
* Understand why exactly your program is slower than you would like.
* Understand some of the details of computer architecture.
* Rewrite your code in a way that better expresses parallelism.

The following steps provide a realistic approach to parallelism:

1. Understand bottlenecks in your program.
2. Optimize the serial version of the program.
3. Pick appropriate parallel hardware and software tools for parallelizing
   your program.
4. Parallelize your program and algorithm.

The rest of this tutorial will cover these steps in detail. This will include
a description of a number of Python based software tools you can use to 
parallelize your program. The following software tools will be covered:

* :ref:`Threading <threading>`
* :ref:`Multiprocessing <multiprocessing>`
* :ref:`IPython <ipython>`
* :ref:`PiCloud <picloud>`
* :ref:`Mpi4Py <mpi4py>`
* :ref:`PyZMQ <pyzmq_chapter>`

The dependencies for the current version of the tutorial are:

* Python 2.6
* IPython with its parallel computing dependencies (zope.interface, Twisted,
  Foolscap).
* PiCloud

All of these dependencies come with EPD versions 6.1 and 6.2.
