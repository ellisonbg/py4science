import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq

nwalkers = 50
nsteps = 100
Steps = np.random.normal(size=(nsteps, nwalkers))

Position = Steps.cumsum(axis=0)

sigma = Position.std(axis=1)
mu = Position.mean(axis=1)

t = np.arange(nsteps)

def fitfunc(pars):
    alpha = pars[0]
    return t**alpha

def errfunc(pars):
    return sigma - fitfunc(pars)

alpha_true = 0.5
guess = 0.7
alpha_fit, mesg = leastsq(errfunc, guess)

print 'Least-squares fit to the data'
print 'true', alpha_true
print 'best', alpha_fit

plt.figure()
plt.plot(t, mu, 'b--', lw=2, label='empirical mean')
plt.plot(t,np.zeros(nsteps), 'b-', lw=2, label='analytical mean')
plt.plot(t, sigma, 'g--', lw=2, label='empirical std')
plt.plot(t, t**alpha_fit, 'g-.', lw=2, label='empirical exp')
plt.plot(t, t**alpha_true, 'g-', lw=2, label='analytical std')
leg = plt.legend(loc='upper left')
plt.show()
