"""Fourier synthesis of a square wave.
"""
import numpy as np
import matplotlib.pyplot as plt

def square_term(x, n):
    return (1.0/n)*np.sin(n*x)


def square_terms(x, number_terms):
    ncols = x.shape[0]
    terms = np.zeros((number_terms, ncols))
    for i in range(number_terms):
        terms[i] = square_term(x, 2*i+1)
    return terms


def square_wave(x, number_terms):
    terms = square_terms(x, number_terms)
    return terms.sum(axis=0)


npts = 2000
nterms = 100
x = np.linspace(-np.pi, 2*np.pi, npts)

plt.figure()
plt.plot(x, square_wave(x, nterms))
plt.title('Square wave with n=%s terms' % nterms)
plt.show()
