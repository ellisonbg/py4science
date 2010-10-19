============
 Statistics
============

In the last 15 years, the open source R project, an implementation
of the S language originally created at Bell Labs in the
mid-1970s, has become in most cases the *lingua franca* of statistical
computing, as it is used widely throughout the academic statistics
community. The Comprehensive R Archive Network (CRAN) has a wealth of
freely available R packages, many of which have been contributed by
the authors of leading research papers. There is an R package to
estimate and analyze nearly any kind of statistical
model. Additionally, it has sophisticated graphics capabilities,
making it a good candidate for research applications.

Of course, there are other popular retail and open source statistical
computing environments, such as MATLAB, SAS, Stata, and many
others. For more specialized applications such as econometrics, there
are software packages with advanced capabilities but are perhaps not
well-suited for general purpose statistics.

Despite the existence of so many other statistical computing
environments, there has been growing interest in building statistical
tools in Python for many of the same reasons we use Python for other
kinds of problems:

* Python excels in high performance applications through its parallel
  computing facilities, and easy of interfacing with lower-level code
  via ``Cython``, ``f2py``, and ``C``, and other tools.
* Python's permissive BSD license makes it both safe for
  cloud-computing (a problem for retail software) and commercial
  software (a problem with R since it is GPL-licensed).
* Python's simplicity and multi-paradigm (object-oriented, functional,
  procedural) nature make it a good choice for building software as
  well as interactive research.

As R was built from the ground up as a statistical computing
language, it is less suitable for writing larger software modules or
building systems than Python. Python users new to R will likely find
its data structures clunky and nuanced and its programming idioms ad
hoc or sometimes "magical".

Currently, Python does not have the breadth and depth of core
statistical functionality that R does, but that is becoming less true
as time goes on. We will not discuss in detail active projects
implementing statistical methods in Python but rather introduce the
core statistical tools in NumPy and SciPy. These include an array of
basic descriptive statistics, hypothesis testing, and numerical tools
for working with almost every common discrete and continuous
probability distribution.

.. _stats_distributions:

Statistical distributions
-------------------------

The ability to efficiently generate samples from common probability
distributions (also known as *random variables*) is a basic
prerequisite for most statistical computing applications. NumPy and
SciPy support this functionality through the ``numpy.random`` and
``scipy.stats`` modules. ``numpy.random`` enables (pseudo) random
number generation using the Mersenne Twister algorithm, while
``scipy.stats`` provides an elegant object-oriented interface to
computing common functions related to each kind of random variable (in
addition to also being also to generate samples). We will give an
overview of both of these modules and their usage.

Generating random numbers: ``numpy.random``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For generating random samples from a distribution with fixed
parameters (for example, $\mathrm{Normal}(\mu, \sigma)$ or
$\mathrm{Uniform}(a, b)$), ``numpy.random`` is your best bet, as it is
an easy-to-use interface to some very fast C code. Calling
``numpy.random?`` in IPython will show a table of distributions
available. To generate samples, we pass the parameters of the
distribution and a ``size`` tuple (as a keyword), which will be the
shape of the ``ndarray`` returned:

.. ipython::

   In [1]: np.random.normal(0, 2, size=(5, 2))

Some distributions (like the normal distribution) have default
parameters, so it may not be necessary in all cases to specify the
parameters (default values can be found in the docstrings):

.. ipython::

    In [35]: np.random.normal(size=4)

A number of convenience functions are available for computing the
most common random numbers:

.. ipython::

    In [46]: np.random.rand(2, 2) # Uniform(0, 1)

    In [47]: np.random.randn(2, 2) # Normal(0, 1)

It should be no surprise that any probability density of interest can
be reasonably well-approximated by a normalized histogram of samples
(we discuss plotting the pdf later in this chapter):

.. sourcecode:: python

    samples = np.random.randn(10000)
    plt.hist(samples, bins=100, normed=True, color='gray',
             rwidth=0.5)
    plot_function(stats.norm.pdf, -4, 4, style='k')

.. plot:: examples/stats_graphs_norm_hist.py

   Normalized histogram of Normal(0, 1) samples with actual density
   curve

.. note::

    For users of other statistical packages, many univariate random
    variables in NumPy and SciPy are parameterized in the classical
    *location-scale* fashion. In other words, samples are constructed
    from a *standard* density function (for example,
    $\mathrm{Normal}(0,1)$), and samples from the parameters of
    interest are computed by $\mu + \sigma \cdot \mathrm{sample}$,
    where $\mu$ and $\sigma$ are the location and scale parameters,
    respectively. Thus, new users should be careful to note which
    convention is being used compared with other environments you may
    be used to (for example R).

Random variable objects: ``scipy.stats``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``scipy.stats`` module provides flexible objects enabling us to
compute a variety of quantities related to a probability
distribution. Each of these functions is accessed through an instance
of either ``rv_discrete`` or ``rv_continuous`` for discrete and
continuous random variables, respectively. You can get a list of all
of the available distributions by calling ``scipy.stats?`` in
IPython. The methods available in these objects is given in the
following table:

.. csv-table:: Probability distribution functions
   :header: "Function", "Description"
   :widths: 10, 60

   ``rvs``, "Generate random samples"
   ``cdf``, "Cumulative distribution function $F(x) = P(X \leq x) = \int_{-\infty}^x f(x) dx$"
   ``pdf``, "(Continuous RV only) Probability density function $F^\prime(x)$"
   ``pmf``, "(Discrete RV only) Probability mass function $f(x) = P(X = x)$"
   ``ppf``, "Inverse CDF, ``u = ppf(x)`` if $F(u) = x$"
   ``fit``, "Compute distribution parameters best fitting data"
   ``rvs``, "Generate random samples"
   ``sf``, "Survival function $1 - F(x)$"
   ``isf``, "Survival function $(1 - F(x))^{-1}$"
   ``stats``, "Mean, variance, and optionally skew and kurtosis"

To illustrate how these work, let's consider the $\mathrm{Beta}(a, b)$
distribution on $[0, 1]$, a common distribution used to model
probabilities. We can use this distribution in similar fashion to the
functions in ``numpy.random``:

.. ipython::

    In [1]: from scipy.stats import beta

    In [2]: beta.rvs(2, 6, size=10)

    In [3]: beta.pdf(0.8, 2, 6)

When writing functions we might be interested in treating a
distribution like a *black box* of sorts; i.e., a probability
distribution whose parameters have been set elsewhere. All we care
about is that we can sample from it, call its ``cdf`` and ``pdf``,
etc. The object-oriented nature of Python made this quite easy to
implement in SciPy:

.. ipython::

    In [3]: dist = beta(2, 6)

    In [4]: dist

    In [5]: dist.cdf(np.arange(0, 1, 0.2))

    In [5]: dist.pdf(np.arange(0, 1, 0.2))

If we were interested in graphing the ``pdf``, ``cdf``, or any other
function of a random variable, we could write a generic plotting
function like this:

.. sourcecode:: python

    def plot_function(f, xstart=0, xend=1, n=1000, style='b'):
	increment = (xend - xstart) / n
	xs = np.arange(xstart, xend + increment, increment)
	ys = f(xs)
	plt.plot(xs, ys, style)
	plt.xlim([xstart - 1, xend + 1])

Then execute code like this to obtain the below plots:

.. sourcecode:: python

   plot_function(beta(2, 4).pdf, 0, 1, style='k--')
   plot_function(beta(2, 4).pdf, 0, 1, style='k')

   figure()
   plot_function(stats.norm.pdf, -4, 4, style='k')
   plot_function(stats.norm.cdf, -4, 4, style='k--')

.. plot:: examples/stats_graphs_beta_pdfs.py

   Plots of some beta probability density functions

.. plot:: examples/stats_graphs_norm_cdf.py

   Normal(0, 1) density and cumulative distribution function

Computing distribution statistics over a range of parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An important feature of the distributions in ``scipy.stats`` is that
most of the functions can accept arrays as parameters for the
distributions.

.. _stats_descriptive:

Computing descriptive statistics
--------------------------------

The first step in any statistical analysis should be to describe,
charaterize and importantly, visualize your data.  The normal
distribution lies at the heart of much of formal statistical analysis,
and normal distributions have the tidy property that they are
completely characterized by their mean and variance.  As you may have
observed in your interactions with family and friends, most of the
world is not normal, and many statistical analyses are flawed by
summarizing data with just the mean and standard deviation (square
root of variance) and associated signficance tests (eg the $t$-test)
as if it were normally distributed data.

``numpy`` and ``scipy.stats`` provide many of the common functions
used in exploratory data analysis, such as mean, median, variance,
skewness, kurtosis, and others. Given some data, we can compute all of
these quantities easily:

.. ipython::

   In [1]: import scipy.stats as stats

   In [1]: data = np.random.normal(2, 5, 50)

   In [2]: data.mean()

   In [4]: data.std()

   In [5]: stats.skew(data) # Skewness

   In [6]: stats.kurtosis(data)


Here is a table of some of the most widely used functions:

.. csv-table:: Common descriptive statistics
   :header: "Statistic", "Where to find"
   :widths: 40, 60

   "``sum, min, max, mean, std, var``", "``ndarray`` instance methods and ``numpy`` namespace"
   "``median``", "``numpy`` namespace"
   "``mode``, ``skew``, ``kurtosis``, ``moment`` (higher moments)", "``scipy.stats``"

A more exhaustive list can be found in the ``scipy.stats`` module
docstring. If you can't find something you are looking for, it may be
available in another library (see end of chapter for some places to
look). Of course, there is nothing to stop you from writing a new
function and contributing it to SciPy!

"Object-oriented" statistics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~


In the exercise below, we write a class to provide descriptive
statistics of a data set passed into the constructor, with class
methods to pretty print the results and to create a battery of
standard plots which may show structure missing in a casual analysis.
Many new programmers, or even experienced programmers used to a
procedural environment, are uncomfortable with the idea of classes,
having heard their geekier programmer friends talk about them but not
really sure what to do with them.  There are many interesting things
one can do with classes (aka object-oriented programming) but at their
heart they are a way of bundling data with methods that operate on
that data.  The ``self`` variable is special in Python and is how the
class refers to its own data and methods.  Here is a toy example:

.. ipython::

   In [115]: class MyData:
      .....:     def __init__(self, x):
      .....:         self.x = x
      .....:     def sumsquare(self):
      .....:         return (self.x**2).sum()
      .....:
      .....:

   In [116]: mydata = MyData(np.random.rand(100))

   In [117]: mydata.sumsquare()
   Out[117]: 29.6851135284

Along these lines, we might be in generating a standard set of output
for a bunch of different data sets, like so:

::

    In [2]: Descriptive(data)
    Npts     = 275
    Mean     = 52.2873
    Median   = 53.0000
    Min      = 24.0000
    Max      = 89.0000
    Range    = 65.0000
    Std      = 11.9170
    Skew     = 0.1801
    Kurtosis = 0.0748

The recipe with plotting code follows. Note that the ``plots`` method
makes use of a "dummy class" to store the various ``matplotlib``
objects created. This is an alternative to returning a large tuple or
dict and is a matter of preference. In practice this idiom is used
widely throughout Python as ``obj.a`` is often more convenient than
``obj['a']``.

.. sourcecode:: python

    class Descriptive:
    	"""
        A helper class for descriptive statistics
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

	def __repr__(self):
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
	    plots the time series, histogram, autocorrelation and
	    spectrogram

	    Parameters
	    ----------
	    fig : figure object, optional
	      If not given, a new figure is created.
	    Fs : float, optional
	      Sampling frequency of the data.
	    maxlags : int, optional
	      max number of lags for the autocorrelation.
	    detrend : function, optional
	      A function used to detrend the data for the correlation and
	      spectral functions.
	    fmt : string, optional
	      The plot format string.
	    bins : int, optional
	      The bins argument to hist.

	    Returns
	    -------
	    An object which stores plot axes and their return values from
	    the plots.  Attributes of the return object are 'plot',
	    'hist', 'acorr', 'psd', 'specgram' and these are the return
	    values from the corresponding plots.  Additionally, the axes
	    instances are attached as c.ax1...c.ax5 and the figure is
	    c.fig
	    """
	    data = self.samples

    	    # create dummy class
    	    class C: pass
	    c = C()

	    # Set font size to be relatively small
	    plt.rc('font', size=10)
    	    c.fig = fig = plt.figure()

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
	    return c

.. plot:: examples/stats_descriptives2.py make_plot

   Plot generated by ``Descriptive`` class

Example: Monte Carlo approximation
----------------------------------

Given two independent random variables $X$ and $Y$, one might wish to
compute probabilities like $P(X < Y)$ or $P(|X - Y| < 5)$. In the
first case, this amounts to evaluating a potentially hairy integral

.. math::

   \int_{-\infty}^\infty \int_{-\infty}^y f_X(x) f_Y(y) dx\> dy.

Assuming we know how to sample from the respective distributions of
$X$ and $Y$, a common computational approach is called *Monto Carlo
approximation*, which is a fancy way of saying: generate a bunch of
samples from $X$ and $Y$ and compute the empirical statistic. For $P(X
< Y)$, we could write a reusable function accepting arbitrary
``scipy.stats`` distributions:

.. sourcecode:: python

    def prob_x_lt_y(xdist, ydist, nsamples=1000):
	xsamples = xdist.rvs(nsamples)
	ysamples = ydist.rvs(nsamples)

	return (xsamples < ysamples).mean()

    prob_x_lt_y(beta(2, 3), beta(3, 2))

Of course, there is a whole body of literature on how well this method
approximates the above integral, but that is outside of the scope of
this book.  Note that using this method we could have computed $P(|X -
Y| < 5)$ by changing only one line of code, while the respective
integral would be more complicated to write down.

Example: Example 2 here
-----------------------

Example: Example 3 here
-----------------------

Other ``scipy.stats`` goodies
-----------------------------

In large part we will refer the reader to NumPy's and SciPy's
documentation and source code to find other statistical tools of
interest. Unfortunately still as of this writing there are some parts
of ``scipy.stats`` without documentation, so reading the actual source
code (easy to find online) may at times be necessary (reading other
people's code is good practice, anyway).

We will mention a couple of additional useful tools in the package;
what we have described here is by no means exhaustive.

Kernel Density Estimation: ``scipy.stats.kde``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A common task in exploratory data analysis is that of approximating a
probability density given a set of data. In general, this is a
difficult problem which has been studied by many different
researchers. By *kernel density estimation* we usually mean inferring
a mixture of random variables (also known as kernels) which might have
generated the input data set. ``scipy.stats.kde`` provides the
``gaussian_kde`` class which uses a mixture of normal distributions to
fit the data.

Using this class is easy: create a instance with your (1-dimensional)
data set, then call its ``evaluate`` method. We generate some data
from a mixture of Normal(0, 1) and Normal(4, 1) random variables and
plot its density estimate with the following code:

.. sourcecode:: python

    data = np.concatenate((np.random.normal(0, 1, 100),
                           np.random.normal(4, 1, 100)))
    kde = stats.kde.gaussian_kde(data)
    plt.hist(data, bins=20, normed=True, color='gray',
             rwidth=0.5)
    plot_function(kde.evaluate, -10, 10, style='k')

.. plot:: examples/stats_graphs_kde.py

   Kernel density estimate of mix of N(0, 1) and N(4, 1)

As we can see, it does a reasonably good job of estimating the true
density.

Other Python statistical libraries of interest
----------------------------------------------

* ``rpy`` / ``rpy2``: Call R functions transparently through Python
* ``pymc``: Bayesian Markov Chain Monte Carlo algorithms
* ``scikits.learn``: Machine learning algorithms

``scikits.statsmodels``: Econometrics and regression models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

