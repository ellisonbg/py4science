.. _whirlwind_tour:

==============
Whirlwind tour
==============

There is an enormous breadth and depth of packages supporting
scientific computing in python -- the packages in scipy alone could
fill several books worth of documentation -- and we will dive into
this material in some depth in chapters to come.  Before going deep
though, we'd like to start showing how easy it is to do common tasks
in scientific computing using just a few core tools: the python
standard library, numpy, matplotlib, scipy and the ipython shell.


Before proceeding, make sure you can fire up ipython in pylab mode
(:ref:`matplotlib_getting_started`) and navigate to the :ref:`sample_data`.


.. _loadtxt_demo:

Loading and plotting some data
-------------------------------

One of the first and most common tasks in scientific computing is
loading, visualizing, and analyzing simple plain text files located on
your computer.  The simplest file format is all numeric -- no dates,
strings, headers, comments or other pesky details to worry about.
numpy provides `np.loadtxt
<http://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html>`_
for loading simple data files (and not so simple data as we will see
below) returning the result as a numpy array.  The :ref:`sample_data`
directory contains a :file:`bodyfat.dat` text file containing body fat
measurements from a group of men, and other meta data as well; the
associated :file:`bodyfat_readme.txt` file describes this file in more
detail.  Let's navigate to the file in the sample data directory in
ipython and take a peak

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

   In [38]: import numpy as np

   In [39]: X = np.loadtxt('bodyfat.dat')

   In [40]: X
   Out[40]:
   array([[  1.0708,  12.3   ,  23.    , ...,  32.    ,  27.4   ,  17.1   ],
	  [  1.0853,   6.1   ,  22.    , ...,  30.5   ,  28.9   ,  18.2   ],
	  [  1.0414,  25.3   ,  22.    , ...,  28.8   ,  25.2   ,  16.6   ],
	  ...,
	  [  1.0328,  29.3   ,  72.    , ...,  31.3   ,  27.2   ,  18.    ],
	  [  1.0399,  26.    ,  72.    , ...,  30.5   ,  29.4   ,  19.8   ],
	  [  1.0271,  31.9   ,  74.    , ...,  33.7   ,  30.    ,  20.9   ]])


Here the ``...`` ellipses were added by numpy in the print out so as to
not dump too much information to your screen.  The tabular data,
numbers organized into rows and columns, has been put into a two
dimensional array of numpy floating point numbers.   We can peak into
the array to get more information about the array, for example, the
shape (number of rows by number of columns) and the type of the data.


.. sourcecode:: ipython

   In [41]: X.shape
   Out[41]: (252, 15)

   In [42]: X.dtype
   Out[42]: dtype('float64')

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

   In [46]: fat = X[:,1]

   In [47]: age = X[:,2]

   In [48]: fat[:4]
   Out[48]: array([ 12.3,   6.1,  25.3,  10.4])

   In [49]: age[:4]
   Out[49]: array([ 23.,  22.,  22.,  26.])

numpy supports a wide range of indexing options to slice out columns
and rows from a larger array -- here we assign the name ``fat`` to the
2nd column, ``age`` to the third column, and then print the first four
elements of each to make sure they look right.  In indexing arrays,
the syntax is *X[ROWINDEX,COLINDEX]* and the colon in the indexing
``X[:,1]`` means take all of the rows, a syntax probably familiar to
Matlab users.  So ``X[:,1]`` means *take all the rows and just the 2nd
column*.

We inspect the first four elements of the ``fat`` variable with
``fat[:4]``, which is the percentage of body fat, with representative
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



To compute the regression line, you can use the numpy ``np.polyfit``
function to find the polynomial that is the best fit to your data in a
least-squared sense.  The argument ``1`` to polyfit indicates a linear
fit.  The parameters ``pars`` in the example are the slope and
intercept of the best-fit line


.. sourcecode:: ipython

   In [48]: pars
   Out[48]: array([  0.19355121,  10.46326299])


For higher order polynomial fits like quadratic or cubic, use orders
``2`` or ``3``.  For much more sophisticated parametric modeling, see
the tools in ``scipy.optimize``.


Another common need is to plot the best-fit Gaussian density along
with a histogram of your data.  Let's plot the probability density
function of the body fat percentage data.  To compute the best-fit
Gaussian, we just need to estimate the mean and standard deviation
from the actual data; for other statistical distributions estimating
the best-fit is trickier and requires the tools in ``scipy.stats``.
We can see that the data is not really normally distributed, but we'll
put on our "typical scientist" hat and try to shoe-horn a normal
distribution onto it anyhow.

.. sourcecode:: ipython

   # the matplotlib hist function will plot the empirical
   # probability density function when passed normed=True
   In [382]: hist(fat, 20, normed=True);

   # the mean and standard deviation are used to compute the
   # analytical best-fit Gaussian density
   In [383]: mu = fat.mean()

   In [384]: sigma = fat.std()

   In [385]: x = linspace(fat.min(), fat.max(), 100)

   # you can use scipy.stats to get the pdf of the normal distribution,
   # but here we'll just show off numpy's array abilities
   In [386]: y = 1/(sqrt(2*pi)*sigma)*exp(-0.5 * (1/sigma*(x - mu))**2)

   In [387]: plot(x, y, 'r-', lw=2);
   In [388]: grid()

   # we can decorate the plot with some text
   In [389]: xlabel('body fat percent');

   In [390]: ylabel('prob density');

   In [391]: mu
   Out[391]: 19.150793650793652

   In [392]: sigma
   Out[392]: 8.3521192637267365

   # matplotlib supports a wide subset of TeX math expressions
   In [393]: text(1.0, 0.045, r'$\mu=1.05, \sigma=0.019$', fontsize=18);

.. plot::

   import numpy as np
   import matplotlib.pyplot as plt

   X = np.loadtxt('bookdata/bodyfat.dat')
   fat = X[:,1]

   fig = plt.figure()
   ax = fig.add_subplot(111)
   ax.hist(fat, 20, normed=True)

   mu = fat.mean()
   sigma = fat.std()
   x = np.linspace(fat.min(), fat.max(), 100)
   y = 1/(np.sqrt(2*np.pi)*sigma)*np.exp(-0.5 * (1/sigma*(x - mu))**2)
   ax.plot(x, y, 'r-', lw=2)
   ax.grid(True)
   ax.set_xlabel('body fat percent')
   ax.set_ylabel('prob density')
   ax.text(1.0, 0.045, r'$\mu=1.05, \sigma=0.019$', fontsize=18)
   plt.show()

In the last ``text`` command, we passed in a TeX expression using the
standard math syntax with the enclosing dollar signs.  matplotlib
ships with a TeX math parsing engine which uses the small and elegant
`pyparsing <http://pyparsing.wikispaces.com/>`_ module to parse a
large subset of TeX mathematical expressions.  In addition,
`matplotlib.mathtext
<http://matplotlib.sourceforge.net/api/mathtext_api.html>`_ implements
the Knuth layout algorithms, and ships a complete set of math fonts
including the freetype version of the TeX `computer modern
<http://en.wikipedia.org/wiki/Computer_Modern>`_ fonts, so matplotlib
can parse and render mathematical expressions on any computer on which
it is installed, regardless of whether there is a TeX distribution
installed, with output supported not only on raster screen displays
and PNG outputs, but to PS, PDF and SVG outputs as well.  In addition,
matplotlib can call out to TeX installations if they are available, in
case you need access to features that may not be implemented in
matplotlib (for example, equation arrays) or simply want maximum
layout and font compatibility for figures inserted into your LaTeX
documents.


.. _stock_demo:

Working with richer data and files
------------------------------------

In the simple body fat example above, we used ``np.loadtxt`` to import
data from one of the simplest formats available: a plain text file
living on your computer with no headers, comments or non-numeric data.
numpy is exceedingly good at handling this data, seamlessly importing
it into a 2D homogeneous array of floating point numbers (notice the
dtype "datatype" of ``float64`` in the array ``X`` above, indicating
an 8byte/64bit floating point number).  Real word data is much more
varied, composed of strings, dates, integers, complex numbers, and
more, and is scattered across filesystems, databases, and the
internet.  Python, with its "batteries included" philosophy, is fully
equipped to work with that data.

A typical example of the kind of data you see in real-world
application is daily stock price data, which is a mix of dates,
floating point numbers and integers.  Take a look at the "Yahoo
Finance" `historical price data
<http://finance.yahoo.com/q/hp?s=CROX>`_ for the Crocs company (ticker
CROX).  At the bottom of this Yahoo page, there is a "Download to
Spreadsheet" to download the CSV file to your computer; manually
clicking works fine for one or two stocks, but if you want to analyze
hundreds, or automate daily analyses, you will need to be able to
fetch this data automatically from your Python program.  It's easy
with the built-in `urllib
<http://docs.python.org/library/urllib.html>`_ library for working
with internet data: the function `urllib.urlretrieve
<http://docs.python.org/library/urllib.html#urllib.urlretrieve>`_ can
fetch a remote file.

First copy the URL from Yahoo Finance historical prices page by right
clicking on the "Download to Spreadsheet" link at the bottom of the
page and choosing "Copy Link Location", and then paste the URL link
into your ipython session and name it "url"


.. sourcecode:: ipython

   In [59]: url = 'http://ichart.finance.yahoo.com/table.csv?s=CROX\
      ....: &d=9&e=22&f=2009&g=d&a=1&b=8&c=2006&ignore=.csv'

   In [60]: import urllib

   # fname is the filename of the file downloaded to your system, a
   # temporary file created by urllib
   In [61]: fname, msg = urllib.urlretrieve(url)

   In [62]: fname
   Out[62]: '/tmp/tmpMXW2Gn.csv'


By default ``urlretrieve`` will create a temporary file somewhere on
your system and download the file, so your location and file name will
be different.  We can inspect the file contents in IPython.

.. sourcecode:: ipython

   In [67]: !more /tmp/tmpMXW2Gn.csv
   Date,Open,High,Low,Close,Volume,Adj Close
   2009-10-22,7.27,7.89,7.27,7.77,2960100,7.77
   2009-10-21,7.58,7.84,7.25,7.30,2686100,7.30
   2009-10-20,7.91,7.98,7.52,7.63,2256900,7.63
   2009-10-19,7.82,8.00,7.74,7.89,3040800,7.89
   2009-10-16,7.90,7.94,7.60,7.76,2403100,7.76

This file has headers (*Date,Open,High,Low,Close,Volume,Adj Close*)
and heterogeneous types: dates, floating point numbers, and integers.
Of course in the file, these are just lines of text, but they are
naturally represented in a typed language like python with
``datetime.date``, ``float`` and ``int``.  The other important
difference between this file and the ``bodyfat.dat`` file above is the
use of a comma as the field delimiter.  ``np.loadtxt`` has support for
converters to covert strings to arbitrary types, and can
heterogeneous datatypes, but it can be cumbersome to set up (we will
cover this in :ref:`numpy_intro`).  For loading CSV files that "just
works" out of the box, `matplotlib.mlab
<http://matplotlib.sourceforge.net/api/mlab_api.html>`_ provides
`csv2rec
<http://matplotlib.sourceforge.net/api/mlab_api.html#matplotlib.mlab.csv2rec>`_
for automatically parsing headers, inspecting the data to guess the
type, and then converting it and loading it into a numpy record array.


.. sourcecode:: ipython

   In [73]: import matplotlib.mlab as mlab

   In [74]: r = mlab.csv2rec(fname)

   In [75]: r.dtype
   Out[75]: dtype([('date', '|O4'), ('open', '<f8'), ('high', '<f8'),
		('low', '<f8'), ('close', '<f8'), ('volume', '<i4'),
		('adj_close', '<f8')])


``r`` in the example above is a numpy record array, which supports a
tabular view of data much like a spreadsheet or SQL table, but is
actually even more flexible than this.  The `dtype
<http://docs.scipy.org/doc/numpy/reference/generated/numpy.dtype.html>`_,
describes the datatype of the record array, and here associates the
names of the fields *date*, *open*, *volume*, etc with the types
``|O4``, ``<f8``, ``<i4`` meaning "4 byte python object", "little
endian 8 byte float" and "little endian 4 byte integer" (endianess is
the byte ordering used to represent the data and varies across
different computing architectures).

In the printed record array above, we see that the values are
*decreasing* over the rows (most recent date is first), and normally
we think of this data *increasing* in time.  To sort a record array,
just call the sort method, which will sort over the first column by
default (you can pass in the *order* keyword argument to ``sort`` to
sort over a different field).

.. sourcecode:: ipython

   In [80]: r.sort()

   In [81]: print(mlab.rec2txt(r[:5]))
   date           open     high      low    close     volume   adj_close
   2006-02-08   30.000   32.500   28.140   28.550   23814000      14.270
   2006-02-09   29.240   29.340   26.120   27.000    4463800      13.500
   2006-02-10   27.000   27.540   26.020   26.550    1800400      13.270
   2006-02-13   26.500   28.250   26.390   27.700    1701800      13.850
   2006-02-14   27.750   28.470   27.750   27.800    2553800      13.900


In the body fat example above, we extracted the columns for age and
fat by using integer column indices into the array.  This works fine,
but becomes tedious when trying to keep track of a large number of
columns.  One of the beauties of the named dtypes in record arrays is
that you can access the named columns of your data.  For example, to
work with the date column, we can refer to ``r.date`` and even call
python `datetime.date <http://docs.python.org/library/datetime.html>`_
methods on the dates stored in the array.

.. sourcecode:: ipython

   In [89]: r.date[:4]
   Out[89]: array([2006-02-08, 2006-02-09, 2006-02-10, 2006-02-13], dtype=object)

   In [90]: date0 = r.date[0]

   In [91]: date0
   Out[91]: datetime.date(2006, 2, 8)

   In [92]: date0.year
   Out[92]: 2006

With record arrays, the dictionary-like syntax is also supported using
the column names as string keys, eg we can access the date column
with ``r['date']``.

We can see how an investment in CROX has fared over the past few years
by plotting the price history.

.. sourcecode:: ipython

   In [93]: plot(r.date, r.adj_close)
   Out[93]: [<matplotlib.lines.Line2D object at 0x8eb398c>]

   In [94]: title('CROX share price - split adjusted')
   Out[94]: <matplotlib.text.Text object at 0x8dde1ac>

   In [95]: gcf().autofmt_xdate()

   In [96]: draw()

.. plot::

   import matplotlib.pyplot as plt
   import matplotlib.mlab as mlab
   fig = plt.figure()
   ax = fig.add_subplot(111)
   r = mlab.csv2rec('bookdata/crox.csv')
   ax.plot(r.date, r.adj_close)
   ax.set_title('CROX share price - split adjusted')
   fig.autofmt_xdate()
   plt.show()

A couple of comments about the last two lines.  Date tick labels can
be quite long, and can tend to overlap.  The matplotlib ``Figure`` has
a method `autofmt_xdate
<http://matplotlib.sourceforge.net/api/figure_api.html#matplotlib.figure.Figure.autofmt_xdate>`_
to do a few formatting operations that are common on date plots, and
one of these is to rotate the ticklabels so that they will not
overlap.  Much, but not all of the matplotlib functionality, which
resides in an object oriented class library, is accessible in the
pylab interface via simple function like ``title`` and ``plot``.  To
get at the rest of the functionality, we need to delve into the
matplotlib API, and the call ``gcf().autofmt_xdate()`` uses ``gcf`` to
*get current figure* and then call the figure's ``autofmt_xdate``
method.  If you are typing along with the example, you may have
noticed that the figure was not redrawn after the call to
``autofmt_xdate``: this is a design decision in matplotlib to only
automatically update the figure when pyplot plotting functions are
called, and otherwise defer drawing until explicitly asked to in a draw
commands.  Since ``autofmt_xdate`` is an *API* command, not a *pyplot*
command, it did not automatically trigger a redraw.


Numpy arrays are extremely flexible and powerful data structures.  In
the example below, we analyze the dollar trading volume in CROX -- the
*dollar trading volume* is closely approximated by the product of the
volume of shares traded (the *volume* field) times the price of the
shares, given by the *close*.  We can easily compute the average daily
trading volume, the average over the most recent forty trading days, the
largest day ever, the date of the largest day, the standard deviation
of the trading volume, etc...


.. sourcecode:: ipython

   # dv is the dollar volume traded; it is an *array* of daily dollar
   # volumes
   In [101]: dv = r.volume * r.close

   # the average and standard deviation of dv
   In [102]: dv.mean()
   Out[102]: 131809256.93676312

   In [103]: dv.std()
   Out[103]: 222149688.4737061

   # the average in the most recent 40 trading days
   In [104]: dv[-40:].mean()
   Out[104]: 66807846.700000003

   # the largest trading volume ever
   In [105]: dv.max()
   Out[105]: 2887587318.0

   # the index into dv where the largest day occurs
   In [106]: dv.argmax()
   Out[106]: 496

   # the date of the largest day
   In [107]: r.date[496]
   Out[107]: datetime.date(2007, 11, 1)


.. _wordcount_demo:

Dictionaries for counting words
-------------------------------

It's not just numerical computing at which Python excels.  While much
of your time doing scientific computing in Python will be spent in the
core extension packages that provide fast arrays, statistics and
visualization, a strong advantage that Python has over many
alternatives for scientific computing is that Python is a full blown
object oriented language with rich data structures, built in
libraries, and support for multiple programming paradigms.  We'll take
a break from crunching numbers to illustrate python's power in string
processing, utilizing one of the essential data structures: the
dictionary.

A common task in text processing is to produce a count of word frequencies.
While numpy has a built in histogram function for doing numerical histograms,
it won't work out of the box for counting discrete items, since it
is a binning histogram for a range of real values.

But the Python language provides powerful string manipulation
capabilities, as well as a flexible and efficiently implemented built
in data type, the *dictionary*, that makes this task a simple one.
The example below counts the frequencies of all the words contained in
a compressed text file of *Alice's Adventures in Wonderland* by Lewis
Carroll, downloaded from `Project Gutenberg
<http://www.gutenberg.org/wiki/Main_Page>`_.

.. figure:: _static/alice_chapter1.jpg
   :width: 4in

   Facsimile from `Chapter 1 <http://www.gutenberg.org/files/19002/19002-h/19002-h.htm>`_ of Project Gutenberg Alice in Wonderland

We'll define "words" to simply be the result of splitting the input
text into a list, using any form of white-space as a separator. This
is obviously a very naive definition of word, but it will suffice for
the purposes of this example.  Python strings have a ``split()``
method that allows for very flexible splitting. You can easily get
more details on it in IPython using the built-in help:

.. sourcecode:: ipython

   In [70]: a = 'some string'

   In [71]: a.split?

   Type:           builtin_function_or_method
   Base Class:     <type 'builtin_function_or_method'>
   String Form:    <built-in method split of str object at 0x98e2548>
   Namespace:      Interactive
   Docstring:
       S.split([sep [,maxsplit]]) -> list of strings

       Return a list of the words in the string S, using sep as the
       delimiter string.  If maxsplit is given, at most maxsplit
       splits are done. If sep is not specified or is None, any
       whitespace string is a separator.


   In [72]: a.split()
   Out[72]: ['some', 'string']

The complete set of methods of Python strings can be viewed by typing
``a.<TAB>``

.. sourcecode:: ipython

   In [73]: a.
   a.__add__          a.__init__      a.__setattr__ a.isdigit a.rsplit
   a.__class__        a.__le__        a.__str__     a.islower a.rstrip
   a.__contains__     a.__len__       a.capitalize  a.isspace a.split
   a.__delattr__      a.__lt__        a.center      a.istitle a.splitlines
   a.__doc__          a.__mod__       a.count       a.isupper a.startswith
   a.__eq__           a.__mul__       a.decode      a.join    a.strip
   a.__ge__           a.__ne__        a.encode      a.ljust   a.swapcase
   a.__getattribute__ a.__new__       a.endswith    a.lower   a.title
   a.__getitem__      a.__reduce__    a.expandtabs  a.lstrip  a.translate
   a.__getnewargs__   a.__reduce_ex__ a.find        a.replace a.upper
   a.__getslice__     a.__repr__      a.index       a.rfind   a.zfill
   a.__gt__           a.__rmod__      a.isalnum     a.rindex
   a.__hash__         a.__rmul__      a.isalpha     a.rjust


Each of them can be queried similarly with the ``'?'`` operator as
above.  For more details on Python strings and their companion
sequence types, see `string methods
<http://docs.python.org/library/stdtypes.html#string-methods>`_

Back to Alice.  We want to read the text in from the zip file, split
it into words and then count the frequency of each word.  You will
need to read the compressed file
:file:`bookdata/alice_in_wonderland.zip` from the
:ref:`sample_data`. Python has facilities to do this with the `zipfile
<http://docs.python.org/library/zipfile.html>`_ module, which avoids
having to first uncompress and unzip the file.  The zip file consists
of one or more files, and we can use the module to load the zip file,
list the files, and then read the text from the one file in the zip
archive

.. sourcecode:: ipython

   In [101]: import zipfile

   In [102]: zf = zipfile.ZipFile('alice_in_wonderland.zip')

   In [103]: zf.namelist()
   Out[103]: ['28885.txt']

   In [104]: text = zf.read('28885.txt')


Be careful printing ``text`` -- it is the entire manuscript so it will
dump a lot of text to your screen.  We can print the characters from
2000:2400 using standard slicing

.. sourcecode:: ipython

   In [106]: print text[2000:2400]
	  The rags of RIP VAN WINKLE!_

				      _AUSTIN DOBSON._



	     All in the golden afternoon
	       Full leisurely we glide;
	     For both our oars, with little skill,
	       By little arms are plied,
	     While little hands make vain pretence
	       Our wanderings to guide.

	     Ah, cruel Three! In such an hour,


We can split the raw text into a list of words using the ``split``
method as described above.  To ignore casing difference, we will
convert every word to lower case

.. sourcecode:: ipython

   In [107]: words = [word.lower() for word in text.split()]

   In [108]: len(words)
   30359

   In [109]: print words[:10]
   ['project', "gutenberg's", "alice's", 'adventures', 'in', 'wonderland,',
     'by', 'lewis', 'carroll', 'this']



Now we have all the pieces in place to implement our work counting
algorithm.  We use a dictionary ``countd`` (mnemonic "count
dictionary") which maps words to counts.  The key trick is to use the
dictionary's ``get`` method, which will return the dictionary value
if it exists, otherwise it will return the specified default value.

.. sourcecode:: ipython

   In [1]: countd = dict()

   In [2]: countd['alice'] = 10

   In [3]: countd.get('alice', 0)
   10

   In [4]: countd.get('wonderland', 0)
   0



In this example, calling ``countd.get('alice', 0)`` returns ``10``
because the key ``'alice'`` is in the dictionary with value ``10``. But
``countd.get('wonderland', 0)`` returns the default value ``0``
because the key ``'wonderland'`` is not in the dictionary.  This idiom
is useful when doing word counts because when we encounter a word that
may or may not already be in our ``countd`` dictionary, we can use
``get`` to return the count with a default value of ``0``.  For each
word in our word list, we increment the count for the word by ``1``,
assuming a default starting count for ``0`` if it is the first time we see
the word and it is not in our ``countd`` dictionary


.. sourcecode:: ipython

   In [16]: countd = dict()

   In [17]: for word in words:
      ....:     countd[word] = countd.get(word, 0) + 1
      ....:
      ....:


We can now inspect the dictionary for individual words to see how
frequently they occur

.. sourcecode:: ipython

   In [18]: countd['alice']
   226

   In [19]: countd['wonderland']
   5

To finish up this example, we want to print the most common occurring
words.  The easiest way to do this is create a list of (*count*,
*word*) tuples, and then sort the list.  So we will create a list of
2-tuples.  Python will sort this according to the first element of the
tuple -- the *count* -- and for identical counts will sort by the second
element of the tuple -- the *word*.  The dictionary method ``items``
returns a list of (*key*, *value*) pairs, ie (*word*, *count*), so we
need to reverse this to get (*count*, *word*) pairs

.. sourcecode:: ipython

   In [103]: counts = [(count, word) for word, count in countd.items()]

   In [104]: counts[:3]
   Out[104]: [(2, '"--and'), (1, 'figure!"'), (6, 'four')]

You will probably see different number/word pairs because dictionaries
are unordered and the return value from ``items`` is unordered.  We can
do an in-place sort of the list, and then index into the last elements
of the sorted list using the negative index to see the most common
words and their counts

.. sourcecode:: ipython

   In [115]: counts.sort()

   # the least common words
   In [116]: counts[:6]
   Out[116]:
   [(1, '"\'--found'),
    (1, '"\'_we'),
    (1, '"\'miss'),
    (1, '"----'),
    (1, '"----likely'),
    (1, '"----or')]

   # the most common words
   In [117]: counts[-6:]
   Out[117]:
   [(522, 'she'),
    (619, 'of'),
    (689, 'a'),
    (803, 'to'),
    (857, 'and'),
    (1812, 'the')]

Of course, this is just a toy example, and we have not cleaned the
word data by stripping off punctuation, but it does show off some of
the versatile data structures and standard library functionality that
makes these tasks easy and elegant in python.

Let's take the example one step further to strip the words of all
non-alphabetic characters.  We can use the regular expression ``re``
module to strip all non-word characters.  In regular expression
syntax, ``'[^a-z]'`` mean *any character except a through z*.  We will
use the regular expression ``sub`` method to replace the non-word
characters with the empty string, thus stripping all non-word
characters from the string

.. sourcecode:: ipython

   In [32]: import re

   In [33]: rgx = re.compile('[^a-z]')

   In [34]: word = "can't123"

   In [35]: rgx.sub('', word)
   Out[35]: 'cant'


.. comment:

  skip this for now, maybe illustrate translate later but the rgx code
  is much cleaner and suitable for the whirlwind

  There are two string methods that help
  here: ``translate`` and ``isalpha``.  The ``translate`` method is used
  to translate certain string characters into other characters, but it
  has an optional second argument which is a string of characters you
  want to delete.  So we need to build a string which is all of the
  characters *except* the alphabetic characters.  The ASCII character
  set are the characters represented by the ordinal numbers from 0..255
  .. sourcecode:: ipython

     In [123]: ascii_chars = [chr(i) for i in range(256)]

  The ``isalpha`` method will return True if the character is a member
  of the alphabet, so we want to filter the character list for the
  ``isalpha`` characters, and then convert the *list* of non-alphabetic
  characters to a *string*, since this is what the ``translate`` method
  requires

  .. sourcecode:: ipython

    # a list of non-alphabetic ASCII characters
    In [137]: nonalpha_chars = [chr(i) for i in range(256)\
       .....: if not chr(i).isalpha()]

    # convert the list of non-alpha character to a string
    In [138]: nonalpha_str = ''.join(nonalpha_chars)

    # this function strips all non-alpha chars from a word
    In [139]: def strip_nonalpha(word):
       .....:     return word.translate(None, nonalpha_str)
       .....:

    In [140]: word = "Can't!"

    In [141]: strip_nonalpha(word.lower())
    Out[141]: 'cant'

Here is the entirety of the script, which reads the zip file,
lowercases and cleans the words of non-alphabetic characters, counts
the words, and prints the least and most common ones -- all in 13
lines of code!

.. sourcecode:: python

   import zipfile, re
   zf = zipfile.ZipFile('alice_in_wonderland.zip')
   text = zf.read('28885.txt')

   words = [word.lower() for word in text.split()]

   rgx = re.compile('[^a-z]')
   countd = dict()

   for word in words:
       word = rgx.sub('', word)
       countd[word] = countd.get(word, 0) + 1

   counts = [(count, word) for word, count in countd.items()]
   counts.sort()

   print('Least common:\n%s'%counts[:6])
   print('Most common:\n%s'%counts[-6:])


.. _image_processing:

Image processing
--------------------

The examples so far have been lightweight explorations of simple data
sets using descriptive statistics.  Here we take on a more meaty
topic: filtering an image to remove noisy artifacts.

.. sourcecode:: ipython

   In [192]: cd bookdata/
   /home/jdhunter/py4science/book/bookdata

   In [193]: X = imread('moonlanding.png')

   In [194]: X.shape
   Out[194]: (474, 630)

   In [195]: imshow(X, cmap='gray')
   Out[195]: <matplotlib.image.AxesImage object at 0x97d1acc>


.. plot::

   import matplotlib.image as mimage
   import matplotlib.pyplot as plt
   X = mimage.imread('bookdata/moonlanding.png')

   fig = plt.figure()
   ax = fig.add_subplot(111)
   ax.imshow(X, cmap='gray')
   plt.show()


The image is a grayscale photo of the moon landing, but there is a
banded pattern of high frequency noise polluting the image.  Our goal
is to filter out that noise to crispen up the image.

A linear filter implemented via convolution of an input with with a
response function in the temporal or spatial domain is equivalent to
multiplication by the Fourier transform of the input and the filter in
the spectral domain.  This provides a conceptually simple way to think
about filtering: transform your signal into the frequency domain via
``np.fft.fft2``, dampen the frequencies you are not interested in by
multiplying the frequency spectrum by the desired weights (zero in the
simplest case), and then apply the inverse transform ``np.fft.ifft2``
to the modified spectrum to create the filtered image in the original
domain.

First we need to take the 2D FFT of the image data to compute the
spatial frequencies.

.. sourcecode:: ipython

   In [197]: F = np.fft.fft2(X)

   # the FFT of of a 2D real array is a 2D complex array of the same
   # shape as the original data
   In [198]: F.dtype
   Out[198]: dtype('complex128')

   In [199]: F.shape
   Out[199]: (474, 630)

   # to estimate spectral power, which is a real quantity, we need to
   # take the absolute value
   In [200]: P = abs(F)

   In [201]: P.dtype
   Out[201]: dtype('float64')

.. comment:

   X = imread('moonlanding.png')
   imshow(X, cmap='gray')
   F = np.fft.fft2(X)
   P = abs(F)
   imshow(P, cmap=cm.Blues)
   axis([500, 510, 120, 130])
   figure()
   imshow(P, cmap=cm.Blues)
   clim(0, 300)
   Fc = F.copy()
   Fc[50:-50, :] = 0.
   Fc[:, 50:-50] = 0.
   figure()
   imshow(abs(Fc), cmap=cm.Blues)
   clim(0, 300)
   figure()
   Xf = np.fft.ifft2(Fc).real
   imshow(Xf, cmap=cm.gray)

If you attempt to plot the spectrum using the colormap ``cm.Blues``, you
will just see a sea of white.

.. sourcecode:: ipython

   In [5]: imshow(P, cmap=cm.Blues)
   Out[5]: <matplotlib.image.AxesImage object at 0x9af988c>

.. plot::
   :width: 3in

   import numpy as np
   import matplotlib.image as mimage
   import matplotlib.cm as cm
   import matplotlib.pyplot as plt

   X = mimage.imread('bookdata/moonlanding.png')

   fig = plt.figure()
   ax = fig.add_subplot(111)
   F = np.fft.fft2(X)
   P = abs(F)
   ax.imshow(P, cmap=cm.Blues)
   plt.show()

But if you look very carefully, you will see that there are speckles
of blue variation; for example, if you zoom into the region between
500-510 on the x-axis and 120-130 on the y-axis, you will see a little
blob of blue in the sea of white.

.. sourcecode:: ipython

   In [13]: axis([500, 510, 120, 130])
   Out[13]: [500, 510, 120, 130]

.. plot::
   :width: 3in

   import numpy as np
   import matplotlib.image as mimage
   import matplotlib.cm as cm
   import matplotlib.pyplot as plt

   X = mimage.imread('bookdata/moonlanding.png')

   fig = plt.figure()
   ax = fig.add_subplot(111)
   F = np.fft.fft2(X)
   P = abs(F)
   ax.imshow(P, cmap=cm.Blues)
   ax.axis([500, 510, 120, 130])
   plt.show()


Here's what is happening: the spectral power image ``P`` is mainly
filled with regions of very small spectral power, punctuated by
regions of large high intensity bursts of noise.  The noisy high
intensity power is *much larger* than the bulk of the low intensity
power that is the real data in the image.  The colormapping in
matplotlib is linear, so it maps the lowest intensity to white and the
highest intensity to blue linearly when using the ``cm.Blues``
colormap.  To enhance the contrast in the image, we want to restrict
the mapping to the region of intensities over which most of our data
varies.  A simple solution here is to set the color limits to capture
the bulk of our data, say 99%, and then the colormapping will simply
clip the data above this threshold to the max value (dark blue).  We
can use the `matplotlib.mlab.prctile
<http://matplotlib.sourceforge.net/api/mlab_api.html#matplotlib.mlab.prctile>`_
function to find the 95% and 99% intensity values -- compare this to
the maximum value to see just how extreme the outliers are.

.. sourcecode:: ipython

   In [39]: import matplotlib.mlab as mlab

   In [40]: mlab.prctile(P, (95, 99))
   Out[40]: array([  121.09301642,   278.55832316])

   In [41]: P.max()
   Out[41]: 126598.45631306525


So the 99% threshold is 278.5.  We'll set the color limits to clip
above 300, a nice round number that is easier to type, to clip the
outliers.  First we'll clear the figure and then replot with the
clipped color limits using the `matplotlib.pyplot.clim
<http://matplotlib.sourceforge.net/api/pyplot_api.html#matplotlib.pyplot.clim>`_
function.

.. sourcecode:: ipython

   In [44]: clf()

   In [45]: imshow(P, cmap=cm.Blues)
   Out[45]: <matplotlib.image.AxesImage object at 0xa33ba0c>

   In [46]: clim(0, 300)


.. plot::
   :width: 3in

   import numpy as np
   import matplotlib.image as mimage
   import matplotlib.cm as cm
   import matplotlib.pyplot as plt

   X = mimage.imread('bookdata/moonlanding.png')

   fig = plt.figure()
   ax = fig.add_subplot(111)
   F = np.fft.fft2(X)
   P = abs(F)
   im = ax.imshow(P, cmap=cm.Blues)
   im.set_clim(0, 300)
   plt.show()

Now we finally have a good picture of the the 2D spatial frequency
spectrum. The spectrum in ``P`` is packed with the lower frequencies
starting in the upper left, proceeding to higher frequencies as one
moves to the center of the spectrum -- this is the most efficient way
numerically to fill the output of the FFT algorithm.  Because the
input signal is real, the output spectrum is complex and symmetric:
the transformation values beyond the midpoint of the frequency
spectrum (the Nyquist frequency) correspond to the values for negative
frequencies and are simply the mirror image of the positive
frequencies below the Nyquist.  This is true for the 1D, 2D and ND
FFTs in numpy.

So the smooth dark blue blobs in the corners show the low spatial
frequencies in the actual image that we want to preserve, and the dark
blue banded bursts of dark blue scattered throughout the middle are
the high frequency busts of noise we want to filter out.  We will
simply set the weights of the frequencies we are uninterested in --
the high frequency noise -- to zero rather than dampening them with a
smoothly varying function.  Although this is not usually the best
thing to do, since sharp edges in one domain usually introduce
artifacts in another -- eg high frequency *ringing* -- it is easy to
do and sometimes provides satisfactory results.

By visual inspection, we see that the "blobs" in the corner extend
about 50 pixels in the x and y directions.  We'll set everything in
the vast middle to zero.  It is important here that you set the zeros
on the Fourier transform array ``F`` rather than the power spectrum
array ``P``, because the complex values in the Fourier array have the
phase information we need to preserve the spatial structure in the
original image.  We'll make a copy of ``F`` first and store it as
``Fc``, in case we make a mistake or want to experiment with other
clipping values.


.. sourcecode:: ipython


   In [242]: Fc = F.copy()

   In [243]: Fc[50:-50,:] = 0.

   In [244]: Fc[:,50:-50] = 0.

   In [245]: imshow(abs(Fc), cmap=cm.Blues)
   Out[245]: <matplotlib.image.AxesImage object at 0xb1091cc>

   In [246]: clim(0, 300)


.. plot::
   :width: 3in

   import numpy as np
   import matplotlib.image as mimage
   import matplotlib.cm as cm
   import matplotlib.pyplot as plt

   X = mimage.imread('bookdata/moonlanding.png')

   fig = plt.figure()
   ax = fig.add_subplot(111)
   F = np.fft.fft2(X)
   P = abs(F)
   Fc = F.copy()
   Fc[50:-50,:] = 0.
   Fc[:,50:-50] = 0.
   im = ax.imshow(abs(Fc), cmap=cm.Blues)
   im.set_clim(0, 300)
   plt.show()

All that remains is to invert the FFT to bring the filtered spectrum
back into the spatial domain, and then plot the cleaned up image.  The
inverse transformed array will be complex, but the non-zero complex
parts are just noise due to floating point inaccuracy, so we want to
extract just the real part to recover the filtered image.

.. sourcecode:: ipython

   In [251]: Xf = np.fft.ifft2(Fc).real

   In [252]: imshow(Xf, cmap=cm.gray)
   Out[252]: <matplotlib.image.AxesImage object at 0xb1b476c>


.. plot::

   import numpy as np
   import matplotlib.image as mimage
   import matplotlib.cm as cm
   import matplotlib.pyplot as plt

   X = mimage.imread('bookdata/moonlanding.png')

   fig = plt.figure()
   ax = fig.add_subplot(111)
   F = np.fft.fft2(X)
   P = abs(F)
   Fc = F.copy()
   Fc[50:-50,:] = 0.
   Fc[:,50:-50] = 0.
   Xf = np.fft.ifft2(Fc).real
   im = ax.imshow(Xf, cmap=cm.gray)
   plt.show()

Below is the complete example, coded as we would using the matplotlib
API which is more robust for scripts.

.. plot::
   :include-source:

   import numpy as np
   import matplotlib.image as mimage
   import matplotlib.cm as cm
   import matplotlib.pyplot as plt

   X = mimage.imread('bookdata/moonlanding.png')
   Nr, Nc = X.shape

   # plot the original image
   fig = plt.figure()
   fig.subplots_adjust(hspace=0.1, wspace=0.1)
   ax1 = fig.add_subplot(221)
   ax1.set_title('image')
   ax1.set_ylabel('original')
   im1 = ax1.imshow(X, cmap=cm.gray)

   # the original spectrum
   ax2 = fig.add_subplot(222)
   ax2.set_title('spectrum')
   F = np.fft.fft2(X)
   im2 = ax2.imshow(abs(F), cmap=cm.Blues)
   im2.set_clim(0, 300)

   # set the high frequencies to zero and invert the transformation
   # to recover the filtered image
   Fc = F.copy()
   Fc[50:-50,:] = 0.
   Fc[:,50:-50] = 0.
   Xf = np.fft.ifft2(Fc).real

   # plot the filtered image
   ax3 = fig.add_subplot(223)
   ax3.set_ylabel('filtered')
   im3 = ax3.imshow(Xf, cmap=cm.gray)

   # plot the filtered spectrum
   ax4 = fig.add_subplot(224)
   im4 = ax4.imshow(abs(Fc), cmap=cm.Blues)
   im4.set_clim(0, 300)

   # turn off the x and y tick labels
   for ax in ax1, ax2, ax3, ax4:
       ax.set_xticks([])
       ax.set_yticks([])

   plt.show()



.. _lotka_volterra:

Foxes and Rabbits
--------------------

We've done a fair amount in the examples thus far: parsed data files,
fetched data from a web server, done some descriptive statistics and
regressions, plotted density functions and best-fit normal
distributions, parsed text, and denoised image data using Fourier
transforms, and we have yet to open the most powerful toolbox in
the python scientific computing arsenal: ``scipy``.  Like Matlab
before it, ``scipy`` at its core is a python wrapper around the
FORTRAN libraries that are the foundation of modern scientific
computing: LAPACK for linear algebra, UMFPACK for sparse linear
systems, ODEPACK for solving ordinary differential equations, ARPACK
for eigenvalue and eigenvector problems, MINPACK for optimization,
CDFLIB for statistical distributions and inverses, and much more.  In
addition to these FORTRAN wrappers, there are many packages in scipy
written in C and plain-ol-python for solving all kinds of tasks in
scientific computing, from reading Matlab files, to finding clusters
in data, to multi-dimensional image processing.



In this tour, will just scratch the surface and peak under the hood,
solving one of the classic problems in ordinary differential
equations: the dynamics of predator-prey interactions given by the
`Lotka-Volterra <http://en.wikipedia.org/wiki/Lotka%E2%80%93Volterra_equation>`_ equations.

The Lotka-Volterra equations are a system of two coupled nonlinear
ordinary differential equations used to describe the interactions
between species, a predator (the Foxes) and prey (the Rabbits).  They
were discovered independently by Alfred J Lotka, a US mathematician,
physical chemist and statistician and author of the first textbook on
mathematical biology *Elements of Mathematical Biology* in 1924, and
Vito Volterra, and Italian mathematician physicist.

The equation for the rabbits $R$ is

.. math::

  dR/dt = \alpha R - \beta R F

where $\alpha \geq 0$ and $\beta \geq 0$.  In words: the change in the
rabbit population over time is proportionate to the rabbit population,
and inversely proportionate to the product of the rabbit and fox
populations.  So if rabbits are left alone in the absence of foxes,
they will do what rabbits do best -- breed like rabbits -- and grow
unchecked.

The equation for the foxes $F$ is

.. math::

  dF/dt = \gamma R F - \delta F

where $\gamma \geq 0$ and $\delta \geq 0$.  In words: the change in
the fox population over time is proportionate to the product of
rabbits and foxes, and inversely proportionate to the fox population.
In the absence of rabbits, the foxes will have nothing to eat and die
off.  The equation is non-linear because of the interaction term $RF$.

Let's translate these equations into python.  In the examples above,
we've been working interactively from the ipython terminal, but we'll
shift here to working in a script because solving this equation will
require defining functions and doing work that is a bit more involved
than what we have been doing.  When working interactively at the
IPython shell, we are a bit fast and loose with namespaces, but when
writing scripts, which have permanence and which we'll likely revisit
later when the memory of our initial intents has faded, it is best to
be explicit about everything.  First we'll define a function
``derivs`` which implements the ODE equations for foxes and rabbits
above

.. sourcecode:: python

   # the parameters for rabbit and fox growth and interactions
   alpha, delta = 1, .25
   beta, gamma = .2, .05

   def derivs(state, t):
       """
       Return the derivatives of R and F, stored in the
       *state* vector::

	  state = [R, F]

       The return data should be [dR, dF] which are the
       derivatives of R and F at position *state* and time
       *t*.
       """
       R, F = state
       dR = alpha*R - beta*R*F
       dF = gamma*R*F - delta*F
       return dR, dF

This is a fairly nice example of *python as executable pseudo-code*,
since the python expressions for ``dR`` and ``dF`` are quite close to
the math expressions for $dR/dt$ and $dF/dt$.  The function ``derivs``
has a special syntax which is not necessarily intuitive, but will be
required for the ODE integration functions in ``scipy.integrate``.  In
particular, the first argument for an N-dimensional ODE is an N-length
state vector giving the current values of the variables being
integrated, in our case the populations of the rabbits and foxes, so
``state = [R, F]``.  The second argument, ``t`` for time, is required
by the integration interface but is not needed for our example since
the population dynamics do not explicitly depend on time.


Let's save this file as  :file:`lotka_volterra.py` and use the IPython
``run`` command to run it.  We can edit the script, run it, re-edit
and re-run as needed while we build out the example.

.. sourcecode:: ipython

   In [1]: ls
   lotka_volterra.py

   In [2]: !head -4 lotka_volterra.py
   # the parameters for rabbit and fox growth and interactions
   alpha, delta = 1, .25
   beta, gamma = .2, .05


   In [3]: alpha
   ---------------------------------------------------------
   NameError            Traceback (most recent call last)

   py4science/book/examples/<ipython console> in <module>()

   NameError: name 'alpha' is not defined

   In [4]: run lotka_volterra.py

   In [5]: alpha
   Out[5]: 1

   In [6]: help derivs
   ------> help(derivs)


``head`` on input line ``In [2]`` is a unix command to read the top of
the file -- if you are on Windows, it may not be available.  We're
just using it here to take a quick look at the file to make sure it is
the right one.  On line ``In [3]``, we try and print the value for
``alpha`` but get an error because it is not defined; this is
expected, because ``alpha`` is defined in the file
:file:`lotka_volterra.py` which has not been run yet.  When on input
line ``In [4]`` we run the file, the contents are executed and the
variables and functions there are brought into the local namespace,
where can inspect them, ask for help on the function, etc....

The first thing we want to do is numerically integrate the equations
using ``scipy.integrate.odeint``, which solves a system of ordinary
differential equations using LSODA from the FORTRAN library ODEPACK.
The function takes at a minimum three arguments

``func``
  A callable(y, t0, ...): computes the derivative of state vector y at
  time t0.

``y0``
  a length N initial condition array, where N is the number of
  dimensions of the system

``t``
  A sequence of time points for which to solve for y.  The initial
  value point should be the first element of this sequence.

In addition, you can pass in extra arguments to specify the gradient
(Jacobian) of the function, which improves performance and accuracy,
as well extra arguments specifying how much information to return, how
much to print out while running, and more which is covered in the
docstring.  But we'll be using the simple form, and we've already
defined the function required in ``derivs`` above, so all that is left
is to specify the initial condition and the times to be evaluated.

A reasonable estimate of the times over which to evaluate the
ODE is to pick a time long compared with the slowest time scale in
your system and a time-step short compared with the fastest time scale
in your system.  Since the rate constants $\alpha$, $\beta$, $\gamma$
and $\delta$ are in units of 1/time, the slowest time scale arises
from smallest rate constant $\gamma=0.05$ which is 20s, and the
fastest time scale arises from the largest rate constant $\alpha=1$
which is 1s.  So we want the time-step $dt$ to be small compared to 1s
and the integration time to be long compared to 20s; we'll choose 100s
for the integration time and 0.1s for the time-step.


.. sourcecode:: python

   import numpy as np
   import scipy.integrate as integrate

   # the initial population of rabbits and foxes
   R0 = 20
   F0 = 10

   # create a time array from 0..100 sampled at 0.1 second steps
   dt = 0.1
   t = np.arange(0.0, 100, dt)

   # the initial [rabbits, foxes] state vector
   y0 = [R0, F0]

   # y is a len(t)x2 2D array of rabbit and fox populations
   # over time
   y = integrate.odeint(derivs, y0, t)


We can extract the rabbits and foxes columns, and plot both over time

.. sourcecode:: python

   rabbits = y[:,0]
   foxes = y[:,1]
   fig = plt.figure()
   ax = fig.add_subplot(111)
   ax.plot(t, rabbits, label='rabbits')
   ax.plot(t, foxes, label='foxes')

   leg = ax.legend(loc='upper left', fancybox=True, shadow=True)
   leg.get_frame().set_alpha(0.5)
   plt.show()

.. plot::

   import numpy as np
   import scipy.integrate as integrate
   import matplotlib.pyplot as plt


   def derivs(state, t):
       """
       Return the derivatives of R and F, stored in the *state* vector::

	  state = [R, F]

       The return data should be [dR, dF] which are the derivatives of R
       and F at position *state* and time *t*.
       """

       # in the plot directive, these need to be defined local to the
       # function
       alpha, delta = 1, .25
       beta, gamma = .2, .05

       R, F = state
       dR = alpha*R - beta*R*F
       dF = gamma*R*F - delta*F
       return dR, dF

   # the initial population of rabbits and foxes
   R0 = 20
   F0 = 10

   # create a time array from 0..100 sampled at 0.1 second steps
   dt = 0.1
   t = np.arange(0.0, 100, dt)

   # the initial [rabbits, foxes] state vector
   y0 = [R0, F0]

   # y is a len(t)x2 2D array of rabbit and fox populations
   # over time
   y = integrate.odeint(derivs, y0, t)

   rabbits = y[:,0]
   foxes = y[:,1]
   fig = plt.figure()
   ax = fig.add_subplot(111)
   ax.plot(t, rabbits, label='rabbits')
   ax.plot(t, foxes, label='foxes')

   leg = ax.legend(loc='upper left', fancybox=True, shadow=True)
   leg.get_frame().set_alpha(0.5)
   plt.show()

In addition to the temporal solution of the ODE, we are often
interested in doing a phase-plane analysis to find the equilibrium
points and visualize the flows.  To do a phase plane analysis, we need
to create a 2D array of all possible rabbit/fox combinations, and then
evaluate the dynamics at each point.  The easiest way to do this is
create a 1D array of possible rabbit values, a 1D array of possible
fox values, and then use numpy's `meshgrid
<http://docs.scipy.org/doc/numpy/reference/generated/numpy.meshgrid.html>`_
function to create 2D arrays over the possible rabbit/fox
combinations.  We use matplotlib's `quiver
<http://matplotlib.sourceforge.net/api/axes_api.html#matplotlib.axes.Axes.quiver>`_
to plot the direction field at the ($R$, $F$) sample points of arrows
pointing in the ($dR$, $dF$) direction.


.. sourcecode:: python

  # R, F, dR and dF are 2D arrays giving the state and \
  # direction for each rabbit, fox combination
  rmax = 1.1 * rabbits.max()
  fmax = 1.1 * foxes.max()
  R, F = np.meshgrid(np.arange(-1, rmax),
		     np.arange(-1, fmax))
  dR = alpha*R - beta*R*F
  dF = gamma*R*F - delta*F

  fig = plt.figure()
  ax = fig.add_subplot(111)
  # the quiver function will show the direction fields
  #dR, dF at each point in R, F
  ax.quiver(R, F, dR, dF)

  ax.set_xlabel('rabbits')
  ax.set_ylabel('foxes')

  # also plot the single solution from odeint on the
  # phase-plane
  ax.plot(rabbits, foxes, color='black')

.. plot::

   import numpy as np
   import scipy.integrate as integrate
   import matplotlib.pyplot as plt

   # the parameters for rabbit and fox growth and interactions
   alpha, delta = 1, .25
   beta, gamma = .2, .05

   def derivs(state, t):
       """
       Return the derivatives of R and F, stored in the *state* vector::

	  state = [R, F]

       The return data should be [dR, dF] which are the derivatives of R
       and F at position *state* and time *t*.
       """
       alpha, delta = 1, .25
       beta, gamma = .2, .05
       R, F = state
       dR = alpha*R - beta*R*F
       dF = gamma*R*F - delta*F
       return dR, dF

   # the initial population of rabbits and foxes
   R0 = 20
   F0 = 10

   # create a time array from 0..100 sampled at 0.1 second steps
   dt = 0.1
   t = np.arange(0.0, 100, dt)

   # the initial [rabbits, foxes] state vector
   y0 = [R0, F0]

   # y is a len(t)x2 2D array of rabbit and fox populations
   # over time
   y = integrate.odeint(derivs, y0, t)

   rabbits = y[:,0]
   foxes = y[:,1]

   # R, F, dR and dF are 2D arrays giving the state and \
   # direction for each rabbit, fox combination
   rmax = 1.1 * rabbits.max()
   fmax = 1.1 * foxes.max()
   R, F = np.meshgrid(np.arange(-1, rmax),
		      np.arange(-1, fmax))
   dR = alpha*R - beta*R*F
   dF = gamma*R*F - delta*F

   fig = plt.figure()
   ax = fig.add_subplot(111)
   # the quiver function will show the direction fields
   #dR, dF at each point R, F
   ax.quiver(R, F, dR, dF)

   ax.set_xlabel('rabbits')
   ax.set_ylabel('foxes')
   ax.plot(rabbits, foxes, color='black')

   plt.show()


Finally, it is useful to study the equilibrium points of the system,
when the rabbit and fox populations are in a steady state.  The
equilibrium in rabbits occurs when $dR/dt=0$ and in foxes when
$dF/dt=0$.  The curves where the derivatives equal zero are called the
*null-clines* of the system, and can be found using matplotlib's
`contour
<http://matplotlib.sourceforge.net/api/axes_api.html#matplotlib.axes.Axes.contour>`_
which is used to find level sets over 2D data.  In particular, we'll
want to find the zero contours of $dR/dt$ and $dF/dt$ (these curves
can also be found by simple algebra in this case).  To accurately find
the null-clines, we'll want to sample the $R$, $F$ state space more
finely than in the direction field above.

.. sourcecode:: ipython

   # resample R, F,dF and dR at a higher frequency
   # for smooth null-clines
   R, F = np.meshgrid(np.arange(-1, rmax, 0.1),
		      np.arange(-1, fmax, 0.1))
   dR = alpha*R - beta*R*F
   dF = gamma*R*F - delta*F

   # use matplotlib's contour function to find the level curves where
   # dR/dt=0 and dF/dt=0 (the null-clines)
   ax.contour(R, F, dR, levels=[0], linewidths=3, colors='blue')
   ax.contour(R, F, dF, levels=[0], linewidths=3, colors='green')

   ax.set_title('trajectory, direction field and null clines')


.. plot::

   import numpy as np
   import scipy.integrate as integrate
   import matplotlib.pyplot as plt

   # the parameters for rabbit and fox growth and interactions
   alpha, delta = 1, .25
   beta, gamma = .2, .05

   def derivs(state, t):
       """
       Return the derivatives of R and F, stored in the *state* vector::

	  state = [R, F]

       The return data should be [dR, dF] which are the derivatives of R
       and F at position *state* and time *t*.
       """
       alpha, delta = 1, .25
       beta, gamma = .2, .05

       R, F = state
       dR = alpha*R - beta*R*F
       dF = gamma*R*F - delta*F
       return dR, dF

   # the initial population of rabbits and foxes
   R0 = 20
   F0 = 10

   # create a time array from 0..100 sampled at 0.1 second steps
   dt = 0.1
   t = np.arange(0.0, 100, dt)

   # the initial [rabbits, foxes] state vector
   y0 = [R0, F0]

   # y is a len(t)x2 2D array of rabbit and fox populations
   # over time
   y = integrate.odeint(derivs, y0, t)

   rabbits = y[:,0]
   foxes = y[:,1]

   # R, F, dR and dF are 2D arrays giving the state and \
   # direction for each rabbit, fox combination
   rmax = 1.1 * rabbits.max()
   fmax = 1.1 * foxes.max()
   R, F = np.meshgrid(np.arange(-1, rmax),
		      np.arange(-1, fmax))
   dR = alpha*R - beta*R*F
   dF = gamma*R*F - delta*F

   fig = plt.figure()
   ax = fig.add_subplot(111)
   # the quiver function will show the direction fields
   #dR, dF at each point R, F
   ax.quiver(R, F, dR, dF)

   ax.set_xlabel('rabbits')
   ax.set_ylabel('foxes')
   ax.plot(rabbits, foxes, color='black')


   # resample R, F,dF and dR at a higher frequency
   # for smooth null-clines
   R, F = np.meshgrid(np.arange(-1, rmax, 0.1),
		      np.arange(-1, fmax, 0.1))
   dR = alpha*R - beta*R*F
   dF = gamma*R*F - delta*F

   # use matplotlib's contour function to find the level curves where
   # dR/dt=0 and dF/dt=0 (the null-clines)
   ax.contour(R, F, dR, levels=[0], linewidths=3, colors='blue')
   ax.contour(R, F, dF, levels=[0], linewidths=3, colors='green')

   ax.set_title('trajectory, direction field and null clines')

   plt.show()

By visual inspection, we see four equilibria where the null-clines
intersect: (0,0), (0,5), (5,0) and (5,5).  You should be able to
easily verify these by solving for R and F where $dR/dt=0$ and
$dF/dt=0$,
