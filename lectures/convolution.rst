===========
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

The easiest way to understand convolution is as the sum of a series of
identical responses to impulses, shifted in time.  Consider a simple
exponential response function with a time constant of 1; by the useful
*five time contant rule*, we know that the signal will be 99% decayed
by 5 seconds.  We can create an impulse response vector 5 seconds long
that will capture the vast bulk of the response.

.. ipython::

   In [32]: tr = np.arange(0, 5, 0.01)

   In [33]: r = np.exp(-tr)

   In [34]: r[-1]
   Out[34]: 0.0068056644922305431

Suppose we have two input signals at ``ind1`` and ``ind2``, that the
system responds to each input with an impulse responses, and that the
total system response is give by the sum of these two impulse responses.
We'll define a longer time vector ``t`` and two impulse reponses.

.. ipython::

   @suppress
   In [34]: plt.close('all')

   In [35]: dt = 0.01

   In [36]: t = np.arange(0, 20, dt)

   In [37]: s1, s2 = np.zeros((2, len(t)))
   
   # the indicies of the two impulse times
   In [39]: ind1, ind2 = 400, 500

   # the length of the impulse response
   In [41]: N = len(tr)

   # s1 has an impulse response starting at ind1 and lasting for N
   In [42]: s1[ind1:ind1+N] = r

   In [43]: s2[ind2:ind2+N] = r

   In [44]: plt.subplot(211);

   In [45]: plt.plot(t, s1, t, s2);

   In [46]: plt.subplot(212);

   @savefig convolution_two_impulses_sum.png
   In [47]: plt.plot(t, s1+s2);


The signal in the lower panel above is the sum of the two impulse
responses, and is identical to the convolution of a signal which is
the sum of the impulses with the impulse response function.  Let's
compute the same signal with convolution.

.. ipython::

   @suppress
   In [49]: plt.close('all')

   In [50]: impulses = np.zeros_like(t)

   In [51]: impulses[ind1] = 1.

   In [52]: impulses[ind2] = 1.

   In [53]: sc = np.convolve(impulses, r)

   In [54]: plt.subplot(211);

   In [55]: plt.plot(t, impulses);

   In [56]: plt.subplot(212);

   @savefig convolution_two_impulses_convolve.png
   In [57]: plt.plot(t, sc[:len(t)]);

The length of the convolution output ``sc`` is equal to the sum of the
lengths of the two inputs minus one. Conceptually, for our time
series, what this is saying is that the convolution is defined over
the entire input train *plus* the decay time of the impulse response
after the inputs are turned off.

A common task in computational neurobiology is to simulate the
membrane voltage of a neuron receiving an incoming stream of action
potentials.  The action potentials are modeled as a series of pulses
(Dirac delta functions), and the membrane voltage is assumed to be
given by the convolution of the action potentials with the synaptic
response function, which to a first order approximation is similar to
the response function plotted above, and is often modeled as the
difference of two exponentials (as above) or as a low order gamma
function, which has a similar shape.

.. ipython::

   @suppress
   In [49]: plt.close('all')

   # the stepsize
   In [242]: dt = 0.01

   # the time vector from 0..20
   In [243]: t = np.arange(0.0, 20.0, dt)        

   In [244]: Nt = len(t)

   # the impulse response 
   In [245]: r = (np.exp(-t) - np.exp(-5*t))

   In [246]: plt.plot(t, r);

   In [247]: plt.xlabel('time');

   @savefig convolution_impulse_response.png
   In [248]: plt.ylabel('impulse response');

A common assumption is that the action potentials have a Poisson
distribution, which means that the waiting time between pulses is
exponentially distributed and the probability of a pulse in any given
time interval is equal.  Using the uniform random number distribution,
we can easily model the Poisson distribution of Dirac delta pulses as
follows.

.. ipython::

   In [281]: spikes = np.zeros_like(t)

   In [282]: rate = 2  # an emission rate in Hz

   In [283]: nse = np.random.rand(len(t))

   In [284]: spikes[nse<rate*dt] =  1.

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

  @suppress
  In [49]: plt.close('all')

  In [298]: fig, (ax1, ax2) = plt.subplots(2, sharex=True)

  In [299]: ax1.plot(t, spikes); ax1.set_ylabel('spikes');

  In [300]: ax2.plot(t, voltage[:Nt]); ax2.set_ylabel('voltage');

  @savefig convolution_spikes.png
  In [302]: ax2.set_xlabel('time (s)');

Convolution of a time series
============================

In the examples above, we convolved the impulse response function with
a series of impuses.  We can use the same methodology to convolve a
discretely sampled continous time series with the impulse response
function.  The basic idea is that the sample points are Dirac delta
functions, as above, scaled by the amplitude of the signal at the
sample point.  We can represent the spike train above as the sum of
Dirac delta functions, each shifted in time to the time of the
:math:`k`-th spike :math:`t_k`.

.. math::

  s(t) = \sum_k \delta(t-t_k)

For a discretely sampled time series, where the :math:`k`-th sample
point has amplitude :math:`a_k`, we can represent the time series as 

.. math::

  x(t) = \sum_k a_k \delta(t-t_k)
 
and treat the discretely sampled continuous process as a sum of amplitude
modulated pulses.

Consider the white noise process of Guassian distributed random
variates -- we can obtain the convolution on the noise with the impulse response function just as we did with the spike impulse train.

.. ipython::

   # gaussian white noise; Nt discrete samples
   In [304]: x = np.random.randn(Nt)   

   # convolution of noise x with impulse response r
   In [305]: y = np.convolve(x, r, mode='full')    

   In [306]: y = y[:Nt]

