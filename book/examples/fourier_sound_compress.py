"""Simple illustration of audio compression by dropping frequency components.

Usage: Run as

  fourier_sound_approx.py [filename.wav]

whith the name of a .wav file containing an audio signal.  If none is given, it
will assume that a single-channel file named 'test_mono.wav' is present in the
current directory.
"""

# NOTE: this script has been converted to a notebook.  Do NOT update further
# here, this will be removed once the notebook machinery is fully in shape.


#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# Stdlib
import os
import sys

# Third-party
import numpy as np

from matplotlib import pyplot as plt
from scipy.io import wavfile

#-----------------------------------------------------------------------------
# Function definitions
#-----------------------------------------------------------------------------
def fourier_approx(x, frac=0.5, Fs=11000):
    """
    approximate x by taking only the frac largest fourier components where frac
    is a float between 0..1

    Fs is the sampling frequency of the data
    
    return the approximated signal

    if makeplot is True, plot the original time series and approximation in a
    pyplot figure
    """
    out = np.fft.rfft(x) 
    print 'rfft', x.shape, out.shape
    # normally the output of fft is the same size as the input, but
    # for real inputs, the fft is symmetric around the DC component,
    # so rfft is a helper function which only returns the positive
    # frequencies and ignores the identical, symmetric negative
    # frequencies.  The output array is half the size of the input
    # plus 1; the extra component is the DC frequency
    magnitude = np.abs(out)
    ind = magnitude.argsort()
    # zero out the 1-frac smallest frequency components
    indmin = int((1-frac)*len(magnitude))
    out[ind[:indmin]] = 0.

    ret = np.fft.irfft(out)
    print 'irrft', ret.shape, out.shape
    return ret


def plot_approx(x, xapprox, frac=0.5, Fs=11000):
    """Plot an audio signal and its approximation.
    """
    t = np.arange(len(x), dtype=float)/Fs

    fig = plt.figure()
    #print 'x', t.shape, x.shape, xapprox.shape
    plt.plot(t, x, label='original', lw=1)
    
    #print 'xapprox', t.shape, xapprox.shape
    plt.plot(t, xapprox, label='approx', lw=1)
    plt.title('Approx signal %.2f%% of the total frequencies'%(
        100*frac))
    plt.xlabel('time (s)')

    plt.grid()
    leg = plt.legend(fancybox=True)
    leg.get_frame().set_alpha(0.5)

    fig, (ax0, ax1) = plt.subplots(2, 1)
    ax0.psd(x, Fs=Fs)
    ax0.set_ylabel('original')
    ax0.set_title('Power spectrum of original and approx')
    ax0.set_xlabel('')
    ax1.psd(xapprox, Fs=Fs)
    ax1.set_ylabel('approx')

#-----------------------------------------------------------------------------
# Main script
#-----------------------------------------------------------------------------
if __name__ == '__main__':

    try:
        infile = sys.argv[1]
    except IndexError:
        infile = 'data/CallRingingIn.wav'

    # Fraction of frequencies to keep (as a number in [0,1]).
    frac = 0.2

    # Load data file
    basename, ext = os.path.splitext(infile)
    rate, x = wavfile.read(infile)

    # Note: the file may have an even or odd number of samples, but if the
    # length is odd, some care must be taken later on when applying the inverse
    # ral-only FFT.  For simplicity, we simply drop the last data point if the
    # file is even.
    if len(x) %2:  x = x[:-1]

    if len(x.shape)==2:
        # looks like a stereo wave
        print 'extracting mono channel'
        x = x[:,0]

    xapprox = fourier_approx(x, frac=frac)
    plot_approx(x, xapprox, frac, rate)
    
    # linearly rescale raw data to wav range and convert to integers
    sound = xapprox.astype(np.int16)
    
    wavfile.write('%s_frac%d.wav' % (basename, 100*frac), rate, sound)

    plt.show()
