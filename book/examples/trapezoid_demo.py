"""Graphical demonstration of numerical integration via trapezoid rule.
"""

import numpy as np
from  matplotlib import pyplot as plt

# Local imports
import trapezoid as trap

# Function definitions
def func(x):
    return (x-3)*(x-5)*(x-7)+85

# Main script
if __name__ == '__main__':

    # Plot function on a fine grid
    ap, bp = 0, 10
    xp = np.linspace(ap, bp, 200)
    yp = func(xp)

    ax = plt.subplot(111)
    ax.plot(xp, yp, linewidth=1)

    # Display trapezoid rule errors by sampling just a few points
    a, b = 2, 9 # integral area
    npts = 4

    # make the shaded region
    ix = np.linspace(a, b, npts)
    iy = func(ix)
    verts = [(a,0)] + zip(ix,iy) + [(b,0)]
    poly = plt.Polygon(verts, facecolor='0.8', edgecolor='k')
    ax.add_patch(poly)
    ax.scatter(ix, iy, zorder=2)

    # Fancify plot with labels and clean axes
    plt.text(0.5 * (a + b), 30,
         r"$\int_a^b f(x)\mathrm{d}x$", horizontalalignment='center',
         fontsize=20)
    plt.axis([0,10, 0, 180])
    plt.figtext(0.9, 0.05, 'x')
    plt.figtext(0.1, 0.9, 'y')
    plt.title('Trapezoid rule integration')
    ax.set_xticks((a,b))
    ax.set_xticklabels(('a','b'))
    ax.set_yticks([])
    plt.show()
