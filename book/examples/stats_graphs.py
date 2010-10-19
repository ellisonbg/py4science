"""
Bayesian statistics and then some
"""

from __future__ import division

import numpy as np

from matplotlib import ticker, cm
import scipy.stats as stats
import scipy.optimize as opt
import scipy.special as special
import scipy.integrate as integ
import matplotlib.pyplot as plt

from scipy.special import gamma, gammaln, binom

def quantile(data, quantiles, axis=None):
    """
    Dumb
    """
    from scipy.stats import scoreatpercentile as _q
    return np.array([_q(data, quantile * 100)
                     for quantile in quantiles])

def effective_size(theta_mcmc):
    from rpy2.robjects import FloatVector
    from rpy2.robjects.packages import importr

    coda = importr('coda')
    es = coda.effectiveSize(FloatVector(theta_mcmc))
    return es[0]

#-------------------------------------------------------------------------------
# Graphing functions

def joint_contour(z_func, xlim=(0, 1), ylim=(0, 1), n=50,
                  ncontours=20):
    x = np.linspace(*xlim, num=n)
    y = np.linspace(*ylim, num=n)

    X, Y = np.meshgrid(x, y)

    plt.figure()
    cs = plt.contourf(X, Y, z_func(X, Y), ncontours, cmap=cm.gray_r)
    plt.colorbar()
    plt.xlim(xlim)
    plt.ylim(ylim)

def _joint_normal(mu, s2, k, nu, X, Y):
    s2_vals = stats.gamma.pdf(Y, nu / 2, scale=2. / (s2 * nu))
    theta_vals = stats.norm.pdf(X, mu, 1 / np.sqrt(Y * k))

    return s2_vals * theta_vals

def graph_data(f, xstart=0, xend=1, n=1000):
    inc = (xend - xstart) / n
    xs = np.arange(xstart, xend + inc, inc)

    ys = f(xs)

    return xs, ys

def plotf(f, xstart=0, xend=1, n=1000, style='b', axes=None, label=None):
    """
    Continuous
    """
    xs, ys = graph_data(f, xstart=xstart, xend=xend, n=n)
    if axes is not None:
        plt.plot(xs, ys, style, label=label, axes=axes)
    else:
        plt.plot(xs, ys, style, label=label)

    # plt.vlines(xs, [0], ys, lw=2)

    plt.xlim([xstart - 1, xend + 1])

def plot_function(f, xstart=0, xend=1, n=1000, style='b'):
    increment = (xend - xstart) / n
    xs = np.arange(xstart, xend + increment, increment)
    ys = f(xs)
    plt.plot(xs, ys, style)
    plt.xlim([xstart - 1, xend + 1])


def plot_pdf(dist, **kwds):
    plotf(dist.pdf, **kwds)

def plot_discrete_pdf(f, xstart=0, xend=100, style='b', axes=None,
                      label=None):
    n = xend - xstart
    xs, ys = graph_data(f, xstart=xstart, xend=xend, n=n)

    print xs, ys

    plt.vlines(xs, [0], ys, lw=2)
    # plt.plot(xs, ys, style, label=label)
    plt.xlim([xstart - 1, xend])

def posterior_ci_plot(dist, ci=[0.025, 0.975]):
    pass

def make_plot(x, y, style='k', title=None, xlabel=None, ylabel=None, path=None):
    plt.figure(figsize=(10,5))
    plt.plot(x, y, style)
    adorn_plot(title=title, ylabel=ylabel, xlabel=xlabel)
    plt.savefig(path, bbox_inches='tight')

def adorn_plot(title=None, ylabel=None, xlabel=None):
    plt.title(title, fontsize=16)
    plt.ylabel(ylabel, fontsize=16)
    plt.xlabel(xlabel, fontsize=16)

def ex_p6():
    plt.figure()

    w = 5.

    colors = 'bgrcm'

    for i in range(1, 5):
        theta_0 = 0.2 * i
        dist = stats.beta(w * theta_0, w * (1 - theta_0))

        plotf(dist.pdf, style=colors[i], label=str(theta_0))

    plt.legend(loc='best')

def all_perms(iterable):
    if len(iterable) <=1:
        yield iterable
    else:
        for perm in all_perms(iterable[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + iterable[0:1] + perm[i:]

#-------------------------------------------------------------------------------
# Plots for statistics chapter

def fig_norm_hist():
    my_figure()
    samples = np.random.randn(10000)
    plt.hist(samples, bins=100, normed=True, color='gray',
             rwidth=0.5)
    plot_function(stats.norm.pdf, -4, 4, style='k')

def fig_beta_pdfs():
    my_figure()
    plotf(stats.beta(2, 4).pdf, style='k--')
    plotf(stats.beta(4, 2).pdf, style='k')
    plt.xlim([0, 1])
    plt.legend((r'Beta(2, 4)', r'Beta(4, 2)'), loc='best')
    # my_savefig('fig/stats_betapdfs.pdf')

def fig_normal_pdf_cdf():
    my_figure()
    plotf(stats.norm.pdf, -4, 4, style='k')
    plotf(stats.norm.cdf, -4, 4, style='k--')
    plt.xlim([-4, 4])
    plt.title(r'Normal(0, 1) PDF and CDF')
    plt.legend((r'PDF', 'CDF'), loc='best')

def fig_kde():
    my_figure()
    np.random.seed(1234)
    data = np.concatenate((np.random.normal(0, 1, 100),
                           np.random.normal(4, 1, 100)))

    kde = stats.kde.gaussian_kde(data)

    plt.hist(data, bins=20, normed=True, color='gray',
             rwidth=0.5)
    plot_function(kde.evaluate, -10, 10, style='k')

    plt.xlim([-6, 10])

def my_figure():
    plt.figure(figsize=(10, 5))

def my_savefig(path):
    plt.savefig(path, dpi=150, bbox_inches='tight')


if __name__ == '__main__':
    # make_plots()

    fig_kde()
    plt.show()
