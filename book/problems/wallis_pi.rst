Wallis' formula
===============

Wallis' formula is a slowly converging infinite product that approximates pi as

.. math::
  :label: wallis-pi
  
   \pi = \lim_{n \rightarrow \infty} 2 \prod_{i=1}^{n}\frac{4i^2}{4i^2-1}.

While this isn't a particularly good way of computing $\pi$ from a numerical
standpoint, it provides for an excellent illustration of how Python's integers
are more flexible and powerful than those typically found by default in
compiled languages like C and Fortran.  The problem is that for
:eq:`wallis-pi` to be even remotely accurate, one must evaluate it for fairly
large values of $n$, where both the numerator and the denominator will easily
overflow the limits of 64-bit integers.  It is only after taking the ratio of
these two huge numbers that the value is small (close to $\pi$).

Fortunately for us, Python integers automatically allocate as many digits as
necessary (within the limits of physically available memory) to hold their
result.  So while impementing :eq:`wallis-pi` in C or Fortran (without auxilary
libraries like GMP_) would be fairly tricky, in Python it's very
straightforward.

.. _gmp: http://gmplib.org

For this exercise, write a program that implements the above formula.  Note
that Python's :mod:`math` module already contains $\pi$ in double precision, so
you can use this value to compare your results:

.. ipython::

   In [1]: import math

   In [2]: math.pi
   Out[2]: 3.1415926535897931

   
Keep in mind that Python by default divides integers by truncating:

.. ipython::

   In [3]: 3/4
   Out[3]: 0

this will change in the future, and the new behavior can be activated even
today:

.. ipython::

   In [4]: from __future__ import division

   In [5]: 3/4
   Out[5]: 0.75

so you should put this ``from __future__`` statement as the first non-comment,
non-docstring statement in your program, to ensure that you can get the
division to produce a floating point number in the end.

.. only:: instructor

   Solution
   --------

   A solution to this problem is here:
     
   .. literalinclude:: examples/wallis_pi.py

   Note that in the computation of $\pi$, you must store the numerator and the
   denominator *separately* as integers, to take advantage of Python's
   arbitrary length integers, and only make the floating point division at the
   very end.
   