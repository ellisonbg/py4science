.. _serial_examples:

===============
Serial examples
===============

This tutorial is based on a series of examples. For each of these examples, we
will go through a sequence of first speeding up the serial version and then
parallelizing it using a variety of tools. This section introduces the serial
versions of the examples.

Prime numbers
=============

We begin with a simple module that can find prime numbers. This code is
contained in the file :file:`code/prime1.py`. First, the :func:`isprime`
function tests if its argument is prime or not:

.. literalinclude:: /code/prime1.py
   :language: python
   :pyobject: isprime
   :linenos:

The :func:`sum_primes` function makes repeated calls to :func:`isprime` to sum
up the primes less than ``n``:

.. literalinclude:: /code/prime1.py
   :language: python
   :pyobject: sum_primes
   :linenos:

Exercise:

* Startup IPython by typing ``ipython``.
* Import :mod:`prime1` and try calling the functions :func:`isprime` and
  :func:`sum_primes`.
* Time their execution for different arguments using ``%timeit``.

Solution:

.. sourcecode:: ipython

    In [27]: import prime1

    In [28]: [prime1.isprime(n) for n in range(20)]

    Out[28]: [0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1]


    In [29]: prime1.sum_primes(100)

    Out[29]: 1060


    In [30]: %timeit map(prime1.isprime, xrange(20000))
    10 loops, best of 3: 86.8 ms per loop

    In [31]: %timeit map(prime1.sum_primes, xrange(1000,2000))
    1 loops, best of 3: 4.02 s per loop

We see that while :func:`isprime` is quite fast, :func:`sum_primes` takes a
while and might be worth parallelizing.

Random matrices
===============
