
.. _numpy_intro:

=======================
 Introduction to numpy
=======================

Todo: write intro about arrays to explain what they are.

``numpy`` arrays are the core data structure for scientific computing
in python, and we've seen lots of examples of their use in the
preceeding pages.  In this chapter we'll take a closer look at how to
create and use numpy arrays.  There are numerous ways to create numpy
arrays, many of which you've seen in previous chapters

* created from scratch using ``np.array``, ``np.zeros``, ``np.ones``
  and ``np.empty``, and their ``_like`` counterparts.

* monotonic samples using ``np.arange`` and ``np.linspace``

* from random deviates using ``np.random``: ``rand``, ``randn``, ``uniform``,
  ``normal``, show others.

* from data files using ``np.loadtxt``, ``mlab.csv2rec``, ``np.load``
  and more.

Let's look at each of these in turn.

Creating arrays from scratch
============================

Using ``np.array``, ``np.zeros``, ``np.ones`` and ``np.empty``.

In many problems, you already have your data in some for, for example
a list or a list of lists, and you just want to put it into an array
for efficient computation later.  The generic :func:`np.array` function is a
flexible function that tries to guess as best as possible both the shape and
the type of a numpy array suitable for storing its argument, and in simple
cases it is often sufficient.

For a simple list of integers, ``array`` will produce a one-dimensional array
whose dtype is ``np.int32`` (on the 32-bit version of Python where this example
was run, it would show ``np.int64`` on a 64-bit system):

.. ipython::

   In [4]: mylist = [1, 2, 3]

   In [5]: myarr = np.array(mylist)

   In [7]: myarr
   Out[7]: array([1, 2, 3])

   In [8]: myarr.shape
   Out[8]: (3,)

   In [11]: myarr.dtype
   Out[11]: dtype('int32')


If given a list of lists, ``array`` will try to guess a suitable 2-dimensional
shape, and we can also force the resulting array dtype explicitly:
   
.. ipython::

   In [240]: Y = np.array([[1,2,3,4], [5,6,7,8]], float)

   In [241]: Y.dtype
   Out[241]: dtype('float64')

   In [242]: Y.shape
   Out[242]: (2, 4)

It is important to recognize that the basic ``array`` call can only *guess*
things like the right dimensionality and shape of your array, and there can be
situations where things fail.  Consider for example:

.. ipython::

   In [19]: np.array([[1,2],[3,4,5]])
   ---------------------------------------------------------------------------
   ValueError                                Traceback (most recent call last)

   /home/fperez/teach/py4science/book/<ipython console> in <module>()

   ValueError: setting an array element with a sequence.

In this example, there is no sensible dimensionality for an array to be created
from the given input list, and the resulting error can be a little confusing
(since it comes from an internal error generated in the internal logic of the
``array`` call).

For situations such as this one, where 

Sometimes we know ahead of time the dimension of your problem, and need to
create some storage in arrays to save the results of calculations.

Arrays with monotonic samples
=============================

using ``np.arange`` and ``np.linspace``

Arrays of random numbers
========================

using ``np.random.rand``, ``np.random.randn`` and
  others.

  
Arrays from data files
======================

using ``np.loadtxt``, ``mlab.csv2rec``, ``np.load``
  and more.
