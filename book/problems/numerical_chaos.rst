Numerical chaos in the logistic map and floating point error
============================================================

One of the most classic examples of chaotic behavior in non-linear systems is
the iteration of the logistic map

.. math::
   :label: logistic-map

   x_{n+1} = f(x_n) = r x_n (1-x_n)

which for $x \in (0,1)$ and $r \in (0,4)$ can produce very surprising
behavior.  We'll revisit this system later with some more sophisticated tools,
but for now we simply want use it to illustrate numerical roundoff error.

Computers, when performing almost any floating point operation, must by
necessity throw away information from the digits that can't be stored at any
finite precision.  This has a simple implication that is nonetheless often
ovelooked: algebraically equivalent forms of the same expression aren't
necessarily always numerically equivalent.  A simple illustration shows the
problem very easily:

.. ipython::

   In [19]: x = 1

   In [20]: y = 1e-18

   In [21]: x+y-x
   Out[21]: 0.0

   In [22]: x-x+y
   Out[22]: 1.0000000000000001e-18


For this exercise, try to find three different ways to express $f(x)$ in
:eq:`logistic-map` and compute the evolution of the same initial condition
after a few hundred iterations.  For this problem, it will be extremely useful
to look at your results graphically; simply build lists of numbers and call
matplotlib's ``plot`` function to look at how each trace evolves.

The following snippet can be used as a starting point, and it includes some
hints on what values of $r$ to look at:

::

   """Illustrating error propagation by iterating the logistic map.

   f(x) = r*x*(1-x)

   Write the above function in three algebraically equivalent forms, and study
   their behavior under iteration.  See for what values of r all forms evolve
   identically and for which ones they don't.
   """

   import matplotlib.pyplot as plt

   # Interesting values to try for r:
   # [1.9, 2.9, 3.1, 3.5, 3.9]
   x0 = 0.6  # any number in [0,1] will do here
   numpoints = 100


.. note::

   This was inspired by this `very nice presentation`_ about Python's
   :mod:`turtle` module, which includes some great numerical examples.

.. _very nice presentation:
   http://us.pycon.org/2009/conference/schedule/event/65/


.. only:: instructor

   Solution
   --------

   .. literalinclude:: examples/numerical_chaos.py

