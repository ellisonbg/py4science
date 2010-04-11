.. _getting_started:

================
Getting started
================

It can be a bit bewildering for a newcomer to Python to figure out
where to start.  Unlike many environments in which people do
scientific computing, Python is a programming language.  Matlab (TM),
Mathematica (TM), IDL (TM), R, Sage, are all *environments* for
computing: they all provide a scripting language, an interactive
shell, a code editor and debugger, a graphics library, integrated
documentation and numerical algorithms built-in.  By contrast, Python
is a programming language which has some of these things built-in, but
it is not designed to be an environment for scientific computing.  It
can be, and is, the basis of a top-notch scientific computing
environment, but these pieces have to be assembled.  Many newcomers to
Python feel overwhelmed by the multitude of choices.

The freedom to assemble the pieces as you like is a blessing for the
advanced researcher or programmer, but it can be a curse for the
newcomer, who wants things to just work out of the box without too
much assembly required.  Fortunately, there are sophisticated packages
like the Enthought Python Distribution (EPD) and Python(x,y), which do
provide a comprehensive environment for scientific computing in a
single click installer.  We encourage people to use these packages.
For those who want to assemble their own and for those who want a
better understanding of how the core pieces fit together, we will look
at the core pieces that make up any good environment for scientific
computing, and the Python packages filling these niches that have been
forged by community development and use.

.. ipython::
   :suppress:

   # set up ipython for plotting in pylab
   In [4]: from pylab import *

   In [5]: ion()

   In [6]: bookmark ipy_start
.. _mins:

MINS
====

The basic components we need are: a good programming language
(Python), a code editor (you decide), and interactive shell in which
to type commands and explore data (IPython), support for efficient
array based computations (numpy), a library of efficient scientific
algorithms (scipy), and the ability to make scientific graphs
(matplotlib) and efficient interactive 3D visualization (MayaVi).
There are many other other wonderful packages out there, some of which
are absolutely essential for certain kinds of work, but with Python
and (M)atplotlib, (I)Python, (N)umpy and (S)cipy (MINS) you can achieve a
fantastic level of productivity, and these tools alone are all that
many people need, particularly at the student level.

We'll explore each of these components in turn.  Because there are a
variety of ways to install Python and associated tools across the
major platforms, we won't cover this here, since one size does not fit
all.  There are good turn-key solutions like EPD and Python(x,y) for
getting everything in an easy installer, so we'll assume you have
either installed everything from one of these packages or have
installed the components yourself.  Note that while Python(x,y) is
completely free for academic and commerical use, EPD is free only for
academic use and others can either try the demo version or pay a
licensing fee with various levels of support -- the academic download
is avalable at `EPD academic
<http://www.enthought.com/products/edudownload.php>`_

.. _python_getting_started:

The Python Language
-------------------

As we discussed at some length in :ref:`why_python`, the major reasons
to use Python for scientific computing are: the language itself, the
quality of the extensions, and inter-operability with other languages.
Some of the "everything under one roof" environments like Matlab and
IDL mentioned above leave something to be desired in the scripting
languages they provide.  Python, by contrast, is a first class
programming language with support for multiple popular programming
paradigms.  While you could implement a free-standing web application
server in Matlab, you probably wouldn't want to.  In contrast, the
*Curse of Python* is that it is so fun and easy to implement powerful
tools that people often prefer to "roll their own" web application
server, plotting library or machine learning toolkit rather than use
someone elses.  This is a bit tongue in cheek: over time communities
do coalesce around successful packages, but in early stages there is
often too much choice rather than too little simply because Python
developers enjoy writing Python code, since it is so expressive and
powerful.


We'll introduce the basics of the python programming language below in
:ref:`python_mini_tutorial`.  For now, make sure you can fire up the
interactive interpreter.  In linux or OS X, to start the python
interpreter you should open a terminal window and simply type
``python``.  In Windows, there will be an entry for Python in the
Start Menu, under a top-level folder like "Python" or "EPD" depending
on where you got your Python distribution from; Python(x,y) has a
launcher dialog from which you can choose from and launch different
interactive consoles and editors.  In the example below, the command
with the single prompt ``> python`` is executed in the the linux
terminal and starts the python interpreter, which uses the triple
prompt ```>>>``` for python commands passed to the interactive Python
interpreter::

  > python
  Python 2.6.4 (r264:75706, Nov  2 2009, 14:38:03)
  [GCC 4.4.1] on linux2
  Type "help", "copyright", "credits" or "license" for more information.
  >>> 2**100
  1267650600228229401496703205376L
  >>> x = 'This is not a pipe'
  >>> x.replace(' ', '_')
  'This_is_not_a_pipe'
  >>> for i in range(5):
  ...      print i**2
  ...
  0
  1
  4
  9
  16


.. figure:: _static/pythonxy_launcher.png

   *The Python(x,y) launch utility* for windows and ubuntu linux.
   Choose your editing environment under "Applications" and click the
   green check mark to launch.  Choose the "Interactive console", here
   the plain vanilla python interpreter but next we'll launch the much
   enhanced IPython interpreter


Now that we've tested the interactive interpreter, next we want to
write a simple python script and make sure we can run it in python.
For this you will need a code editor.  Many hardcore programmers use
the plain text editors emacs or vi, and there are endless debates and
even paintball wars to resolve which is superior.  We won't wade into
that particular debate except to say both are good choices and if you
have some time to invest in your future productivity, learning one of
these editors will pay off in spades, but does entail a significant
"up-front" cost.  There are a variety of choices for those who prefer
a graphical user interface environment for their editor, with the
traditional "File/Edit" menus for loading and saving files with a
mouse and doing search-and-replace operations.  A good choice is `Idle <http://docs.python.org/library/idle.html>`,
a tkinter based editor which comes with the standard Python distribution.
Another good choice is the `SciTE
<http://www.scintilla.org/SciTE.html>`_ editor which ships with
Python(x,y) and EPD, runs across major platforms, and supports python
and most every other programming languages.  Essential things to look
for in an editor are: syntax highlighting, syntax aware automatic
indentation for code blocks, and the ability to use whitespace instead
of tabs for indentation. google "python code editor" for more
information and see the `python editors
<http://wiki.python.org/moin/PythonEditors>`_ section of the Python
wiki.

Once you've selected your editor, create a simple file called
:file:`my_hello.py` and save it somewhere easy to navigate to on your
file system.  Our first script will print out the ASCII codes of the
characters in "Hello World".

.. sourcecode:: python

    mystring = 'Hello World'
    for c in mystring:
        print(ord(c))

and we can execute this file from the terminal (in windows you can get
access to a primitive terminal by running ``cmd.exe``)::

  > python my_hello.py
  72
  101
  108
  108
  111
  32
  87
  111
  114
  108
  100



In Windows you can execute a python file which ends in the suffix
".py" by double clicking on it.  When you double click on it, you
will see a command terminal window pop up, whatever output your
program generates will scroll by, and the window will immediately
disappear as soon as your program finished.  For most programs, this
will happen in the blink of an eye, and you won't be able to see
what output your program generated.  You can prevent your program
from exiting by causing the execution to block waiting for input
from the user by making a call to ``raw_input``.  Eg, for the test
program above, we could write::

  mystring = 'Hello World'
  for c in mystring:
      print(ord(c))


  raw_input("press any key to exit")

If you are running your program from the command like or a Python
editor like Idle, or better yet from the IPython shell which we
introduce below, this won't be necessary.


.. _ipython_getting_started:

IPython
--------

The interactive interpreter is one of the core strengths of python.
Unlike compiled languages like C, FORTRAN and C++ which typically lead
to a work-flow where you write code, compile it, run it, find
problems, go back and insert diagnostic output, and repeat *ad
nauseum*, with an interactive interpreter you can explore code and data
as you develop it.  The Python interpreter is great for this, but is
not a full featured command shell that you expect if you are used to
modern terminal environments like the bash shell which include the
ability to navigate the file systems, set bookmarks on favorite
locations, use aliases for often typed commands, and use command
completion, history and other nice readline features.  The "I" in
IPython stands for *Interactive* and it is a Python shell on steroids,
integrating all the features from the standard python interpreter with
all the desirable features just mentioned and more.

For many people who do scientific computing in Python as part of their
research or employment, an open IPython shell is as much a feature of
their everyday, all day work environment as a firefox web browser, a
terminal shell and their favorite editor.  For the rest of this book,
we'll spend *most* of our time in an IPython shell.  We can launch it
just like we launched the plain vanilla Python interpreter above, but
this time we'll prefix our command with an "i", and instead of seeing
the familiar triple quoted prompt ``>>>`` from the Python interpreter,
we see Mathematica-style numbered input and output prompts.  In the
example below, we seamlessly blend python commands like ``2**100``
with basic file system navigation and manipulation commands like
``cd``, ``mkdir`` and ``!more`` ::

  > ipython
  Python 2.6.4 (r264:75706, Nov  2 2009, 14:38:03)
  Type "copyright", "credits" or "license" for more information.

  IPython 0.10 -- An enhanced Interactive Python.
  ?         -> Introduction and overview of IPython's features.
  %quickref -> Quick reference.
  help      -> Python's own help system.
  object?   -> Details about 'object'. ?object also works, ?? prints more.

  In [1]: 2**100
  Out[1]: 1267650600228229401496703205376L

  In [2]: mkdir mypy

  In [3]: cd mypy/
  /home/jdhunter/mypy

  In [4]: fh = file('mydata.dat', 'w')

  In [5]: fh.write('this is a test')

  In [6]: fh.close()

  In [7]: ls
  mydata.dat

  In [8]: !more mydata.dat
  this is a test

We'll talk more about IPython below in our :ref:`basic_workflow`
section below.  For now we want to complete our tour of the basic MINS
components to make sure everything is installed and working properly.


.. _numpy_getting_started:

Numpy
-------

Numpy is the core extension library on which almost all other
libraries for scientific computing in python are built.  It provides
an N-dimensional array implemented in C which provides extremely fast
operations on large blocks of data.  For example, in plain python to
compute $2 i^2$ for the first 5 integers, we could write a for-loop

.. ipython::

   In [130]: for i in range(5):
      .....:     print i, 2*i**2
      .....:
      .....:
   0 0
   1 2
   2 8
   3 18
   4 32

but this can be quite slow for a large number of integers because
python is a dynamic interpreted language.  For each integer in the
loop, python has to look up i, determine its type and value, look up
the multiplication and exponention operators ``*`` and ``**`` to see
how to handldle them for integers and so on.  And it doesn't learn: it
does each of these operations on every pass through the loop.  This
can be extremely slow.  In numpy we simply do

.. ipython::


   In [139]: import numpy as np

   In [140]: x = np.arange(5)

   In [141]: 2*x**2
   Out[141]: array([ 0,  2,  8, 18, 32])

Not only is this syntactically convenient -- we can get the same
result with less typing and less code -- it has much better
performance in an interpreted language like Python because most of the
work happens in C.  Python only has to do look up the variable name
"x" and multiplication and exponention operators one time to see how
to use them with numpy arrays, unlike in the Python case where it had
to do the look up in each iteration of the loop.  For loops with a
large number of iterations, the differences can be a 100-fold or more
performance improvement, which is why dynamic interpreted languages
like Python and Matlab rely so heavily on array based computations.
This is sometimes confusing for people coming from languages which do
not encourage or support array based element-wise operations.

In this book, as above, we will be utilizing the import abbreviation
``np`` for ``numpy``.  You can check which version of numpy you are
running, and where it is installed, by inspecting the ``__version__``
and ``__file__`` attributes.

.. ipython::

   In [18]: np.__file__
   Out[18]: '/home/jdhunter/dev/lib/python2.6/site-packages/numpy/__init__.pyc'

   In [19]: np.__version__
   Out[19]: '1.4.0.dev7577'


Creating numpy arrays
~~~~~~~~~~~~~~~~~~~~~

The basic data structure numpy provides is an N-dimensional array of
homogeneous elements, the ``ndarray``.  The simplest ndarray is one
dimension, for example the numbers from 0..5 we used in the example
above which we created with ``np.arange(5)`` -- this is the numpy
version of the built-in python function ``range`` which creates a
*list* of the integers from 0 to 5.

.. ipython::


   # a python list
   In [52]: mylist = range(5)

   In [53]: mylist
   Out[53]: [0, 1, 2, 3, 4]

   # a numpy array
   In [54]: myarray = np.arange(5)

   In [55]: myarray
   Out[55]: array([0, 1, 2, 3, 4])

You may be surprised that both ``mylist`` and ``myarray`` do not
include the end point number 5; this is a feature of python in which
ranges start at the beginning number and go up to, but do not include
the terminal number.  Unlike the python list in ``mylist``, the numpy
array ``myarray`` is build for efficieny in storage and performance,
and is represented internally as a C data buffer of integers.  There
are several crucial methods to inspect the size and type of numpy
arrays, including ``shape``, ``size``, and ``dtype``, which show the
dimensional shape of the array, the total number of elements in the
array, and the datatype of the array (eg integer or float).

.. ipython::

   # the shape here is a length 1 python tuple reflecting the fact
   # that myarray is is a 1 dimensional array.  The first (and only)
   # dimension has 5 elements in it
   In [56]: myarray.shape
   Out[56]: (5,)

   In [57]: myarray.size
   Out[57]: 5

   # the dtype, or "data type" here is 'int32' for a 32 bit integer.
   # If you are working on a 64 bit architecture, you will see 'int64'
   @verbatim
   In [58]: myarray.dtype
   Out[58]: dtype('int32')


There are lots of ways of creating numpy arrays.  ``np.arange``
created 5 python integers from 0 to 5; it inspected the argument ``5``
and inferred that we wanted to create an integer array.  If instead we
wanted to create an array of floating point numbers, we could give the
argument ``5.0`` or explicitly pass in ``dtype=float`` to the
constructor.

.. ipython::

   # note the "." at the end of the numbers, indicating floating point
   # numbers
   In [76]: farray = np.arange(5.)

   In [77]: farray
   Out[77]: array([ 0.,  1.,  2.,  3.,  4.])

   # unlike integers, where the default size of 32bit or 64bit is
   # platform dependent, the default floating point size is 64bit (8
   # bytes).
   In [78]: farray.dtype
   Out[78]: dtype('float64')

   In [79]: farray = np.arange(5, dtype=float)

   In [80]: farray
   Out[80]: array([ 0.,  1.,  2.,  3.,  4.])

   In [81]: farray.dtype
   Out[81]: dtype('float64')

There are several other useful functions for creating numpy arrays.
``np.array`` creates an array from existing data.  Below we create a
two dimension array from lists of python integers

.. ipython::

   In [91]: X = np.array([[4,5,6,7], [12,13,14,15]])

   In [92]: X
   Out[92]:
   array([[ 4,  5,  6,  7],
	  [12, 13, 14, 15]])

   # the shape is a length 2 tuple showing that the array is 2 rows
   # and 4 columnes
   In [93]: X.shape
   Out[93]: (2, 4)

   # the size is the total number of elements in the array
   In [94]: X.size
   Out[94]: 8

   In [95]: X.dtype
   Out[95]: dtype('int32')


Another set of handy functions for creating arrays are ``zeros`` and
``ones``, create an array filled with either zeros or ones.  In the
example below, we create a 3x3x4 array of zeros and then assign the
first element the value 12

.. ipython::

   In [108]: Z = zeros((3,3,4))

   In [109]: Z.shape
   Out[109]: (3, 3, 4)

   In [110]: Z[0,0,0] = 12

   In [111]: Z
   Out[111]:
   array([[[ 12.,   0.,   0.,   0.],
	   [  0.,   0.,   0.,   0.],
	   [  0.,   0.,   0.,   0.]],

	  [[  0.,   0.,   0.,   0.],
	   [  0.,   0.,   0.,   0.],
	   [  0.,   0.,   0.,   0.]],

	  [[  0.,   0.,   0.,   0.],
	   [  0.,   0.,   0.,   0.],
	   [  0.,   0.,   0.,   0.]]])


Two other functions we will be using a lot to create numpy arrays in
this book are the random number array generators ``np.random.rand``
and ``np.random.randn``.  The first creates random numbers from the
uniform distribution from 0..1, and the second creates Gaussian random
numbers with zero mean and unit standard deviation (the "n" in "randn"
is for "normal").

.. ipython::

   # 5 random numbers from the uniform distribution over 0..1
   In [117]: x = np.random.rand(5)

   In [118]: x
   Out[118]: array([ 0.17123039,  0.35602158,  0.9429075 ,  0.26874412,  0.55789462])

   # 5 new random numbers from the uniform distribution over 0..1
   In [119]: x = np.random.rand(5)

   In [120]: x
   Out[120]: array([ 0.60718795,  0.33060536,  0.06879506,  0.02842788,  0.060915  ])



You can also create new arrays from operations on existing arrays, for
example, by creating a new array ``y = 2*x`` which will have the same
size and dtype as ``x`` but will be twice the value for each element.

Finally, perhaps the most useful way to create numpy arrays is to load
them from files using the functions ``np.loadtxt``, ``np.load`` and
``np.fromfile``.  We will be encountering these in many examples below
as we explore numpy in more depth.

numpy indexing and slicing
~~~~~~~~~~~~~~~~~~~~~~~~~~

You can *view* individual elements of the array using the integer
index starting at 0 and ending at the length of the array minus one.

.. ipython::

   In [176]: x = 3*np.arange(7)

   In [177]: x
   Out[177]: array([ 0,  3,  6,  9, 12, 15, 18])

   In [178]: x[0]
   Out[178]: 0

   In [179]: x[1]
   Out[179]: 3

   In [180]: x[6]
   Out[180]: 18


You can index into the end of the array using negative
numbers -- -1 is the last elememt of the array, -2 is the second to
last, etc...

.. ipython::

   In [181]: x[-1]
   Out[181]: 18

   In [182]: x[-2]
   Out[182]: 15


Similarly, you can *assign* to elemtns of the array with the same syntax.

.. ipython::

   In [183]: x[1] = 2358

   In [184]: x[-2] = 123

   In [185]: x
   Out[185]: array([   0, 2358,    6,    9,   12,  123,   18])


For multi-dimensional arrays, you specify the index of each axis in
the array, starting with the row index, then the column index, and so
on for higher dimensions.

.. ipython::

   # X is a two dimensional array, the first axis is the rows, the
   # second axis is the columns.
   In [187]: X = np.array([[4,5,6,7], [12,13,14,15]])

   In [188]: X
   Out[188]:
   array([[ 4,  5,  6,  7],
	  [12, 13, 14, 15]])

   In [189]: X[0,2]
   Out[189]: 6

   In [190]: X[1,-1]
   Out[190]: 15

For a multi-dimensional array, if you give an index argument for less
than the total number of dimensions, you get all of the elements of
the remaining unspecified dimensions.  For example, X[0] specifies the
entire first row and X[-1] is the entire last row

.. ipython::

   In [191]: X[0]
   Out[191]: array([4, 5, 6, 7])

   In [192]: X[-1]
   Out[192]: array([12, 13, 14, 15])

When you assign to a slice like the those in the rows above, numpy
will try and mathc the shapes of the left hand side and right hand
sides using broadcasting.  If the two sides have identical shapes, the
assigment is straigntforward element-wise assigment.  If the right
hand side has fewer elements than the left hand side, the element will
be repeated to fill up the slice on the left hand side.

.. ipython::

   # the left hand and right hands sides are the same shape,
   # element-wise assignment

   In [196]: X[0] = [8,9,10,11]

   In [197]: X
   Out[197]:
   array([[ 8,  9, 10, 11],
	  [12, 13, 14, 15]])

   # the left hand side is 4 elements, the right hand side is a single
   # element, so the single element is broadcast to fill the left hand
   # side

   In [198]: X[-1] = 23

   In [199]: X
   Out[199]:
   array([[ 8,  9, 10, 11],
	  [23, 23, 23, 23]])



numpy has a powerful syntax for viewing and operating on individual
elements or slices of an array, using the
``INDEX_START:INDEX_END:STRIDE`` syntax inspired Matlab(TM).  For
example, to view a slice of every 2nd element (the ``STRIDE``) in the
range from 0..20 starting at element 4 (``INDEX_START`` included) and
ending at element 14 (``INDEX_END`` not included) you write

.. ipython::

   In [153]: x = np.arange(20)

   In [154]: x
   Out[154]:
   array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
	  17, 18, 19])

   In [155]: x[4:14:2]
   Out[155]: array([ 4,  6,  8, 10, 12])

Each of these three slice arguments has a default value and can be left out.
``INDEX_START`` defaults to 0, ``INDEX_END`` defaults to the length of
the array, and ``STRIDE`` defaults to 1.  Here are several examples
illustrating the defaults.

.. ipython::

   # INDEX_START defaults to 0
   In [158]: x[:10:2]
   Out[158]: array([0, 2, 4, 6, 8])

   # INDEX_END defaults to 20
   In [159]: x[4::2]
   Out[159]: array([ 4,  6,  8, 10, 12, 14, 16, 18])

   # STRIDE defaults to 1
   In [160]: x[4:10]
   Out[160]: array([4, 5, 6, 7, 8, 9])

   # INDEX_START defaults to 0, INDEX_END defaults to 20
   In [161]: x[::2]
   Out[161]: array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18])

   # INDEX_START, INDEX_END and STRIDE all take on default values
   In [163]: x[::]
   Out[163]:
   array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
	  17, 18, 19])

   # INDEX_START, INDEX_END and STRIDE all take on default values
   In [164]: x[:]
   Out[164]:
   array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
	  17, 18, 19])


Now that we've indroduced indexing and slicing, we can combine the
two.  For example, in a two dimensional array, the first axis might be
indexed with a single integer index, and the second axis with a slice
index.

.. ipython::

   In [202]: X = np.array([[4,5,6,7], [12,13,14,15]])

   In [203]: X[1, 1::2]
   Out[203]: array([13, 15])




Working with numpy arrays
~~~~~~~~~~~~~~~~~~~~~~~~~

In addition to providing the basic array data structure, numpy
provides a set of core mathematical functions *ufuncs* on this data,
eg sin, cos, exp, log, as well as core numerical algorithms like
convolution, correlation, and FFTs, and basic descriptive statistics
like mean, standard deviation, min, max and median.  In IPython you
can explore the numpy namespace using TAB completion; eg to see all
the methods that are available on the basic array object ``x`` in the
example below, we type ``x.<TAB>``

.. ipython::

   In [5]: x = np.arange(5.)

   @verbatim
   In [6]: x.<TAB>
   x.T             x.cumsum        x.min           x.shape
   x.all           x.data          x.nbytes        x.size
   x.any           x.diagonal      x.ndim          x.sort
   x.argmax        x.dtype         x.newbyteorder  x.squeeze
   x.argmin        x.dump          x.nonzero       x.std
   x.argsort       x.dumps         x.prod          x.strides
   x.astype        x.fill          x.ptp           x.sum
   x.base          x.flags         x.put           x.swapaxes
   x.byteswap      x.flat          x.ravel         x.take
   x.choose        x.flatten       x.real          x.tofile
   x.clip          x.getfield      x.repeat        x.tolist
   x.compress      x.imag          x.reshape       x.tostring
   x.conj          x.item          x.resize        x.trace
   x.conjugate     x.itemset       x.round         x.transpose
   x.copy          x.itemsize      x.searchsorted  x.var
   x.ctypes        x.max           x.setfield      x.view
   x.cumprod       x.mean          x.setflags


If you are typing along, your probably see many more names with double
underscores like ``__gt__`` but we've suppressed these by configuring
our IPython interpreter in :file:`.ipython/ipythonrc` with the
``readline_omit__names 2`` option to hide attributes with special
names.

But no matter how you are configured, those are a lot of symbols --
the basic numpy array is feature rich and powerful.  Below are a
sampling with intuitive names -- try ``help`` on any method to see
more information, for example in ipython you can type ``help x.clip``
which clips the values in a numpy array to the min/max values
specified in the ``clip`` method call.


.. ipython::

   In [6]: x
   Out[6]: array([0, 1, 2, 3, 4])

   In [7]: x.mean()
   Out[7]: 2.0

   In [8]: x.max()
   Out[8]: 4

   In [9]: x.clip(0, 2.5)
   Out[9]: array([ 0. ,  1. ,  2. ,  2.5,  2.5])




The TAB completion listing on ``x`` above shows the *array
attributes*: the functions and attributes attached to the numpy array
object itself.  In addition, there are many more functions that are
part of the numpy namespace that operate on numpy arrays but are not
part of the array object.  These include functions like ``sin`` and
``exp``

.. ipython::

   In [10]: np.exp(x)
   Out[10]: array([  1.        ,   2.71828183,   7.3890561 ,  20.08553692,  54.59815003])


as well as algorithms like ``corrcoef``, ``convolve`` and
``histogram``, and random number generators like ``np.random.rand``
and ``np.random.randn``.  Below we create two arrays of 100 normally
distributed random numbers and compute their correlation matrix; items
on the diagonal are correlation with self and hence 1.0.

.. ipython::

   In [13]: y1, y2 = np.random.randn(2, 100)

   In [14]: np.corrcoef(y1, y2)
   Out[14]:
   array([[ 1.       , -0.0669782],
	  [-0.0669782,  1.       ]])

We'll return to numpy in much more depth in :ref:`numpy_getting_started` and
almost every subsequent chapter in this book.  For now we'll continue
with our tour of MINS.


.. matplotlib_getting_started:

Matplotlib
-----------

Matplotlib is a package for making scientific graphs and data
visualizations.  Although it has limited support for basic 3D graphs
like surfaces and meshes, its core focus is on making publication
quality 2D graphics.  Data visualization is a rich area, and there
many different things people want to do when generating graphics.
Perhaps the most common is exploratory analysis where you want to
load, process, and plot data interactively at the command line prompt,
and matplotlib supports this in conjunction with IPython in the
*pylab* mode, which provides a Matlab-like environment for easily
creating and manipulating plots with a procedural interface that is
easy for scientists with little programming expertise to master.
Moving past the quick-and-easy exploratory phase, experienced
programmers in labs often want to build interfaces where scientists
can interact with their data, selecting and annotating regions of
interest, monitoring incoming data in quasi real time, navigating
through deep and nested data sets, and matplotlib supports this
through a FigureCanvas object that is embeddable in all the common
user interface toolkits available in Python.  Yet another common need
is a headless server generating static hardcopy for review later or to
be served up dynamically in a web application server, which matplotlib
supports through a full object oriented API that gives the server
complete control over the graphics creation and rendering process.

Because these different modes of working require matplotlib to be
configured, imported and used in different ways, newcomers are
sometimes unsure what is *right* way to use matplotlib, and the answer
is that the right way depends on what you are trying to do: the most
natural way to work interactively and make quick and easy plots is
through pylab, and the right to serve data through a web application
server is to use the matplotlib API directly with no help from pylab.
As we tackle different kinds of examples in this book, we'll
illustrate these various idioms with commentary without bogging down.
Borrowing a phrase from Larry Wall and Perl, matplotlib tries to "make
easy things easy and hard things possible".  So let's start with the
easy things, and fire up IPython in pylab mode and make a plot.


You can start IPython in pylab mode, which pre-imports all of numpy
and matplotlib, and tweaks some matplotlib settings so that plotting
"just works", ie figures pop up when you type "plot" and are updated
when you type commands.  In windows, IPython has a menu entry in the
start menu for starting pylab mode, as shown below

.. figure:: _static/ipython_pylab_windows.png
   :width: 4in

   A windows XP screenshot launching IPython in *pylab* mode from the
   start menu

If you installed python from a package distribution like EPD_ or
pythonxy_, the menu entry will be different, eg "Enthought ->
EPD_VERSION -> Pylab (IPython)"


From a terminal window in linux or OS X, you can simply type::

  > ipython -pylab
  Python 2.4.5 (#4, Apr 12 2008, 09:09:16)
  Type "copyright", "credits" or "license" for more information.

  IPython 0.10 -- An enhanced Interactive Python.
  ?         -> Introduction and overview of IPython's features.
  %quickref -> Quick reference.
  help      -> Python's own help system.
  object?   -> Details about 'object'. ?object also works, ?? prints more.

    Welcome to pylab, a matplotlib-based Python environment.
    For more information, type 'help(pylab)'.

  In [1]: hist(randn(10000), 100);

If you see the following graph pop up, everything is working (if not
see the matplotlib installation `faq
<http://matplotlib.sourceforge.net/faq/installing_faq.html>`_ and
:ref:`how_to_get_help`).


.. plot::
   :width: 4in

   import matplotlib.pyplot as plt
   import numpy as np
   x = np.random.randn(10000)
   plt.hist( x, 100)

We'll walk through a simple matplotlib example which also exercises
some numpy: loading a black and white image and doing some
pseudo-color mapping using a photo taken by Michael Sarahan and used
in his matplotlib `image tutorial
<http://matplotlib.sourceforge.net/users/image_tutorial.html>`_.

First we navigate to the :ref:`sample_data` directory and load and
plot the "stinkbug" image with pyplot's `imshow
<http://matplotlib.sourceforge.net/api/pyplot_api.html#matplotlib.pyplot.imshow>`_


.. ipython::

   In [2]: cd bookdata/
   /home/jdhunter/py4science/book/bookdata

   In [3]: im = imread('stinkbug.png')

   @savefig mystinkbug.png width=4in
   In [4]: imshow(im)
   Out[4]: <matplotlib.image.AxesImage object at 0x39ea850>

The image data in ``im`` is an RGB array, which is three 2D images of
the red, green, and blue planes.  The true data is gray-scale, as we
see in the image above, so all three channels are identical, as we can
see by using the numpy `all
<http://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.all.html>`_
method, which returns true if every element in the array is true.

.. ipython::

   In [5]: im.shape
   Out[5]: (375, 500, 3)

   In [6]: red = im[:,:,0]

   In [7]: green = im[:,:,1]

   In [8]: blue = im[:,:,2]

   In [9]: (red==green).all()
   Out[9]: True

   In [10]: (red==blue).all()
   Out[10]: True


so we can take any one of these channels to be the "luminosity"
channel ``lum``, or more generally we can take the average of red,
green and blue to get the lumonsity channel by taking the average of
the red, green and blue channels.  We can do this in numpy by
computing the mean over the last axis, which is ``axis=2``.  Since
this is luminosity data, we can do pseudo-color mapping.

.. ipython::

   # lum for "luminosity"
   In [14]: lum = im.mean(axis=2)

   In [15]: imshow(lum)
   Out[15]: <matplotlib.image.AxesImage object at 0x2ade550>

   @savefig stinkbug_spectral.png width=4in
   In [16]: spectral()

Here the function `spectral
<http://matplotlib.sourceforge.net/api/pyplot_api.html#matplotlib.pyplot.spectral>`_
activates the spectral colormap, which sets the current colormap to
``cm.spectral`` where ``cm`` is the matplotlib colormap module
`matplotlib.cm <http://matplotlib.sourceforge.net/api/cm_api.html>`_.
There are over 100 colormaps, which you can explore via tab completion
in IPython.  Two popular colormaps are ``cm.hot`` for *Heated ObjecT*
scale, and ``cm.jet`` which was invented by NASA's Jet Propulsion
Laboratory.




A common need in analyzing luminosity images is to enhance the
contrast by limiting the scale of the colormapping to a tighter range
than the full 0..1 scale of the pixel intensities.  To accomplish
this, we can plot a histogram of the pixel intensities, and *clip* the
color limits to a range that encompasses the bulk of the data.  We
need to *flatten* the data using the `flatten <http://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.flatten.html>`_ method which takes an
N dimensional array and flattens it into a 1D array.

.. ipython::

   In [30]: plt.close('all')

   @savefig stinkbug_hist.png width=4in
   In [31]: hist(lum.flatten(), 100, range=(0,1));


We see that the bulk of the data lies between 0.3 and 0.7, so we can
update clip the color limits to this range to enhance the contrast

.. ipython::

   In [38]: plt.close('all')

   In [39]: imshow(lum, cmap=cm.spectral)
   Out[39]: <matplotlib.image.AxesImage object at 0x4acca10>

   @savefig stinkbug_contrast.png width=5in
   In [46]: clim(0.3, 0.7)


As in the example above, you can also pass a colormap into ``imshow``
using the *cmap* keyword argument, as in ``imshow(lum,
cmap=cm.hot)``.  first, and pass a 1D array to the histogram function.

Here are the ones starting with "s"

.. ipython::

   In [21]: import matplotlib.cm as cm

   @verbatim
   In [22]: cm.s<TAB>
   cm.spectral    cm.spring      cm.summer
   cm.spectral_r  cm.spring_r    cm.summer_r

All of the colormaps have a *reversed* counterpart named with the
postfix "_r" (eg ``summer`` and ``summer_r``) which inverts the
normal color order of the map from luminosity to color.  For, example,
``cm.gray`` maps 0.0 to black and 1.0 to white, and ``cm.gray_r`` maps
0.0 to white and 1.0 to black.

.. ipython::

   In [62]: plt.close('all')

   In [63]: X = np.arange(96).reshape(12,8)

   # one row, two columns, first (left) axes
   In [64]: subplot(121)
   Out[64]: <matplotlib.axes.AxesSubplot object at 0x5dbe6d0>

   In [65]: imshow(X, origin='lower', cmap=cm.gray)
   Out[65]: <matplotlib.image.AxesImage object at 0x5de6450>

   # one row, two columns, second (right) axes
   In [66]: subplot(122)
   Out[66]: <matplotlib.axes.AxesSubplot object at 0x5ded110>

   @savefig cmap_reversed.png width=5in
   In [67]: imshow(X, origin='lower', cmap=cm.gray_r)
   Out[67]: <matplotlib.image.AxesImage object at 0x610f090>

.. scipy_getting_started:

Scipy
-----

For a quick look at what's available in scipy, just import it and type
``help scipy`` in IPython.


.. sourcecode:: ipython

   In [269]: import scipy

   In [270]: help scipy

The top level packages are shown in the table below.


================================ ==============================================
Package                          Functionality
================================ ==============================================
``odr``                          Orthogonal Distance Regression
``cluster``                      Vector Quantization / Kmeans
``fftpack``                      Discrete Fourier Transform algorithms
``io``                           Data input and output
``special``                      Airy Functions
``lib.blas``                     Wrappers to BLAS library
``sparse.linalg.eigen``          Sparse Eigenvalue Solvers
``stats``                        Statistical Functions
``lib``                          Python wrappers to external libraries
``lib.lapack``                   Wrappers to LAPACK library
``maxentropy``                   Routines for fitting maximum entropy models
``integrate``                    Integration routines
``ndimage``                      n-dimensional image package
``linalg``                       Linear algebra routines
``spatial``                      Spatial data structures and algorithms
``interpolate``                  Interpolation Tools
``sparse.linalg``                Sparse Linear Algebra
``sparse.linalg.dsolve.umfpack`` Interface to the UMFPACK library
``sparse.linalg.dsolve``         Linear Solvers
``optimize``                     Optimization Tools
``sparse.linalg.eigen.arpack``   Eigenvalue solver using iterative methods.
``signal``                       Signal Processing Tools
``sparse``                       Sparse Matrices
================================ ==============================================


To get additional information about a subpackage, you first need to
import it, and then ask for help on the package.


.. ipython::
   :verbatim:

   In [48]: import scipy.optimize

   In [49]: help scipy.optimize



.. _sample_data:

Sample data
=============

The data for the examples used in the book is available at bookdata_.
Download this zip file and unzip it in a working directory on your
system.  You can check your self to make sure the download and unzip
was successful by testing to see if you can load a simple dataset from
ipython.

.. sourcecode:: ipython

  In [13]: cd bookdata/
  /home/titan/johnh/py4science/book/bookdata

  In [14]: ls bodyfat*
  bodyfat.dat          bodyfat_readme.txt

  In [15]: import numpy as np

  In [16]: X = np.loadtxt('bodyfat.dat')

  In [17]: print X.shape
  (252, 15)









.. _python_mini_tutorial:

A Python Mini-Tutorial
======================

TODO


.. _basic_workflow:

Basic workflow
================

TODO

.. _how_to_get_help:

How to get help
===============


TODO

.. _futher_reading:

Suggestions for further reading
===================================

TODO


.. ipython::
   :suppress:

   # return to home
   In [4]: cd -b ipy_start

   In [5]: plt.close('all')

.. include:: links.txt
