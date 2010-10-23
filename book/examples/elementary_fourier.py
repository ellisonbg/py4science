"""Introduction to Fourier analysis.

We illustrate the basic construction of a square wave with successively higher
order approximations.
"""

#-----------------------------------------------------------------------------
# Library imports
#-----------------------------------------------------------------------------

import numpy as np
from matplotlib import pyplot as plt
from numpy import pi, sin, cos

#-----------------------------------------------------------------------------
# Function definitions
#-----------------------------------------------------------------------------

def square(nterms=5, npts=2000):
    """Add nterms to construct a square wave.

    Computes an approximation to a square wave using a total of nterms.
    
    Parameters
    ----------
    nterms : int, optional
      Number of terms to use in the sum.
    npts : int, optional
      Number of points at which to sample the function.

    Returns
    -------
    t : array
      The t values where the wave was sampled.
    y : array
      The square wave approximation (the final sum of all terms).
      """
    
    t = np.linspace(-pi, 2*pi, npts)
    y = np.zeros_like(t)

    for i in range(nterms):
        y += (1.0/(2*i+1))*sin( (2*i+1)* t)

    return t, y


def square_terms(nterms=5, npts=500):
    """Compute all nterms to construct a square wave.

    Computes an approximation to a square wave using a total of nterms, and
    returns the individual terms as well as the final sum.
    
    Parameters
    ----------
    nterms : int, optional
      Number of terms to use in the sum.
    npts : int, optional
      Number of points at which to sample the function.

    Returns
    -------
    t : array
      The t values where the wave was sampled.
    y : array
      The square wave approximation (the final sum of all terms).
    terms : array of shape (nterms, npts)
      Array with each term of the sum as one row.
      """
    t = np.linspace(-pi, 2*pi, npts)
    terms = np.zeros((nterms, npts))
    for i in range(nterms):
        terms[i] = (1.0/(2*i+1))*sin( (2*i+1)* t)
    y = terms.sum(axis=0)
    return t, y, terms


def plot_square(terms):
    """Plot the square wave construction for a list of total number of terms.

    Parameters
    ----------
    terms : int or list of ints
      If a list is given, the plot will be constructed for all terms in it.
    """
    plt.figure()

    if isinstance(terms, int):
        # Single term, just put it in a list since the code below expects a list
        terms = [terms]
        
    for nterms in terms:
        t, y = square(nterms)
        plt.plot(t, y, label='n=%s' % nterms)

    plt.grid()
    plt.legend()
    plt.title('Square wave with n terms')


def plot_square_terms(nterms):
    """Plot individual terms of square wave construction."""
    plt.figure()

    t, y, terms = square_terms(nterms)
    for i,term in enumerate(terms):
        plt.plot(t, term, label='freq=%i' % (2*i+1))
        
    plt.plot(t, y, color='k', linewidth=2, label='sum')
    plt.grid()
    plt.legend()
    plt.title('Individual components of a square wave')


def plot_cesaro(nterms):
    """Cesaro summation"""
    t, y, terms = square_terms(nterms)
    csum = terms.cumsum(axis=0)
    yc = csum.mean(axis=0)
    plt.plot(t, yc, label='cesaro(%s)' % nterms)
    plt.legend()

#-----------------------------------------------------------------------------
# Main script
#-----------------------------------------------------------------------------

if __name__ == '__main__':
    
    # First plot the full construction for low # of terms
    plot_square_terms(3)

    # Then show how successive approximations work
    plot_square(range(1, 9, 2))

    # Finally, illustrate Gibbs effect
    plot_square([5,10,30,50])
    
    plot_square(100)

    # Then show how successive approximations work
    plot_square([3,5,7])
    plot_cesaro(7)

    # Display figures
    plt.show()
