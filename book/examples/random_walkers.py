import numpy as np
import matplotlib.pyplot as plt

mu = 0.01
sigma = 0.1

walkers = 200
Nsteps = 1000

t = np.arange(Nsteps)
# the random walk
steps = (mu + sigma*np.random.randn(walkers, Nsteps))
X = steps.cumsum(axis=1)

# the empirical mean and standard deviation
mux = X.mean(axis=0)
sigmax = X.std(axis=0)

fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212, sharex=ax1)

ax1.plot(t, mux, lw=1, label='empirical')
ax1.plot(t, mu*t, lw=2, label='analytic')
ax1.set_ylabel('Population mean')
ax1.grid()
leg = ax1.legend(loc='upper left')
leg.get_frame().set_alpha(0.5)

ax2.plot(t, sigmax, lw=1)
ax2.plot(t, sigma*np.sqrt(t), lw=2)
ax2.set_ylabel('Population std')
ax2.grid()

Nplot = 23  # plot a few samples
fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(t, X[:Nplot].T)
ax.plot(t, mu*t, lw=2)
ax.fill_between(t, mu*t + sigma*np.sqrt(t),
                mu*t - sigma*np.sqrt(t), facecolor='yellow',
                alpha=0.5)
                
plt.show()
