.. _random_walks:

Random Walks
--------------------

The `random walk <http://en.wikipedia.org/wiki/Random_walk>`_, in
which the next position is a random step from the current position, is
a fundamental process in the study of phenomena as diverse as
molecular dynamics, animal foraging, and financial time series.  Each
step is drawn from a statistical distribution; in a simple random walk
the steps are drawn from [-1,1] and in the Wiener process which models
Brownian motion, the steps are drawn from a normal, or Gaussian,
distribution.

.. ipython::
   :suppress:

   # set up ipython for plotting in pylab
   In [4]: from pylab import *

   In [5]: ion()

   In [6]: bookmark ipy_start


It is simple to implement a random walk with steps from a normal
distribution using a ``for`` loop in Python.

.. plot::
   :include-source:

   import numpy as np
   import matplotlib.pyplot as plt

   x = 0.          # the initial position
   nsteps = 100    # the number of steps
   position = np.zeros(nsteps)

   for i in range(nsteps):
       x += np.random.normal()
       position[i] = x	

   plt.plot(position)

But Python is slow with looks, and typically we want to compute a
population of random walkers over multiple steps.

.. plot::
   :include-source:

   import numpy as np
   import matplotlib.pyplot as plt

   nsteps = 100    # the number of steps
   nwalkers = 10   # the number of walkers
   position = np.zeros((nsteps, nwalkers))

   # use a local name for normal 
   randfunc = np.random.normal
   for i in range(nwalkers):
       x = 0.          # the initial position
       for j in range(nsteps):
           x += randfunc()
           position[j,i] = x	

   plt.plot(position)

Since Python is an interpreted language, this code will be slow.  For
each pass though the inner loop, Python has to do name lookups to
determine the types of ``x``, ``position``, ``i``, etc...  It also has
to figure out what the operators ``()`` and ``[i,j]`` and ``+=`` mean
for those types.  And it doesn't remember: it has to do these lookups
on *every* pass through the loop.  We used a common idiom to make the
code slightly faster, defining a local variable named ``randfunc``
outside the loops to avoid having to do attribute lookup on the numpy
random module in the inner loop with ``np.random.normal``, but
nonetheless this code will be *very* slow because of the nested loop.

Fortunately, we can use numpy to define our random walkers succinctly
and efficiently.  For a single random walker we can generate an array
of normally distributed random deviates by passing the *size* keyword
argument to the ``normal`` method.

.. ipython::

   In [85]: steps = np.random.normal(size=100)

   In [86]: position = steps.cumsum()

   In [87]: position.shape
   Out[87]: (100,)

Similarly, we can make a 2D array of steps by passing in a length 2
tuple as the *size* argument; we use capitalized variable names below
to denote that the ``Steps`` and ``Position`` variables are 2D arrays.
The ``cumsum`` numpy method call below cumulatively sums the steps
along ``axis=0`` which is the first axis, the number of steps.

.. ipython::

   In [116]: Steps = np.random.normal(size=(100, 10))

   In [117]: Position = Steps.cumsum(axis=0)

   In [118]: Position.shape
   Out[118]: (100, 10)

   @verbatim
   In [119]: plot(Position);


Here all the hard work is done by numpy at the C level and will be
extremely fast.  

We can easily draw our steps from other distributions.  For example,
to draw random steps from 1 or -1, the simple random walk, we can use
the numpy ``where`` function, which takes a logical mask as the first
argument, the value to take where the mask is true for the second
argument, and the value to take where the mask is false for the third
argument.  We use the uniform distribution (``np.random.random``)
sampled over [0,1] to randomly select steps in the positive direction
where the random deviates are greater than 0.5, and steps in the
negative direction where the deviates are less.

.. ipython::

   In [139]: Uniform = np.random.random(size=(100,10))

   In [140]: Steps = np.where(Uniform>0.5, 1, -1)

   In [141]: Position = Steps.cumsum(axis=0)

   @ savefig simple_random_walk.png width=6in
   In [142]: plot(Position);

Likewise, we can draw from the wealth of statistical distributions in
``np.random`` and ``scipy.stats`` to create deviates from more
esoteric distributions, for example ``scipy.stats.levy_stable.rvs`` to create
`Lévy flights <http://en.wikipedia.org/wiki/Levy_flights>`_.

