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
can be, and is, the basis if a top-notch scientific computing
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
completely free for academic and commerical use, EPS is free only for
academic use and others can either try the Demo version or pay a
licensing fee -- the academic download is avalable at `EPD academic
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
do coalece around successful packages, but in early stages there is
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
terminal and starts the python interpreter, which uses the a prompt
```>>>``` for python commands passed to the interactive Python
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


Now that we've tested the interactive interpeter, next we want to
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
mouse and doing search-and-replace operations.  A good choice is the
`SciTE <http://www.scintilla.org/SciTE.html>`_ editor which ships with
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

    s = 'Hello World'
    for char in s:
        print(ord(char))

and we can execute this file from the terminal (in windows you can get
access to a primitize terminal by running ``cmd.exe``)::

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



.. _ipython_getting_started:

IPython
--------

The interactive interpreter is one of the core strengths of python.
Unlike compiled languages like C, FORTRAN and C++ which typically lead
to a work-flow where you write code, compile it, run it, find
problems, go back and insert diagnositic ouput, and repeat *ad
nauseum*, with an interactive interpeter you can explore code and data
as you develop it.  The Python interpreter is great for this, but is
not a full featured command shell that you expect if you are used to
modern terminal environments like the bash shell which include the
ability to navigate the file systems, set bookmarks on favorite
locations, use aliases for often typed commands, and use command
completion, history and other nice readline features.  The "I" in
IPython stands for *Interactive* and it is a python shell on steroids,
integrating all the features from the standard python interpreter with
all the desirable features just mentioned and more.

For many people who do scientific computing in Python as part of their
research or employment, an open IPython shell is as much a feature of
their everyday, allday work environment as firefox, a terminal shell
and their favorite editor.  For the rest of this book, we'll spend
*most* of our time in an IPython shell.  We can launch it just like we
launched the plain vanilla Python interpreter above, but this time
we'll prefix our command with an "i", and instead of seeing the
familiar triple quoted prompt ``>>>`` from the Python interpreter, we
see Mathematica-style numbered input and output prompts.  In the
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
compute the square root of the first 5 integers, we could write a
for-loop and use ``math.sqrt``

.. ipython::

   In [11]: import math

   In [12]: for i in range(5):
      ....:     print math.sqrt(i)
      ....:
      ....:
   0.0
   1.0
   1.41421356237
   1.73205080757
   2.0

but this can be quite slow for a large number of integers because
python is a dynamic interpreted language.  For each integer in the
loop, python has to look up i, determine its type and value, look up
the symbol ``math`` and figure out what the ``.`` operator does, and
then look up the name ``sqrt`` and see if implements the function call
operator ``()`` and so on.  And it doesn't learn: it does each of
these operations on every pass through the loop.  This can be
extremely slow.  In numpy we simply do

.. ipython::

   In [13]: import numpy as np

   In [14]: np.sqrt(np.arange(5))
   Out[14]: array([ 0.        ,  1.        ,  1.41421356,
                    1.73205081,  2.        ])

and everything happens in C -- we have to do each lookup only one
time, for example the lookup to figure out what ``np.sqrt`` is --
whereas in python we had to lookup ``math.sqrt`` for each element in
the range.  For loops with a large number of iterations, the
differences can be a 100-fold or more performance improvement, which
is why dynamic interpreted languages like Python and Matlab rely so
heavily on array based computations.

We will be utilizing the import abbreviation for ``np`` throughout the
book.  You can check which version of numpy you are running, and where
it is installed, by inspecting the ``__version__`` and ``__file__``
attributes.

.. ipython::

   In [18]: np.__file__
   Out[18]: '/home/jdhunter/dev/lib/python2.6/site-packages/numpy/__init__.pyc'

   In [19]: np.__version__
   Out[19]: '1.4.0.dev7577'


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
sampling with intuituve names -- try ``help`` on any method to see
more information, for example in ipython you can type ``help x.clip``.


.. ipython::

   In [6]: x
   Out[6]: array([0, 1, 2, 3, 4])

   In [7]: x.mean()
   Out[7]: 2.0

   In [8]: x.max()
   Out[8]: 4

   In [9]: x.clip(0, 2.5)
   Out[9]: array([ 0. ,  1. ,  2. ,  2.5,  2.5])

   In [10]:


The TAB completion listing on ``x`` above shows the *array
attributes*, the functions and attributes attached to the numpy array
object itself.  In addition, there are many more methods that are part
of the numpy namespace that operate on numpy arrays but are not part
of the array object.  These include functions like ``sin`` and ``exp``

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





.. _ipython_pylab:

IPython in pylab mode
----------------------

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
:ref:`how_to_get_help`.


.. plot::

    import matplotlib.pyplot as plt
    import numpy as np
    x = np.random.randn(10000)
    plt.hist( x, 100)



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




.. include:: links.txt
