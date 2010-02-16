#!/usr/bin/env python
"""Root finding using SciPy's Newton's method routines.
"""

from math import sin

from scipy.integrate import quad
from scipy.optimize import newton

# test input function
def f(t):
    return t*(sin(t))**2

def g(t):
    "Exact form for g by integrating f(t)"
    u = 0.25
    return .25*(t**2-t*sin(2*t)+(sin(t))**2)-u

def gn(t):
    "g(t) obtained by numerical integration"
    u = 0.25
    return quad(f,0.0,t)[0] - u

# main
tguess = 10.0

print '"Exact" solution (knowing the analytical form of the integral)'
t0 = newton(g,tguess,f)
print "t0, g(t0) =",t0,g(t0)

print
print "Solution using the numerical integration technique" 
t1 = newton(gn,tguess,f)
print "t1, g(t1) =",t1,g(t1)

print
print "To six digits, the answer in this case is t==1.06601."
