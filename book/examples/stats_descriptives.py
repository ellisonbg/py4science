import scipy.stats as stats
from matplotlib.mlab import detrend_linear, load

import numpy
import pylab


class Descriptives:
    """
    a helper class for basic descriptive statistics and time series plots
    """
    def __init__(self, samples):
        self.samples = numpy.asarray(samples)
        self.N = len(samples)
        self.median = stats.median(samples)
        self.min = numpy.amin(samples)
        self.max = numpy.amax(samples)
        self.mean = stats.mean(samples)
        self.std = stats.std(samples)
        self.var = self.std**2.
        self.skew = stats.skew(samples)
        self.kurtosis = stats.kurtosis(samples)
        self.range = self.max - self.min

    def __repr__(self):
        """
        Create a string representation of self; pretty print all the
        attributes:

         N, median, min, max, mean, std, var, skew, kurtosis, range,
        """
        
        descriptives = (
            'N        = %d'        % self.N,
            'Mean     = %1.4f' % self.mean,
            'Median   = %1.4f'   % self.median,
            'Min      = %1.4f'  % self.min,
            'Max      = %1.4f'  % self.max,
            'Range    = %1.4f'  % self.range,                        
            'Std      = %1.4f' % self.std,            
            'Skew     = %1.4f'     % self.skew,
            'Kurtosis = %1.4f' % self.kurtosis,           
        )
        return '\n'.join(descriptives)

    def plots(self, figfunc, maxlags=20, Fs=1, detrend=detrend_linear,
              fmt='bo', bins=100,
              ):
        """
        plots the time series, histogram, autocorrelation and spectrogram

        figfunc is a figure generating function, eg pylab.figure
        
        return an object which stores plot axes and their return
        values from the plots.  Attributes of the return object are
        'plot', 'hist', 'acorr', 'psd', 'specgram' and these are the
        return values from the corresponding plots.  Additionally, the
        axes instances are attached as c.ax1...c.ax5 and the figure is
        c.fig

        keyword args:
        
          Fs      : the sampling frequency of the data

          maxlags : max number of lags for the autocorr

          detrend : a function used to detrend the data for the correlation and spectral functions

          fmt     : the plot format string

          bins : the bins argument to hist
        """
        data = self.samples

	# Here we use a rather strange idiom: we create an empty do
        # nothing class C and simply attach attributes to it for
        # return value (which we carefully describe in the docstring).
        # The alternative is either to return a tuple a,b,c,d or a
        # dictionary {'a':someval, 'b':someotherval} but both of these
        # methods have problems.  If you return a tuple, and later
        # want to return something new, you have to change all the
        # code that calls this function.  Dictionaries work fine, but
        # I find the client code harder to use d['a'] vesus d.a.  The
        # final alternative, which is most suitable for production
        # code, is to define a custom class to store (and pretty
        # print) your return object
        class C: pass
        c = C()
        N = 5
        fig = c.fig = figfunc()
	fig.subplots_adjust(hspace=0.3)
        ax = c.ax1 = fig.add_subplot(N,1,1)
        c.plot = ax.plot(data, fmt)
	ax.set_ylabel('data')

        ax = c.ax2 = fig.add_subplot(N,1,2)
        c.hist = ax.hist(data, bins)
	ax.set_ylabel('hist')

        ax = c.ax3 = fig.add_subplot(N,1,3)
        c.acorr = ax.acorr(data, detrend=detrend, usevlines=True, 
	  maxlags=maxlags, normed=True)
	ax.set_ylabel('acorr')

        ax = c.ax4 = fig.add_subplot(N,1,4)
        c.psd = ax.psd(data, Fs=Fs, detrend=detrend)
	ax.set_ylabel('psd')

        ax = c.ax5 = fig.add_subplot(N,1,5)
        c.specgtram = ax.specgram(data, Fs=Fs, detrend=detrend)
	ax.set_ylabel('specgram')
        return c


if __name__=='__main__':

    # load the data in filename fname into the list data, which is a
    # list of floating point values, one value per line.  Note you
    # will have to do some extra parsing
    data = []
    fname = '../bookdata/nm560.dat'  # tree rings in New Mexico 837-1987
    fname = '../bookdata/hsales.dat'  # home sales
    for line in file(fname):
        line = line.strip()
        if not line: continue
        vals = line.split()
        val = vals[0]
        data.append(float(val))

    desc = Descriptives(data)
    print desc
    c = desc.plots(pylab.figure, Fs=12, fmt='-')
    c.ax1.set_title(fname)

    c.fig.savefig('stats_descriptives.png', dpi=150)    
    c.fig.savefig('stats_descriptives.eps')    
    pylab.show()
