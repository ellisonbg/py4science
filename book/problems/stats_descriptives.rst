.. include:: ../stats_descriptives.rst

For this exercise, you should write a class that can be initialized with a
dataset (a 1-d sequence) and will compute and store the following statistics
from the data: length, median, min, max, mean, std, var, skew, kurtosis and
range (max-min).

Printing an instance of this class should print a nicely formatted text summary
with the above quantities, such as::

    Name     = ../bookdata/hsales.dat
    Npts     = 275
    Mean     = 52.2873
    Median   = 53.0000
    Min      = 24.0000
    Max      = 89.0000
    Range    = 65.0000
    Std      = 11.9170
    Skew     = 0.1801
    Kurtosis = 0.0748

The object should also have a :meth:`plots` method, which when called, produces
a figure with a few subplots: the data itself, its histogram, an
autocorrelation plot, a power spectral density plot and a spectrogram.  See the
figure for an example of such a plot.

.. figure:: fig/stats_descriptives.png
   :width: 4in

   Simple descriptive statistics from a dataset of home sale volumes.
    
.. admonition:: Hints

   - You can load the data from the example files provided.

   - In addition to the methods of numpy arrays, you may find the
     :mod:`scipy.stats` module useful for some of the required statistics.
     
   - When you call in python ``print(x)``, Python will print the output of the
     special :meth:`__str__` method.
     
   - For the necessary plots, see the :meth:`acorr`, :meth:`psd` and
     :meth:`specgram` methods of Axis objects.


.. only:: instructor

   Solution
   ~~~~~~~~

   .. literalinclude:: examples/stats_descriptives.py
