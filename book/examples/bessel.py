#!/usr/bin/env python
"""Illustrate some well-known properties of the Bessel functions."""

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy import special

#-----------------------------------------------------------------------------
# Function definitions
#-----------------------------------------------------------------------------
def jn_asym_sx(n, x):
    r"""Asymptotic form of Jn(x) for small x.

    Redo the above, for the asymptotic range :math:`0 <x << \sqrt{n}`.  The
    asymptotic form in this regime is:

    .. math::

       J_n(x) \approx \frac{1}{\Gamma(n+1)} \left( \frac{x}{2} \right) ^n


    Parameters
    ----------
    n : int
        Order of the Bessel function.

    x : float or array
        Argument to the Bessel function.

    Returns
    -------
    j : array
        Approximate Value of Jn(x)."""
    
    return ((x/2.0)**n)/special.gamma(n+1)


def jn_asym_lx(n,x):
    r"""Asymptotic form of Jn(x) for large x.

    Redo the above, for the asymptotic range :math:`x >> n^2`.  The
    asymptotic form in this regime is:

    .. math::

       J_n(x) \approx \sqrt{\frac{2}{\pi x}}
                  \cos \left( x- \frac{n\pi}{2} - \frac{\pi}{4} \right)


    Parameters
    ----------
    n : int
        Order of the Bessel function.

    x : float or array
        Argument to the Bessel function.

    Returns
    -------
    j : array
        Approximate Value of Jn(x)."""

    return np.sqrt(2.0/np.pi/x)*np.cos(x-(n*np.pi/2.0+np.pi/4.0))


def show_asymptotic(nvals, x, x_asym, jn_asym):
    """Illustrate an asymptotic relation.

    This function creates a matplotlib figure.

    Parameters
    ----------

    nvals : list
        List of values of n (Bessel order) to evaluate.

    x : array
        Array of values where the function should be sampled.

    x_asym : function
        A function taking (n, x) arguments that should return the values of x
        where the desired asymptotic form is valid.

    jn_asym : function
        A function taking (n, x) arguments and returning an asymptotic form of
        the Bessel function Jn(x).

    Returns
    -------
    fig : matplotlib figure object.
        A new figure containing all the plots.
    """

    # Start by plotting the well-known J0 and J1, as well as J5:
    fig = plt.figure()
    # Now, compute and plot the asymptotic forms (valid for x>>n, where n is
    # the order).  We must first find the valid range of x where at least x>n.
    for n in nvals:
        xa = x_asym(n, x)
        plt.plot(x, special.jn(n, x), label='$J_{%s}$' % n)
        plt.plot(xa, jn_asym(n, xa), '--', lw=3,
                 label='$J_{%s}$ (asymp.)' % n)

    # Finish off the plot
    plt.legend(loc='best')
    # horizontal line at 0 to show x-axis, but after the legend
    plt.axhline(0)
    return fig


def show_asymptotic_large(nvals, x):
    """Illustrate the asymptotic relation for large x.

    Parameters
    ----------

    nvals : list
      List of values of n (Bessel order) to evaluate.

    x : array
      Array of values where the function should be sampled.
    """

    x_asym = lambda n, x: x[x > n**2]
    show_asymptotic(nvals, x, x_asym, jn_asym_lx)
    plt.title('Bessel Functions, large x')


def show_asymptotic_small(nvals, x):
    """Illustrate the asymptotic relation for small x.

    Parameters
    ----------

    nvals : list
      List of values of n (Bessel order) to evaluate.

    x : array
      Array of values where the function should be sampled.
    """

    x_asym = lambda n, x: x[x < np.sqrt(n)]
    show_asymptotic(nvals, x, x_asym, jn_asym_sx)
    plt.title('Bessel Functions, small x')


def show_recursion_rel(n, x):
    """Verify numerically the Bessel recursion relation.

    The relation reads:
    J(n+1,x) = (2n/x)J(n,x)-J(n-1,x).

    Parameters
    ----------

    x : array
      Values where the relation will be evaluated.

    n : int
      Order of the function to check."""
    
    jn = special.jn  # just a shorthand

    # Be careful to check only for x!=0, to avoid divisions by zero
    xp = x[x>0.0]

    # construct both sides of the recursion relation, these should be equal
    j_np1 = jn(n+1,xp)
    j_np1_rec = (2.0*n/xp)*jn(n,xp)-jn(n-1,xp)

    # Now make a nice error plot of the difference, in a new figure
    plt.figure()
    plt.semilogy(xp,abs(j_np1-j_np1_rec),'r+-')
    plt.title('Error in recursion for $J_%s$' % n)
    plt.grid()


if __name__ == '__main__':
    # build ranges for x to plot in for each type of asymptotic form
    xs = np.linspace(0,3,400)
    xl = np.linspace(0,35,400)
    # Make figures
    show_asymptotic_large([0, 1, 5], xl)
    show_asymptotic_small([4, 5, 6], xs)
    show_recursion_rel(5, xl)
    # Don't forget a show() call at the end of the script
    plt.show()
