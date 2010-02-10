.. _bessel:

Recursion relations and Bessel functions
========================================

**Illustrates**: Special functions library, array manipulations
to check recursion relation.

In this exercise, you will verify a few simple relations involving the Bessel
functions of the first kind.  The important relations to keep in mind are the
asymptotic form of $J_n(x)$ for $x \gg n^2$:

.. math::

   J_n(x) \approx \sqrt{\frac{2}{\pi x}}
                  \cos \left( x- \frac{n\pi}{2} - \frac{\pi}{4} \right),

the asymptotic form of $J_n(x)$ for $x \ll \sqrt{n}$

.. math::
   
   J_n(x) \approx \frac{1}{\Gamma(n+1)} \left( \frac{x}{2} \right) ^n, 
   
and the recursion relation

.. math::
   :label: bessel_rec

   J_{n+1}(x) = \frac{2n}{x} J_n(x)-J_{n-1}(x).

The :mod:`scipy.special` module contains functions :func:`j0`, :func:`j1` and
:func:`jn` to compute Bessel functions of order 0, 1 and arbitrary $n$, as well
as many other useful special function-related routines.

For this problem, build three separate figures showing:

#. $J_0(x)$, $J_1(x)$ and $J_5(x)$ for $x$ in the interval $[0, 35]$, as well
   as their asymptotic forms.  Use thicker dashed lines for the asymptotic
   forms, and only plot them in their region of validity.

#. A similar plot, for $J_4(x)$, $J_5(x)$ and $J_6(x)$ for $x$ in the interval
   $[0, 3]$ (be careful to use the proper asymptotic form).

#. The error in the recursion relation :eq:`bessel_rec` for $J_5$ over the same
   interval. These errors should be displayed using a logarithmic vertical
   axis.


Try to get your figures to look reasonably close to those below.

.. figure:: fig/bessel_functions.pdf
   :width: 5in

   A few Bessel functions and their asymptotic forms valid for $x \gg n^2$.


.. figure:: fig/bessel_functions_small_x.pdf
   :width: 5in

   A few Bessel functions and their asymptotic forms valid for $x \ll \sqrt{n}$.


.. figure:: fig/bessel_error.pdf
   :width: 5in

   Numerical error in manually implementing the Bessel recursion for $J_5$ vs
   scipy's implementation.


Hints
-----

* Passing a ``label`` keyword to :func:`plot` calls lets you label each plot,
  these plots are then used by :func:`plt.legend` which puts legend boxes.

* :func:`plt.legend` takes a ``loc`` parameter for location.

* look at :func:`plt.semilogy` for the logarithmic error plots.


.. only:: instructor

   Solution
   ~~~~~~~~

   .. literalinclude:: examples/bessel.py

   Bessel module - API documentation
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   .. automodule:: examples.bessel
      :members:
