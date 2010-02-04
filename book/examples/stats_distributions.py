"""
Illustrate the connections bettwen the uniform, exponential, gamma and
normal distributions by simulating waiting times from a radioactive
source using the random number generator.  Verify the numerical
results by plotting the analytical density functions from scipy.stats
"""
import numpy
import scipy.stats
from pylab import figure, show, close


# N samples from a uniform distribution on the unit interval.  Create
# a uniform distribution from scipy.stats.uniform and use the "rvs"
# method to generate N uniform random variates
N = 100000
uniform = scipy.stats.uniform()  # the frozen uniform distribution
uninse = uniform.rvs(N)          # the random variates

# in each time interval, the probability of an emission 
rate = 20.  # the emission rate in Hz
dx = 0.001  # the sampling interval in seconds
t = numpy.arange(N)*dx  # the time vector

# the probability of an emission is proportionate to the rate and the interval
emit_times = t[uninse < rate*dx]

# the difference in the emission times is the wait time
wait_times = numpy.diff(emit_times)  

# plot the distribution of waiting times and the expected exponential
# density function lambda exp( lambda wt) where lambda is the rate
# constant and wt is the wait time; compare the result of the analytic
# function with that provided by scipy.stats.exponential.pdf; note
# that the scipy.stats.expon "scale" parameter is inverse rate
# 1/lambda.  Plot all three on the same graph and make a legend.
# Decorate your graphs with an xlabel, ylabel and title
fig = figure()
ax = fig.add_subplot(311)
p, bins, patches = ax.hist(wait_times, 100, normed=True)
l1, = ax.plot(bins, rate*numpy.exp(-rate * bins), lw=2, color='red')
l2, = ax.plot(bins, scipy.stats.expon.pdf(bins, 0, 1./rate),
        lw=2, ls='--', color='green')

ax.set_ylabel('PDF')
ax.set_title('waiting time densities of a %dHz Poisson emitter'%rate)
ax.text(0.05, 0.9, 'one interval', transform=ax.transAxes)
ax.legend((patches[0], l1, l2), ('simulated', 'analytic', 'scipy.stats.expon'))


# plot the distribution of waiting times for two events; the
# distribution of waiting times for N events should equal a N-th order
# gamma distribution (the exponential distribution is a 1st order
# gamma distribution.  Use scipy.stats.gamma to compare the fits.
# Hint: you can stride your emission times array to get every 2nd
# emission
wait_times2 = numpy.diff(emit_times[::2])
ax = fig.add_subplot(312)
p, bins, patches = ax.hist(wait_times2, 100, normed=True)
l1, = ax.plot(bins, scipy.stats.gamma.pdf(bins, 2, 0, 1./rate),
        lw=2, ls='-', color='red')

ax.set_ylabel('PDF')
ax.text(0.05, 0.9, 'two intervals', transform=ax.transAxes)
ax.legend((patches[0], l1), ('simulated', 'scipy.stats.gamma'))

# plot the distribution of waiting times for 10 events; again the
# distribution will be a 10th order gamma distribution so plot that
# along with the empirical density.  The central limit thm says that
# as we add N independent samples from a distribution, the resultant
# distribution should approach the normal distribution.  The mean of
# the normal should be N times the mean of the underlying and the
# variance of the normal should be 10 times the variance of the
# underlying.  HINT: Use scipy.stats.expon.stats to get the mean and
# variance of the underlying distribution.  Use scipy.stats.norm to
# get the normal distribution.  Note that the scale parameter of the
# normal is the standard deviation which is the square root of the
# variance
expon_mean, expon_var = scipy.stats.expon(0, 1./rate).stats()
mu, var = 10*expon_mean, 10*expon_var
sigma = numpy.sqrt(var)
wait_times10 = numpy.diff(emit_times[::10])
ax = fig.add_subplot(313)
p, bins, patches = ax.hist(wait_times10, 100, normed=True)
l1, = ax.plot(bins, scipy.stats.gamma.pdf(bins, 10, 0, 1./rate),
        lw=2, ls='-', color='red')
l2, = ax.plot(bins, scipy.stats.norm.pdf(bins, mu, sigma),
        lw=2, ls='--', color='green')

ax.set_xlabel('waiting times')
ax.set_ylabel('PDF')
ax.text(0.1, 0.9, 'ten intervals', transform=ax.transAxes)
ax.legend((patches[0], l1, l2), ('simulated', 'scipy.stats.gamma', 'normal approx'))

fig.savefig('stats_distributions.png', dpi=150)
fig.savefig('stats_distributions.eps')


show()
