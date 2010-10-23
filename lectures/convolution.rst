Convolution
===========

.. ipython::
   :suppress:

   # set up ipython for plotting in pylab
   In [3]: from pylab import *

   In [4]: plt.close('all')

   In [5]: ion()

   In [6]: bookmark ipy_start

In signal processing, the output of a linear system to an arbitrary
input is given by the convolution of the impule response function (the
system response to a Dirac-delta impulse) and the input signal.

Mathematically  :math:`y(t) = \int_0^t x(\tau)r(t-\tau)d\tau`

where :math:`x(t)` is the input signal at time :math:`t`, :math:`y(t)`
is the output, and :math:`r(t)` is the impulse response function.

In this exercise, we will compute the convolution of an impulse traine
and a white noise process with a double exponential impulse response
function using ``np.convolve``.  We compare the results with those
obtained in Fourier space to illustrate that a convolution in the
temporal domain is a multiplication in the fourier domain.

First we define a stepsize ``dt``, and a time vector ``t``, and the
impuse response vector ``r``.

.. ipython::

   # the stepsize
   In [242]: dt = 0.01

   # the time vector from 0..20
   In [243]: t = np.arange(0.0, 20.0, dt)        

   In [244]: Nt = len(t)

   # the impulse response 
   In [245]: r = (np.exp(-t) - np.exp(-5*t))*dt

   In [246]: plt.plot(t, r);

   In [247]: plt.xlabel('time');

   @savefig convolution_impulse_response.png
   In [248]: plt.ylabel('impuse response');

A common task in computational neurobiology is to simulate the
membrane voltage of a neuron receiving an incoming stream of action
potentials.  The action potentials are modeled as a series of pulses
(Dirac delta functions), and the membrane voltage is assumed to be
given by the convolution of the action potentials with the synaptic
response function, which to a first order approximation is similar to
the response function plotted above, and is often modeled as the
difference of two exponentials (as above) or as a low order gamma
function, which has a similar shape.  A common assumption is that the
action potentials have a Poisson distribution, which means that the
waiting time between pulses is exponentially distributed and the
probability of a pulse in any given time interval is equal.  Using the
uniform random number distribution, we can easily model the Poisson
distribution of Dirac delta pulses as follows.

.. ipython::

   In [281]: spikes = np.zeros_like(t)

   In [282]: rate = 2  # an emission rate in Hz

   In [283]: nse = np.random.rand(len(t))

   # we divide the spike height by dt because the Dirac distribution
   # (the impulse) should integrate to 1
   In [284]: spikes[nse<rate*dt] =  1./dt

   In [285]: voltage = np.convolve(spikes, r, mode='full')

   In [286]: len(spikes)
   Out[286]: 2000

   In [287]: len(r)
   Out[287]: 2000
 
   # the length of the convolution is equal to the sum of the lengths
   # of the two input vectors minus 1 
   In [288]: len(voltage) 
   Out[288]:
   3999

Although in this example, the length of the two inputs, the spikes and
the impulse response vector, are the same, though they need not be.
The output of the convolution of ``np.convolve(a, v, mode='full')``
will be ``len(a) + len(v) - 1``.  For our data this is :math:`2000 +
2000 -1 = 3999`.

We now plot the input spike train and output membrane voltage below.

.. ipython::

  In [298]: fig, (ax1, ax2) = plt.subplots(2, sharex=True)

  In [299]: ax1.plot(t, spikes); ax1.set_ylabel('spikes');

  In [300]: ax2.plot(t, voltage[:Nt]); ax2.set_ylabel('voltage');

  @savefig convolution_spikes.png
  In [302]: ax2.set_xlabel('time (s)');
