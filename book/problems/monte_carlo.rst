.. F Perez

.. _monte_carlo:

Monte Carlo integration
=======================

Compute $\pi$ via Monte Carlo integration.  To do this, think of a function
whose integral is related to $\pi$, and then compute this integral via
MonteCarlo integration (even if it's a simple integral you could do
analytically, since the point is to practice MC methods).

.. only:: instructor

   Solution
   --------

   .. literalinclude:: examples/montecarlo_pi.py

   This code includes a weave-enabled version of the computation, to illustrate
   how certain cases can be easily sped up with very little effort.
   