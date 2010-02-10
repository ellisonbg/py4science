#!/usr/bin/env python
"""Simple trapezoid-rule integrator."""

import numpy as np

def trapz(x, y):
    """Simple trapezoid integrator for sequence-based innput.

    Inputs:
      - x,y: arrays of the same length (and more than one element).  If the two
    inputs have different lengths, a ValueError exception is raised.

    Output:
      - The result of applying the trapezoid rule to the input, assuming that
      y[i] = f(x[i]) for some function f to be integrated.

    Minimally modified from matplotlib.mlab."""

    # Sanity checks.
    if len(x) != len(y):
        raise ValueError('x and y must have the same length')
    if len(x) < 2:
        raise ValueError('x and y must have > 1 element')

    # Efficient application of trapezoid rule via numpy
    return 0.5*((x[1:]-x[:-1])*(y[1:]+y[:-1])).sum()

def trapzf(f,a,b,npts=100):
    """Simple trapezoid-based integrator.

    Inputs:
      - f: function to be integrated.

      - a,b: limits of integration.

    Optional inputs:
      - npts(100): the number of equally spaced points to sample f at, between
      a and b.

    Output:
      - The value of the trapezoid-rule approximation to the integral."""


    # Generate an equally spaced grid to sample the function.
    x = np.linspace(a,b,npts)

    # For an equispaced grid, the x spacing can just be read off from the first
    # two points and factored out of the summation.
    dx = x[1]-x[0]

    # Sample the input function at all values of x
    y = np.array(map(f,x))

    # Compute the trapezoid rule sum for the final result
    return 0.5*dx*(y[1:]+y[:-1]).sum()


#-----------------------------------------------------------------------------
# Tests
#-----------------------------------------------------------------------------
import nose, nose.tools as nt
import numpy.testing as nptest

# A simple function for testing
def square(x): return x**2

def test_err():
    """Test that mismatched inputs raise a ValueError exception."""
    nt.assert_raises(ValueError,trapz,range(2),range(3))

def test_call():
    "Test a direct call with equally spaced samples. "
    x = np.linspace(0,1,100)
    y = np.array(map(square,x))
    nptest.assert_almost_equal(trapz(x,y),1./3,4)

def test_square():
    "Test integrating the square() function."
    nptest.assert_almost_equal(trapzf(square,0,1),1./3,4)

def test_square2():
    "Another test integrating the square() function."
    nptest.assert_almost_equal(trapzf(square,0,3,350),9.0,4)


# If called from the command line, run all the tests
if __name__ == '__main__':
    # This call form is ipython-friendly
    nose.runmodule(argv=['-s','--with-doctest'],
                   exit=False)
