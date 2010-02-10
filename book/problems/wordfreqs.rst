Dictionaries for counting words
===============================

A common task in text processing is to produce a count of word frequencies.
While NumPy has a builtin histogram function for doing numerical histograms, it
won't work out of the box for couting discrete items, since it is a binning
histogram for a range of real values.

But the Python language provides very powerful string manipulation
capabilities, as well as a very flexible and efficiently implemented builtin
data type, the *dictionary*, that makes this task a very simple one.

In this problem, you will need to count the frequencies of all the words
contained in a compressed text file supplied as input.  Load and read the data
file ``HISTORY.gz`` (without uncompressing it on the filesystem separately),
and then use a dictionary count the frequency of each word in the file.  Then,
display the 20 most and 20 least frequent words in the text.


Hints
-----


* To read the compressed file ``HISTORY.gz`` without uncompressing it first,
  see the :mod:`gzip` module.
* Consider 'words' simply the result of splitting the input text into a list,
  using any form of whitespace as a separator. This is obviously a very naive
  definition of 'word', but it shall suffice for the purposes of this exercise.
* Python strings have a ``.split()`` method that allows for very flexible
  splitting. You can easily get more details on it in IPython:

.. sourcecode:: ipython

   In [2]: a = 'somestring'

   In [3]: a.split?
   Type:           builtin_function_or_method
   Base Class:     <type 'builtin_function_or_method'>
   Namespace:      Interactive
   Docstring:
       S.split([sep [,maxsplit]]) -> list of strings

       Return a list of the words in the string S, using sep as the
       delimiter string.  If maxsplit is given, at most maxsplit
       splits are done. If sep is not specified or is None, any
       whitespace string is a separator.

The complete set of methods of Python strings can be viewed by hitting
the TAB key in IPython after typing ``a.``, and each of them
can be similarly queried with the ``?`` operator as above.
For more details on Python strings and their companion sequence types,
see `here
<http://docs.python.org/library/stdtypes.html#sequence-types-str-unicode-list-tuple-buffer-xrange>`_.

.. only:: instructor

   Solution
   --------

   A solution to this problem is here:
     
   .. literalinclude:: examples/wordfreqs.py
