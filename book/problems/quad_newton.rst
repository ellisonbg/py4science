.. _quad_newton:

Newton's method
---------------

**Illustrates:** functions as first class objects, use of the scipy libraries.

Consider the problem of solving for $t$ in

.. math::
  \int_{o}^{t}f(s)ds=u

where $f(s)$ is a monotonically increasing function of $s$ and $u>0$.


Think about how to cast this problem as a root-finding question and use
Newton's method to solve it.  The Scipy library includes an optimization
package that contains a Newton-Raphson solver called ``scipy.optimize.newton.``
This solver can optionally take a known derivative for the function whose roots
are being sought.

For this exercise, implement the solution for the test function

.. math::

   f(t)=t\sin^{2}(t),

using

.. math::

   u=\frac{1}{4}.


.. only:: instructor

   Solution
   ~~~~~~~~

   This problem can be simply solved if seen as a root finding question. Let

   .. math::
      g(t)=\int_{o}^{t}f(s)ds-u,

   then we just need to find the root for $g(t),$ which is guaranteed to be
   unique given the conditions above. In this case the derivative can be
   trivially computed in exact form, and we can then pass them to the
   Newton-Raphson solver.

   The following code implements this solution:

   .. literalinclude:: examples/quad_newton.py
