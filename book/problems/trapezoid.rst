.. _trapezoid:

Trapezoidal rule
================

**Illustrates**: basic array slicing, functions as first class objects.

In this exercise, you are tasked with implementing the simple trapezoid rule
formula for numerical integration. If we want to compute the definite integral

.. math::
    :label: trapzf

     \int_{a}^{b}f(x)dx

we can partition the integration interval $[a,b]$ into smaller subintervals,
and approximate the area under the curve for each subinterval by the area of
the trapezoid created by linearly interpolating between the two function values
at each end of the subinterval. This is graphically illustrated in the Figure
below, where the blue line represents the function $f(x)$ and the red line
represents the successive linear segments.  The area under $f(x)$ (the value of
the definite integral) can thus be approximated as the sum of the areas of all
these trapezoids. If we denote by $x_{i}$ ($i=0,\ldots,n,$ with $x_{0}=a$ and
$x_{n}=b$) the abscissas where the function is sampled, then

.. math::

   \int_{a}^{b}f(x)dx\approx\frac{1}{2}\sum_{i=1}^{n}\left(x_{i}-x_{i-1}\right)\left(f(x_{i})+f(x_{i-1})\right).

The common case of using equally spaced abscissas with spacing $h=(b-a)/n$
reads simply

.. math::
   :label: trapzf2
   
   \int_{a}^{b}f(x)dx\approx\frac{h}{2}\sum_{i=1}^{n}\left(f(x_{i})+f(x_{i-1})\right).

One frequently receives the function values already precomputed, $y_{i}=f(x_{i}),$
so equation :eq:`trapzf` becomes

.. math::
   :label: trapz

   \int_{a}^{b}f(x)dx\approx\frac{1}{2}\sum_{i=1}^{n}\left(x_{i}-x_{i-1}\right)\left(y_{i}+y_{i-1}\right).


.. figure:: fig/trapezoid_rule.png
   :width: 4in

   Illustration of the composite trapezoidal rule with a non-uniform grid
   (Image credit: Wikipedia).
   
In this exercise, you'll need to write two functions, ``trapz`` and
``trapzf``. ``trapz`` applies the trapezoid formula to pre-computed values,
implementing equation :eq:`trapz`, while ``trapzf`` takes a function $f$ as
input, as well as the total number of samples to evaluate, and computes
eq. :eq:`trapzf2`.

Test it and show that it produces correct values for some simple integrals you
can compute analytically.


.. only:: instructor

   Solution
   --------

   .. literalinclude:: examples/trapezoid.py

   With this simple code we can see directly how to generate a similar figure
   using matplotlib:

   .. literalinclude:: examples/trapezoid_demo.py

   produces:

   .. figure:: fig/trapezoid_demo.pdf
