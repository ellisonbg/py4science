=================================================
 Introductory Spectral Methods for Data Analysis
=================================================

Fourier expansions
==================

In general, a Fourier series is a sum of the form

.. math::

   f(t) = \sum_{n=-\infty}^{n=\infty}{c_n e^{int}}

For example, a square wave is represented by the expansion:

.. math::

   f(t)=\sum_{n=1, \mathrm{odd}}^{\infty}\frac{1}{n}\sin(n t)=\sin(t)+\frac{1}{3}\sin(3t)+\frac{1}{5}\sin(5t)+\ldots

This can be computed with the code::

    def square_terms(nterms=5, npts=500):
	t = np.linspace(-pi, 2*pi, npts)
	terms = np.zeros((nterms, npts))
	for i in range(nterms):
	    terms[i] = (1.0/(2*i+1))*sin( (2*i+1)* t)
	y = terms.sum(axis=0)
	return t, y, terms

If we use a low number of terms, we get something like:

.. plot::
   :include-source:

   from examples.spectral import elementary_fourier as ef
   ef.plot_square_terms(3)


As we increase the number of terms:

.. plot::
   :include-source:

   from examples.spectral import elementary_fourier as ef
   ef.plot_square(range(1, 9, 2))

 
Notice that the ringing doesn't seem to go away.  This is called the *Gibbs
effect* and is a fundamental property of Fourier expansions:

.. plot::
   :include-source:

   from examples.spectral import elementary_fourier as ef
   ef.plot_square([5,10,30,50])
   plt.xlim(-0.5, 2)
   plt.ylim(0.5, 1)

Even going to very high orders doesn't help:
   
.. plot::
   :include-source:

   from examples.spectral import elementary_fourier as ef
   ef.plot_square(100)

Using Cesaro summation can alleviate this problem.  Instead of using only the
final sum with all $n$ terms, we average all the intermediate sums.  Each
partial sum is defined as:

.. math::

   f_{n}(t)=\sum_{i=1, \mathrm{odd}}^{n-1}\frac{1}{i}\sin(it)

and if we average all of them, we get beneficial cancellation:

.. math::

   \tilde{f}(t)=\frac{1}{n}\sum_{i=0}^{n-1}f_{i}(t)

In code::

    t, y, terms = square_terms(nterms)
    csum = terms.cumsum(axis=0)
    yc = csum.mean(axis=0)

Let's see the results:
   
.. plot::
   :include-source:

   from examples.spectral import elementary_fourier as ef
   ef.plot_square([3,5,7])
   ef.plot_cesaro(7)

And zooming in:

.. plot::
   :include-source:

   from examples.spectral import elementary_fourier as ef
   ef.plot_square([10, 50])
   ef.plot_cesaro(10)
   ef.plot_cesaro(50)
   plt.xlim(-0.5, 2)
   plt.ylim(0.5, 1)


Data windowing, or tapering
===========================

Define PSD - continuum.

Illustrate windows.

Multitaper example in nitime.