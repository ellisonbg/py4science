"""
Moire patterns from random dot fields

http://en.wikipedia.org/wiki/Moir%C3%A9_pattern

See L. Glass. 'Moire effect from random dots' Nature 223, 578580 (1969).
"""
import cmath
import numpy as np
import numpy.linalg as linalg
import matplotlib.pyplot as plt


def myeig(M):
    """
    compute eigen values and eigenvectors analytically

    Solve quadratic:

      lamba^2 - tau*lambda +/- Delta = 0

    where tau = trace(M) and Delta = Determinant(M)

    if M = | a b |
           | c d |

    the trace is a+d and the determinant is a*d-b*c

    Return value is lambda1, lambda2
    """

    a,b = M[0,0], M[0,1]
    c,d = M[1,0], M[1,1]
    tau = a+d       # the trace
    delta = a*d-b*c # the determinant

    lambda1 = (tau + cmath.sqrt(tau**2 - 4*delta))/2.
    lambda2 = (tau - cmath.sqrt(tau**2 - 4*delta))/2.
    return lambda1, lambda2


# main script
# 2000 random x,y points in the interval[-0.5 ... 0.5]
X1 = np.random.rand(2,2000)-0.5


# For each type of transform, store sx, sy,  angle
transform_params = dict(saddle = (1.05, 0.95, 0.),
                        center = (1., 1., 2.5),
                        stable_focus = (0.95, 0.95, 2.5)
                        )

name =  'saddle'
#name = 'center'
#name= 'stable_focus'  # spiral

sx, sy, angle = transform_params[name]

theta = angle * cmath.pi/180.

S = np.array([[sx, 0],
              [0, sy]])

R = np.array([[np.cos(theta),  -np.sin(theta)],
              [np.sin(theta), np.cos(theta)],])

M = np.dot(S, R)  # rotate then stretch

# compute the eigenvalues using numpy linear algebra
vals, vecs = linalg.eig(M)
print 'numpy eigenvalues', vals

# compare with the analytic values from myeig
avals = myeig(M)
print 'analytic eigenvalues', avals

# transform X1 by the matrix
X2 = np.dot(M, X1)

# plot the original x,y as green dots and the transformed x, y as red
# dots
x1 = X1[0]
y1 = X1[1]
x2 = X2[0]
y2 = X2[1]


fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title(name)
ax.plot(x1, y1, 'go', x2, y2, 'ro', markersize=2)

#fig.savefig('glass_dots1.png', dpi=100)
#fig.savefig('glass_dots1.eps', dpi=100)
plt.show()
