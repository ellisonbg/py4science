"""Illustrating error propagation by iterating the logistic map.

Inspired by :http://us.pycon.org/2009/conference/schedule/event/65/
"""

import matplotlib.pyplot as plt

# Interesting values to try for r:
# [1.9, 2.9, 3.1, 3.5, 3.9]
r = 3.9 # global default
x0 = 0.6  # any number in [0,1] will do here

num_points = 100  # total number of points to compute
drop_points = 0  # don't display the first drop_points

def f1(x): return r*x*(1-x)
def f2(x): return r*x - r*x**2
def f3(x): return r*(x-x**2)

# Main script
fp = (r-1.0)/r
x1 = x2 = x3 = x0
data = []
data.append([x1,x2,x3])
for i in range(num_points):
    x1 = f1(x1)
    x2 = f2(x2)
    x3 = f3(x3)
    data.append([x1,x2,x3])

# Display the results
plt.figure()
plt.title('r=%1.1f' % r)
plt.axhline(fp, color='black')
plt.plot(data[drop_points:], '-o', markersize=4)
plt.show()
