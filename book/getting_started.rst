.. _getting_started:

================
Getting started
================

blah

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

Downloading the data
---------------------

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



.. _how_to_get_help:

How to get help
---------------------

TODO


.. include:: links.txt
