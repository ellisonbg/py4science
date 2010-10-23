Glass Moiré Patterns
====================

.. ipython::
   :suppress:

   # set up ipython for plotting in pylab
   In [3]: from pylab import *

   In [4]: plt.close('all')

   In [5]: ion()

   In [6]: bookmark ipy_start

When Leon Glass was a post-doc in the late sixties studying iterative
systems such as the Mandelbrot set and the logistic map, he conducted
an unusual experiment using a new-fangled copy machine.  He took a
blank piece of paper, fed it into the machine, and got a blank copy
out.  He took the copy and copied it, a copy of the copy, and got
another (mostly) blank copy out.  He repeated this for a large number
of iterations and saw that random dots began to appear, either from
imperfections in the copy process, or specks of dust that grew
progressively larger and darker with repeated copies.  His intention
was to study the statistical distribution of these random dots, and
gave a talk with his preliminary results.

In those days, before the advent of Power Point, it was common to give
an "overhead talk" using transparencies, and typically the presenter
would have a paper copy of the original and a transparent copy of the
overhead atop the paper copy, to help keep them organized.  The
transparencies slide around on top of their paper copy, with small or
large translations and rotations from the original, and additionally
the copy process from the paper to the transparency can introduce
minor scaling distortions in the x and y directions.  As Leon was
organizing his talk, he noticed that the superposition of the random
dots in the transparency over his original random dots created
interesting visual effects when the copied dots were slightly rotated
or scaled with respect to the original.

He gave up on the study of the statistical distribution of these dot
patterns, and focused his attention instead on these interesting
visual patterns he was seeing in the random dots.  The result was a
Nature paper  "Moiré effect from random dots" (cite Glass1969)

Here we'll use numpy's 2D arrays, random numbers and linear algebra
functions to simulate the effect that Glass observed.  We'll see that
these Glass dot patterns and transformations have a close connection
to flow fields of 2D linear ordinary differential equations around
fixed points. 

First, we'll create some random (x,y) coordinates for our random dot
pattern, and then use scaling and rotation matrices to transform them,
simulating the dots on the transparent overhead which were slightly
scaled and rotated with respect to the original.  In the code below,
we create two rows of data drawn from the uniform distribution over
[-0.5, 0.5], the first row are the random x coordinates and the second
row are the y coordinates.  The arguments to ``plot`` say "use red
circles and a marker size of 2".

.. ipython::

    In [101]: X1 = np.random.rand(2,2000)-0.5

    @savefig glass_dots_paper_view.png 
    In [102]: plt.plot(X1[0], X1[1], 'ro', markersize=2)

Next we want to transform the data in ``X1`` using a minor scaling
:math:`\mathbf{S}` and rotation :math:`\mathbf{R}` matrix; in matrix notation we
have :math:`\mathbf{R}` matrix :math:`\mathbf{X_2} = \mathbf{S} \mathbf{R}
\mathbf{X_1}`.

.. ipython::

   # the scalex, scaley, and rotation parameters
   In [112]: sx, sy, theta = 0.975, 0.975, 2.5*np.pi/180.

   # the scaling matrix
   In [113]: S = np.array([[sx, 0],
      .....:               [0, sy]])

   # the rotation matrix
   In [114]: R = np.array([[np.cos(theta),  -np.sin(theta)],
      .....:               [np.sin(theta), np.cos(theta)] ])

To do matrix multiplication in numpy, use ``np.dot``; although there
is a matrix class in which the multiplication operator ``*`` is
overloaded to do a matrix multiply rather than an element-wise
multiply (which is what happens for plain numpy array), we don't
recommend using it for most cases, as ``np.dot`` is easy enough to
type and you retain the advantage that the 2D array is fully
compatible with any python code expecting numpy arrays (eg
matplotlib).  We'll take the matrix product of ``R`` and ``S`` to
create a single matrix transformation ``M``.

.. ipython::

  # rotate then stretch
  In [119]: M = np.dot(R, S)

  # transform X1 by M
  In [120]: X2 = np.dot(M, X1)

  In [140]: plt.plot(X2[0], X2[1], 'go', markersize=2)

  @savefig glass_dots_superimposed.png 
  In [141]: title('X1 and X2 superimposed')


If the scale and rotation factors are small, the transformation is
analogous to a single step in the numerical solution of a 2D ODE, and
the plot of both :math:`\mathbf{X_1}` and :math:`\mathbf{X_2}` reveals the
structure of the vector field flow around the fixed point (the
invariant under the transformation).

The eigenvalues of the transformation matrix :math:`\mathbf{M} =
\mathbf{S}\mathbf{R}` determine the type of fix point: *center*,
*stable focus*, *saddle node*, etc....  The complex part of the
eigenvalue determines whether there is any rotation in the matrix
transformation, so another way to look at this is to break out the
scaling and rotation components of the transformation :math:`\mathbf{M}`.
If there is a rotation component, then the fixed point will be
analogous to a *center* or a *focus*.  If the scaling components are
both one, the rotation will be around a *center*, if they are both
less than one (contraction), it will be around a *stable focus*.
Likewise, if there is no rotation component, the fixed point will be a
*node*, and the scaling components will determine the type of node.
If both are less than one, we have a *stable node*, if one is greater
than one and the other less than one, we have a *saddle node*.

We can determine the eigenvalues using the ``np.linalg.eig`` function,
which returns the eigenvalues of the transformation as the first
argument, and the eigenvectors as the second.

.. ipython::

   In [145]: w, v = np.linalg.eig(M)

   In [146]: w
   Out[146]: array([ 0.98905774+0.04318319j,  0.98905774-0.04318319j])

   In [147]: abs(w)
   Out[147]: array([ 0.99,  0.99])


In our example above, both ``sx`` and ``sy`` were less than 1, so the
transformation is contracting and we have complex eigenvalues
indicating a rotation component, so the fixed point is analogous to a
*stable focus*.  

**Exercise**: try various combinations of ``sx``, ``sy``, and `theta``
to simulate the different kinds of flow fields around a fixed point.


Interactively exploring Glass dot patterns
===========================================

We can use matplotlib's event handling to track the mouse movements to
support interactively changing the scale in the x and y directions, as
well as the rotation.  When you run the example below, pressing the
left mouse button while dragging the mouse in the x direction changes
the x scaling variable ``sx``, and dragging it in the y direction
changes it in the ``sy`` direction.  Pressing the right mouse button
and dragging the mouse will update the rotation variable.

This example requires a brief introduction to matplotlib event
handling -- for a more detailed overview see the official matplotlib
documentation `event handling tutorial
<http://matplotlib.sf.net/users/event_handling.html>`_.

To connect to a matplotlib event, eg a button press event, a key press
event, or a mouse motion event, use the ``mpl_connect`` method of the
matplotlib canvas.  Eg, we can print the display coordinates
(``event.x`` and ``event.y) and data coordinates (``event.xdata`` and
``event.ydata``) on every mouse press event by defining the following
callbaqck and registering it with the matplotlib canvas.

.. sourcecode:: ipython

   In [215]: def report(event):
      .....:     if not event.inaxes: return
      .....:     print 'display: x=%d, y=%d'%(event.x, event.y)
      .....:     print 'data: x=%.2f, y=%.2f'%(event.xdata, event.ydata)
      .....:     
      .....:     


   In [216]: fig, ax = plt.subplots(1)

   In [217]: ax.plot(np.random.rand(20))
   Out[217]: [<matplotlib.lines.Line2D object at 0xb8ca4ec>]

   In [218]: cid = fig.canvas.mpl_connect('button_press_event', report)

Then, whenever you click over the subplot, you will see output like::

  display: x=217, y=148
  data: x=5.52, y=0.26

Whenever you are finished with the event and want to disconnect the callback, use the connection id ``cid`` returned by ``mpl_connect`` to disconnect


.. sourcecode:: python

  In [225]: fig.canvas.mpl_disconnect(cid)

In the example below, we connect to the 'button_press_event',
'button_release_event', and 'motion_notify_event'.

.. sourcecode:: python

   import numpy as np

   class Transformer:
       def __init__(self, axes):

	   # initial scaling and rotation
	   self.sx, self.sy, self.theta = 1., 1., 0.
	   self.dx = 0.001     # scaling increment on mouse move
	   self.dtheta = 0.01  # rotation increment on mouse move
	   self.axes = axes
	   self.canvas = axes.figure.canvas

	   # set up the matplotlib event handling callbacks
	   self.canvas.mpl_connect('button_press_event', self.press)
	   self.canvas.mpl_connect('button_release_event', self.release)
	   self.canvas.mpl_connect('motion_notify_event', self.move)

	   # the initial X data -- the "paper copy"
	   X1 = self.X1 = np.random.rand(2,2000)-0.5

	   # the matplotlib Line2D objects; we'll update line2 on mouse
	   # moves
	   self.line1, self.line2 = ax.plot(X1[0], X1[1], 'go', 
					    X1[0], X1[1], 'ro', markersize=2)
	   # the x and y locations when the mouse button is pressed or
	   # mouse is moved
	   self.xlast, self.ylast = None, None

	   self.title = ax.set_title('drag the left or right mouse to stretch and rotate', fontweight='bold')

       def press(self, event):
	   'mouse press, save the x and y locations'
	   self.xlast, self.ylast = event.xdata, event.ydata

       def release(self, event):
	   'release the mouse'
	   self.xlast, self.ylast = None, None
	   self.draw()

       def draw(self):
	   sx, sy, theta = self.sx, self.sy, self.theta
	   # the new rotate then scale matrix
	   M =  np.array([[sx*np.cos(theta), -sx*np.sin(theta)],
			  [sy*np.sin(theta), sy*np.cos(theta)]])

	   X2 = np.dot(M, self.X1)
	   # update the data in line2, then redraw.  line1 is unchanged
	   self.line2.set_data(X2[0], X2[1])
	   self.canvas.draw()

       def move(self, event):

	   if not event.inaxes: return    # not over axes
	   if self.xlast is None: return  # no initial data
	   if not event.button: return    # no button press

	   # compute the distance moved since last mouse press
	   dx = event.xdata - self.xlast
	   dy = event.ydata - self.ylast

	   if event.button==1:    # update the scale
	       self.theta += dx
	   elif event.button==3:  # update the rotation
	       self.sx += dx
	       self.sy += dy

	   self.title.set_text('sx=%1.2f, sy=%1.2f, theta=%1.2f'%(self.sx, self.sy, self.theta))
	   self.draw()
	   # update the last x and y locations
	   self.xlast, self.ylast = event.xdata, event.ydata


   if __name__=='__main__':
       import matplotlib.pyplot as plt
       fig = plt.figure()
       ax = fig.add_subplot(111)
       t = Transformer(ax)
       plt.show()


.. [#] L. Glass. 'Moiré effect from random dots' Nature 223, 578580 (1969).
