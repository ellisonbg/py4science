import numpy as np

def f(x):
    return x**2

def trap_loop(x, y):
    integral = 0.0
    for i in xrange(1, len(x)):
        integral += (x[i] - x[i-1])*(y[i]+y[i-1])
    return integral/2.0

def trap_arr(x, y):
    return 0.5*((x[1:]-x[:-1])*(y[1:]+y[:-1])).sum()

a, b = 0, 2
npts = 100000
x = np.linspace(a, b, npts)
y = f(x)

# Here, compute and print the trapezoid approximation to integral(f(x), x)
print 'integral:', trap_loop(x, y), 'exact:', 8/3.0
