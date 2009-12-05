
.. _numpy_intro:

************************
Introduction to numpy
************************

``numpy`` arrays are the core data structure for scientific computing
in python, and we've seen lots of examples of their use in the
preceeding pages.  In this chapter we'll take a closer look at how to
create and use numpy arrays.  There are numerous ways to create numpy
arrays, many of which you've seen in previous chapters

* created from scratch using ``np.array``, ``np.zeros``, ``np.ones``
  and ``np.empty``.

* monotonic samples using ``np.arange`` and ``np.linspace``

* from random deviates using ``np.random.rand``, ``np.random.randn``
  and others.

* from data files using ``np.loadtxt``, ``mlab.csv2rec``, ``np.load``
  and more.

Let's look at each of these in turn.

Creating arrays from scratch
-----------------------------

In many problems, you already have your data in some for, for example
a list or a list of lists, and you just want to put it into an array
for efficient computation later.  

.. ipython: 
   In [237]: x
   Out[237]: array([ 0,  1,  4,  9, 16])

   In [238]: x.dtype
   Out[238]: dtype('int64')

   In [239]: x.shape
   Out[239]: (5,)

   In [240]: Y = np.array([[1,2,3,4], [5,6,7,8]], float)

   In [241]: Y.dtype
   Out[241]: dtype('float64')

   In [242]: Y.shape
   Out[242]: (2, 4)


Sometime we know ahead of time the dimension of your problem, and need
to create some storage in arrays to save the results of calculations.
