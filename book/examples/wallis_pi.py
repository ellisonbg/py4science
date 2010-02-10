#!/usr/bin/env python
"""Simple demonstration of Python's arbitrary-precision integers."""

# We need exact division between integers as the default, without manual
# conversion to float b/c we'll be dividing numbers too big to be represented
# in floating point.
from __future__ import division

def pi(n):
    """Compute pi using n terms of Wallis' product.

    Wallis' formula approximates pi as

    pi(n) = 2 \prod_{i=1}^{n}\frac{4i^2}{4i^2-1}."""
    
    num = 1
    den = 1
    for i in xrange(1,n+1):
	tmp = 4*i*i
	num *= tmp
	den *= tmp-1
    return 2.0*(num/den)

# This part only executes when the code is run as a script, not when it is
# imported as a library
if __name__ == '__main__':
    # Simple convergence demo.

    # A few modules we need
    from matplotlib import pyplot as plt
    import numpy as np

    # Create a list of points 'nrange' where we'll compute Wallis' formula
    nrange = np.linspace(10,2000,20).astype(int)
    # Make an array of such values
    wpi = np.array(map(pi,nrange))
    # Compute the difference against the value of pi in numpy (standard
    # 16-digit value)
    diff = abs(wpi-np.pi)

    # Make a new figure and build a semilog plot of the difference so we can
    # see the quality of the convergence
    plt.figure()
    # Line plot with red circles at the data points
    plt.semilogy(nrange,diff,'-o',mfc='red')

    # A bit of labeling and a grid
    plt.title(r"Convergence of Wallis' product formula for $\pi$")
    plt.xlabel('Number of terms')
    plt.ylabel(r'Absolute Error')
    plt.grid()

    # Display the actual plot
    plt.show()
