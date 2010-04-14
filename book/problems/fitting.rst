.. _fitting:

Simple fitting
==============

Generate some data of the form

.. math::

   y(x) = a \exp(\alpha x) + k

for the following choice of constants: $a=2, \alpha=-0.75, k=0.1$, in the range
$x \in [0,4]$. Add zero-mean gaussian noise with amplitude $0.1$ to this signal
to create a noisy version of the signal.

Then, compare the results of fitting the noisy data using a least-squares fit
to the analytical form, as well as splines (from ``scipy.interpolate``) and
polynomial fits (from ``numpy``) of orders 0, 1 and 2.

.. only:: instructor

   Solution
   --------

   .. literalinclude:: examples/fitting.py

   The least-squares and polynomials fits should look like this:
   
   .. image:: fig/fitting_ls.png
      :width: 4in

   .. image:: fig/fitting_poly.png
      :width: 4in
