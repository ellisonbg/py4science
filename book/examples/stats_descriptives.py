#!/usr/bin env python
"""Simple descriptive statistics for a data file.

Usage:

stats_descriptives.py filename [column]

The column number defaults to 0 if not given."""


#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

import sys

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

from matplotlib.mlab import detrend_linear, load

#-----------------------------------------------------------------------------
# Class and function declarations
#-----------------------------------------------------------------------------

class Descriptives:
    """
    a helper class for basic descriptive statistics and time series plots
    """
    def __init__(self, samples, name=None):
        samples = np.asarray(samples)
        self.samples = samples
        self.name = name
        self.npts = len(samples)
        self.median = stats.median(samples)
        self.min = samples.min()
        self.max = samples.max()
        self.mean = samples.mean()
        self.std = samples.std()
        self.var = samples.var()
        self.skew = stats.skew(samples)
        self.kurtosis = stats.kurtosis(samples)
        self.range = self.max - self.min

    def __str__(self):
        """
        Return a string representation of self; pretty print all the
        attributes:

         npts, median, min, max, mean, std, var, skew, kurtosis, range,
        """
        descriptives = []
        if self.name:
            descriptives.append('Name     = %s'    % self.name)
        descriptives.extend([
            'Npts     = %d'    % self.npts,
            'Mean     = %1.4f' % self.mean,
            'Median   = %1.4f' % self.median,
            'Min      = %1.4f' % self.min,
            'Max      = %1.4f' % self.max,
            'Range    = %1.4f' % self.range,                        
            'Std      = %1.4f' % self.std,            
            'Skew     = %1.4f' % self.skew,
            'Kurtosis = %1.4f' % self.kurtosis,           
            ])
        return '\n'.join(descriptives)

    def plots(self, fig=None, maxlags=20, Fs=1, detrend=detrend_linear,
              fmt='-', bins=100 ):
        """
        plots the time series, histogram, autocorrelation and spectrogram

        Parameters
        ----------
        
        fig : figure object, optional
          If not given, a new figure is created.

        
        Fs : float, optional
          Sampling frequency of the data.

        maxlags : int, optional
          max number of lags for the autocorrelation.

        detrend : function, optional
          A function used to detrend the data for the correlation and spectral
          functions.

        fmt : string, optional
          The plot format string.

        bins : int, optional  
          The bins argument to hist.

        Returns
        -------

        An object which stores plot axes and their return values from the
        plots.  Attributes of the return object are 'plot', 'hist', 'acorr',
        'psd', 'specgram' and these are the return values from the
        corresponding plots.  Additionally, the axes instances are attached as
        c.ax1...c.ax5 and the figure is c.fig
        """
        data = self.samples

	# Here we use an idiom that may appear strange, but that is in practice
        # widely used in Python: we create an empty do nothing class C and
        # simply attach attributes to it for return value (which we carefully
        # describe in the docstring).
        #
        # The alternative is either to return a tuple a,b,c,d or a dictionary
        # {'a':someval, 'b':someotherval} but both of these methods have
        # problems.  If you return a tuple, and later want to return something
        # new, you have to change all the code that calls this function.
        # Dictionaries work fine, but I find the client code harder to use
        # d['a'] vesus d.a.  The final alternative, which is most suitable for
        # production code, is to define a custom class to store (and pretty
        # print) your return object
        class C: pass
        c = C()

        # Set font size to be relatively small
        plt.rc('font', size=8)
        if fig is None:
            fig = plt.figure()
            
        c.fig = fig
        nplots = 5
	fig.subplots_adjust(hspace=0.4)
        ax = c.ax1 = fig.add_subplot(nplots,1,1)
        if self.name:
            ax.set_title(self.name)
        c.plot = ax.plot(data, fmt)
	ax.set_ylabel('data')

        ax = c.ax2 = fig.add_subplot(nplots,1,2)
        c.hist = ax.hist(data, bins)
	ax.set_ylabel('hist')

        ax = c.ax3 = fig.add_subplot(nplots,1,3)
        c.acorr = ax.acorr(data, detrend=detrend, usevlines=True, 
                           maxlags=maxlags, normed=True)
	ax.set_ylabel('acorr')

        ax = c.ax4 = fig.add_subplot(nplots,1,4)
        c.psd = ax.psd(data, Fs=Fs, detrend=detrend)
	ax.set_ylabel('psd')

        ax = c.ax5 = fig.add_subplot(nplots,1,5)
        c.specgtram = ax.specgram(data, Fs=Fs, detrend=detrend)
	ax.set_ylabel('specgram')
        return c

#-----------------------------------------------------------------------------
# Main use as script
#-----------------------------------------------------------------------------
if __name__=='__main__':

    # Grab command-line arguments.  For anything more complex than one or two
    # positional arguments, one should use the optparse module in Python's
    # standard library, or even better, argparse, which will be part of the
    # stdlib as of Python 2.7 and 3.2 (and can be downloaded separately).
    try:
        fname = sys.argv[1]
    except IndexError:
        # Hardcode some defaults so we can run it without arguments as a demo
        fname = '../bookdata/nm560.dat'  # tree rings in New Mexico 837-1987
        fname = '../bookdata/hsales.dat'  # home sales
    try:
        colnum = int(sys.argv[2])
    except IndexError:
        colnum = 0

    # Load the data file
    data = np.loadtxt(fname, usecols=[colnum])
    desc = Descriptives(data, name=fname)
    # Print the summary on screen
    print desc
    # Some of our sample data files contain monthly data, so Fs=12.  This only
    # alters the units on the display.
    c = desc.plots(Fs=12)

    # Leave a figure on disk
    c.fig.savefig('stats_descriptives.png', dpi=150)    
    plt.show()
