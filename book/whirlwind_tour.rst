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


Before proceeding, make sure you can fire up ipython in
:ref:`ipython_pylab` and navigate to the :ref:`sample_data`.


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



To compute the regression line above, we used the numpy ``np.polyfit``
function, which will find the polynomial that is the best fit to your
data in a least-squared sense.  The argument ``1`` to polyfit
indicates a linear fit.  The parameters ``pars`` in the example are
the slope and intercept of the best-fit line


.. sourcecode:: ipython

   In [48]: pars
   Out[48]: array([  0.19355121,  10.46326299])


For higher order polynomial fits like quadratic or cubic, use orders
``2`` or ``3``.  For much more sophisticated parametric modeling, see
the tools in ``scipy.optimize``.


.. _stock_demo:

Working with richer data and files
------------------------------------

In the simple body fat example above, we used ``np.loadtxt`` to import
data from one of the simplest formats available: a plain text file
living on your computer with no headers, comments or non-numeric data.
numpy is exceedingly good at handling this data, seamlessly importing
it into a 2D homogeneous array of floating point numbers (notice the
dtype "datatype" of ``float64`` in the array ``X`` above, indicating
an 8byte/64 bit floating point number).  Real word data is much more
varied than floating point numbers, composed of strings, dates,
integers, complex numbers, and more, and is scattered across
filesystems, databases, and the internet.  Python, with its "batteries
included" philosophy, is fully equipped to work with that data.

A nice example of the kind of data you see in real-world application
is daily stock price data, with it's mix of dates, floating point
numbers and integers.  Take a look at the "Yahoo Finance" `historical
price data <http://finance.yahoo.com/q/hp?s=CROX>`_ for the Crocs
company (ticker CROX).  At the bottom of this page, there is a
"Download to Spreadsheet" to download the CSV file to your computer;
this works fine for one or two stocks, but if you want to analyze
hundreds, or automate daily analysis, you will need to be able to
fetch this data automatically from your Python program.  Using the
built-in `urllib <http://docs.python.org/library/urllib.html>`_
library for working with internet data, it's easy.  The function
`urllib.urlretrieve
<http://docs.python.org/library/urllib.html#urllib.urlretrieve>`_ can
be used to fetch a remote file.

First copy the URL from Yahoo Finance historical prices page by right
clicking on the "Download to Spreadsheet" link at the bottom of the
page and choosing "Copy Link Location", and then pasting the URL link
into your ipython session and name it "url"


.. sourcecode:: ipython

   In [59]: url = 'http://ichart.finance.yahoo.com/table.csv?s=CROX\
      ....: &d=9&e=22&f=2009&g=d&a=1&b=8&c=2006&ignore=.csv'

   In [60]: import urllib

   In [61]: fname, msg = urllib.urlretrieve(url)

   In [62]: fname
   Out[62]: '/tmp/tmpMXW2Gn.csv'


By default ``urlretrieve`` will create a temporary file somewhere on
your system and download the file, so your location and file name will
be different.  We can inspect it in ipython.

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
converters to covert strings to arbitrary types, and handling
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
which describes the datatype of the record array.  The ``dtype``
object here maps the names of the fields *date*, *open*, *volume*, etc
to the types ``|O4``, ``<f8``, ``<i4`` meaning "4 byte python object",
"little endian 8 byte float" and "little endian 4 byte integer
(endianess is the byte ordering used to represent the data and varies
across different computing architectures).

In the printed record array above, we see that the values are
*decreasing* over the rows, and normally we think of this data
*increasing* in time.  To sort a record array, just call the sort
method, which will sort over the first column by default (you can
pass in the *order* keyword argument to ``sort`` to sort over a
different field.

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
but becomes tedious to track for a large number of columns.  One of
the beauties of the named dtypes in record arrays is that you can
access the named columns of your data.  For example, to work with the
date column, we can refer to ``r.date`` and even call python
`datetime.date <http://docs.python.org/library/datetime.html>`_
methods on the dates stored in the array.

.. sourcecode:: ipython

   In [89]: r.date[:4]
   Out[89]: array([2006-02-08, 2006-02-09, 2006-02-10, 2006-02-13], dtype=object)

   In [90]: date0 = r.date[0]

   In [91]: date0
   Out[91]: datetime.date(2006, 2, 8)

   In [92]: date0.year
   Out[92]: 2006

Wrapping up this section, we can see how an investment in CROX has
fared over the past few years.

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
the example below, we tackle the following questions about dollar trading
volume in CROX -- the total dollars traded is approximately given by
the product of the volume of shares traded (the *volume* field) times
the price of the shares, given by the *close*.  We can easily answer
compute the average daily trading volume, the average over the last
forty trading days, the largest day ever, the date of the largest day,
the standard deviation of the trading volume, etc...


.. sourcecode:: ipython

   # dv is the dollar volume traded
   In [101]: dv = r.volume * r.close

   # the average and standard deviation of dv
   In [102]: dv.mean()
   Out[102]: 131809256.93676312

   In [103]: dv.std()
   Out[103]: 222149688.4737061

   # the average in the last 40 trading days
   In [104]: dv[-40:].mean()
   Out[104]: 66807846.700000003

   # the biggest date ever
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

It's not just numerical computing that Python excels at.  While much
of your time doing scientific computing in Python will be spent in the
core extension packages that provide fast arrays, statistics and
visualization, a strong advantage that Python has over many
alternatives is that Python is a full blow object oriented language
with rich data structures, built in libraries, and support for
multiple programming paradigms.  We'll take a break from crunching
numbers to illustrate python's power in string processing, utilizing
one of the essential data structures in python: the dictionary.

A common task in text processing is to produce a count of word frequencies.
While numpy has a built in histogram function for doing numerical histograms,
it won't work out of the box for counting discrete items, since it
is a binning histogram for a range of real values.

But the Python language provides very powerful string manipulation
capabilities, as well as a very flexible and efficiently implemented
built in data type, the *dictionary*, that makes this task a very
simple one.  Below, count the frequencies of all the words contained
in a compressed text file of *Alice's Adventures in Wonderland* by
Lewis Carroll, downloaded from `Project Gutenberg <http://www.gutenberg.org/wiki/Main_Page>`_.

.. figure:: _static/alice_chapter1.jpg
   :width: 4in

   Facimile from `Chapter 1 <http://www.gutenberg.org/files/19002/19002-h/19002-h.htm>`_ of Project Gutenberg Alice in Wonderland

We'll define "words" to simply be the result of splitting the input
text into a list, using any form of white-space as a separator. This
is obviously a very naive definition of word, but it will suffice for
the purposes of this example.  Python strings have a ``split()``
method that allows for very flexible splitting. You can easily get
more details on it in IPython:

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

The complete set of methods of Python strings can be viewed by typing ``a.TAB``

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


Each of them can be similarly queried with the ``'?'`` operator as
above.  For more details on Python strings and their companion
sequence types, see `string methods
<http://docs.python.org/library/stdtypes.html#string-methods>`_

Back to Alice.  We want to read the text in from the zip file, split
it into words and then count the frequency of each word.  You will
need to read the compressed file
:file:`bookdata/alice_in_wonderland.zip` . Python has facilities to do
this without having to manually uncompress using the `zipfile
<http://docs.python.org/library/zipfile.html>`_ module.  The zip file
consists of one or more text files, and we can use the module to load
the zip file, list the files, and then read the text from the one file
in the zip archive

.. sourcecode:: ipython

   In [101]: import zipfile

   In [102]: zf = zipfile.ZipFile('alice_in_wonderland.zip')

   In [103]: zf.namelist()
   Out[103]: ['28885.txt']

   In [104]: text = zf.read('28885.txt')


Be careful printing text -- it is the entire manuscript so it will
dump a lot of text to your screen.  We can print the characters from
2000:2400 using standard python slicing

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
method as described.  To ignore casing difference, we will convert
every word to lower case

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

To finish up this example, we want to print the most common occuring
words.  The easiest way to do this is create a list of (*count*,
*word*) tuples, and then sort the list.  So we will create a list of
2-tuples.  python will sort this according to the first element of the
tuple -- the *count* -- and for identical counts will sort by the second
element of the tuple -- the *word*.  The dictionary method ``items``
returns a list of (*key*, *value*) pairs, ie (*word*, *count*), so we
need to reverse this to get (*count*, *word*) pairs

.. sourcecode:: ipython

   In [103]: counts = [(count, word) for word, count in countd.items()]

   In [104]: counts[:3]
   Out[104]: [(2, '"--and'), (1, 'figure!"'), (6, 'four')]

You will probably see different number/word pairs because dictionaries
are unordered and the return value from ``items`` is unorded.  We can
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

Of course, this is just a toy example, and have not "cleaned" the word
data by stripping off punctuation, but it does show off some of the
versatile data structures and standard library functionality that
makes these tasks easy and elegant in python.  Let's take the example
one step further to strip the words of all non-alphabetic characters.
There are two string methods that help here: ``translate`` and
``isalpha``.  The ``translate`` method is used to translate certain
string characters into other characters, but it has an optional second
argument which is a string of characters you want to delete.  So we
need to build a string which is all of the characters *except* the
alphabetic characters.  The ASCII character set are the characters
represented by the ordinal numbers from 0..255, and the ``isalpha``
method will return True if the character is a member of the alphabet.

.. sourcecode:: ipython

   In [123]: ascii_chars = [chr(i) for i in range(256)]

   In [124]: nonalpha_chars = [chr(i) for i in range(256)\
      .....: if not chr(i).isalpha()]


From this list of non-alpha characters, we need to create a string of
the same characters.  To create a string from a list of characters,
use the ``join`` method::

    nonalpha_str = ''.join(nonalpha_chars)



Here is the entirety of the
script without the extra commentary

.. sourcecode:: ipython

  import zipfile
  zf = zipfile.ZipFile('alice_in_wonderland.zip')
  text = zf.read('28885.txt')

  words = [word.lower() for word in text.split()]

  countd = dict()

  for word in words:
      countd[word] = countd.get(word, 0) + 1

  counts = [(count, word) for word, count in countd.items()]
  counts.sort()

  for count, word in counts[-6:]:
      print word, count

