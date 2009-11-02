import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

# the parameters for rabbit and fox growth and interactions
alpha, delta = 1, .25
beta, gamma = .2, .05

def derivs(state, t):
    """
    Return the derivatives of R and F, stored in the *state* vector::

       state = [R, F]

    The return data should be [dR, dF] which are the derivatives of R
    and F at position state and time *t*.
    """
    R, F = state
    dR = alpha*R - beta*R*F
    dF = gamma*R*F - delta*F
    return dR, dF

# the initial population of rabbits and foxes
R0 = 20
F0 = 10

# create a time array from 0..100 sampled at 0.1 second steps
dt = 0.1
t = np.arange(0.0, 100, dt)

# the initial [rabbits, foxes] state vector
y0 = [R0, F0]

# y is a len(t)x2 2D array of rabbit and fox populations
# over time
y = integrate.odeint(derivs, y0, t)

rabbits = y[:,0]
foxes = y[:,1]
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(t, rabbits, label='rabbits')
ax.plot(t, foxes, label='foxes')

leg = ax.legend(loc='upper left', fancybox=True, shadow=True)
leg.get_frame().set_alpha(0.5)

# R, F, dR and dF are 2D arrays giving the state and \
# direction for each rabbit, fox combination
rmax = 1.1 * rabbits.max()
fmax = 1.1 * foxes.max()
R, F = np.meshgrid(np.arange(-1, rmax),
                   np.arange(-1, fmax))
dR = alpha*R - beta*R*F
dF = gamma*R*F - delta*F

fig = plt.figure()
ax = fig.add_subplot(111)
# the quiver function will show the direction fields
#dR, dF at each point R, F
ax.quiver(R, F, dR, dF)

ax.set_xlabel('rabbits')
ax.set_ylabel('foxes')
ax.plot(rabbits, foxes, color='black')


# resample R, F,dF and dR at a higher frequency
# for smooth null-clines
R, F = np.meshgrid(np.arange(-1, rmax, 0.1),
                   np.arange(-1, fmax, 0.1))
dR = alpha*R - beta*R*F
dF = gamma*R*F - delta*F

# use matplotlib's contour function to find the level curves where
# dR/dt=0 and dF/dt=0 (the null-clines)
ax.contour(R, F, dR, levels=[0], linewidths=3, colors='blue')
ax.contour(R, F, dF, levels=[0], linewidths=3, colors='green')

ax.set_title('trajectory, direction field and null clines')

plt.show()
