.. _whirlwind_tour:

==============
Whirwind tour
==============

There is an enormous breadth and depth of packages supporting
scientific computing in python -- the packages in scipy alone could
fill several books worth of documentation -- and we will dive into
this material in some depth in chapters to come.  Before going deep
though, we'd like to start showing how easy it is to do common tasks
in scientific computing using just a few core tools: the python
standard library, numpy, matplotlib, scipy and the ipython shell.


Before proceeding, make sure you can fire up ipython in
:ref:`ipython_pylab` and navigate to the :ref:`sample_data`.

Loading and plotting some data
-------------------------------

One of the first and most common tasks in scientific computing is
loading, visualizing, and analyzing simple plain text files located on
your computer.  The simplest file format is all numeric -- no dates,
strings, headers, comments or other pesky details to worry about.
numpy provides ``loadtxt`` for loading simple data files (and not so simple
data as we will see below) returning the result as a numpy array.  The
:ref:`sample_data` directory contains a :file:`bodyfat.dat` text file
containing body fat measurements from a group of men, and other meta
data as well; the associated :file:`bodyfat_readme.txt` file describes
this file in more detail.  Let's navigate to the file in the sample
data directory in ipython and take a peak

.. sourcecode:: ipython

  In [13]: cd bookdata/
  /home/titan/johnh/py4science/book/bookdata

  In [14]: ls bodyfat*
  bodyfat.dat          bodyfat_readme.txt


  In [15]: !more bodyfat.dat
    1.0708    12.3      23  154.25   67.75    36.2    ...
    1.0853     6.1      22  173.25   72.25    38.5    ...
    1.0414    25.3      22  154.00   66.25    34.0    ...

In the example below, there are several columns more in the output you
should see that have been elided in this document so as to not
overflow the line.  ``!more bodyfat.dat`` takes advantage of a very
handy IPython feature: the ability to make system calls (not python
calls) by prefixing the input line with the exclamation point.  We can
now load this file into ipython using ``np.loadtxt``.

.. sourcecode:: ipython

   In [20]: import numpy as np

   In [21]: X = np.loadtxt('bodyfat.dat')

   In [22]: print X
   [[  1.0708  12.3     23.     ...,  32.      27.4     17.1   ]
    [  1.0853   6.1     22.     ...,  30.5     28.9     18.2   ]
    [  1.0414  25.3     22.     ...,  28.8     25.2     16.6   ]
    ...,
    [  1.0328  29.3     72.     ...,  31.3     27.2     18.    ]
    [  1.0399  26.      72.     ...,  30.5     29.4     19.8   ]
    [  1.0271  31.9     74.     ...,  33.7     30.      20.9   ]]

Here the ``...`` elipses were added by numpy in the print out so as to
not dump too much information to your screen.  The tabular data,
numbers organized into rows and columns, has been put into a two
dimensional array of numpy floating point numbers.   We can peak into
the array to get more information about the array, for example, the
shape (number of rows by number of columns) and the type of the data.


.. sourcecode:: ipython

   In [25]: print X.shape
   (252, 15)

   In [26]: print X.dtype
   float64

These attributes will be covered in detail in the upcoming chapter
:ref:`numpy_intro`.

From the :file:`bodyfat_readme.dat`, we see the columns of this file
represent the following fields::

  Density determined from underwater weighing
  Percent body fat from Siri's (1956) equation
  Age (years)
  Weight (lbs)
  Height (inches)
  Neck circumference (cm)
  Chest circumference (cm)
  Abdomen 2 circumference (cm)
  Hip circumference (cm)
  Thigh circumference (cm)
  Knee circumference (cm)
  Ankle circumference (cm)
  Biceps (extended) circumference (cm)
  Forearm circumference (cm)
  Wrist circumference (cm)


We want to extract the percentage of body fat (the second column) and the age
(the third column), and make a plot of age on the x-axis and body fat
on the y-axis.  Since python indexing starts with 0 not 1, the second
column is indexed with ``1`` and the third column is indexed with
``2``.

.. sourcecode:: ipython

   In [31]: fat = X[:,1]

   In [32]: age = X[:,2]

   In [33]: print fat[:4]
   [ 12.3   6.1  25.3  10.4]

   In [34]: print age[:4]
   [ 23.  22.  22.  26.]

numpy supports a wide range of indexing options to slice out columns
and rows from a larger array -- here we assign the name ``fat`` to the
2nd column, ``age`` to the third column, and then print the first four
elements of each to make sure they look right.  We see the ``fat``
variable, which is the percentage of body fat, with representative
numbers like 12.3 and 6.1, and the ``age`` variable with
representative numbers like 23 and 22, so this looks like we have
loaded and extracted the data properly.  We'll make a quick graph,
estimate the best fit regression line using ``np.polyfit``, and plot
the regression line and the scatter points (the semi-colon at the end
of some of the lines below tells IPython not to print the output).


.. sourcecode:: ipython

   In [35]: plot(age, fat, 'o');

   In [36]: title('body fat density by age');

   In [37]: xlabel('age');

   In [38]: ylabel('body fat percentage');

   In [39]: grid()

   In [42]: pars = np.polyfit(age, fat, 1)

   In [43]: x = [age.min(), age.max()]

   In [44]: y = np.polyval(pars, x)

   In [45]: plot(x, y, '-', lw=2, color='red');


.. plot::

   import numpy as np
   import matplotlib.pyplot as plt

   X = np.loadtxt('bookdata/bodyfat.dat')
   fat = X[:,1]
   age = X[:,2]
   fig = plt.figure()
   ax = fig.add_subplot(111)

   # make the basic scatter
   ax.plot(age, fat, 'o')
   ax.set_title('body fat density by age')
   ax.set_xlabel('age')
   ax.set_ylabel('body fat percentage')
   ax.grid()

   # now add the regression line
   pars = np.polyfit(age, fat, 1)
   x = [age.min(), age.max()]
   y = np.polyval(pars, x)
   ax.plot(x, y, '-', lw=2, color='red')



TODO