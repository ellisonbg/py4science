.. _glass_patterns:

Glass Moiré Patterns
--------------------

When a random dot pattern is scaled, rotated, and superimposed over the
original dots, interesting visual patterns known as Glass Patterns emerge [#]_.
In this exercise, we generate random dot fields using numpy's uniform
distribution function, and apply transformations to the random dot field using
a scale $\mathbf{S}$ and rotation $\mathbf{R}$ matrix $\mathbf{X_2} =
\mathbf{S} \mathbf{R} \mathbf{X_1}$.

If the scale and rotation factors are small, the transformation is analogous to
a single step in the numerical solution of a 2D ODE, and the plot of both
$\mathbf{X_1}$ and $\mathbf{X_2}$ will reveal the structure of the vector field
flow around the fixed point (the invariant under the transformation); see for
example the *stable focus*, aka *spiral*, in the figure below.

The eigenvalues of the tranformation matrix $\mathbf{M} = \mathbf{S}\mathbf{R}$
determine the type of fixed point: *center*, *stable focus*, *saddle node*,
etc...  For example, if the two eigenvalues are real but differing in signs,
the fixed point is a *saddle node*.  If the real parts of both eigenvalues are
negative and the eigenvalues are complex, the fixed point is a *stable focus*.
The complex part of the eigenvalue determines whether there is any rotation in
the matrix transformation, so another way to look at this is to break out the
scaling and rotation components of the transformation $\mathbf{M}$.  If there
is a rotation component, then the fixed point will be a *center* or a *focus*.
If the scaling components are both one, the rotation will be a *center*, if
they are both less than one (contraction), it will be a *stable focus*.
Likewise, if there is no rotation component, the fixed point will be a *node*,
and the scaling components will determine the type of node.  If both are less
than one, we have a *stable node*, if one is greater than one and the other
less than one, we have a *saddle node*.

.. plot:: examples/glass_dots1.py
   :include-source:
   :width: 4in

   Glass pattern showing a stable focus

.. [#] L. Glass. 'Moiré effect from random dots' Nature 223, 578580 (1969).
