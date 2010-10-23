import os
import numpy as np
from matplotlib import pyplot as plt
from scipy.io import wavfile


def fourier_approx(x, frac=0.5, makeplot=True, Fs=11000):
    """
    approximate x by taking only the frac largest fourier components where frac
    is a float between 0..1

    Fs is the sampling frequency of the data
    
    return the approximated signal

    if makeplot is True, plot the original time series and approximation in a
    pyplot figure
    """
    out = np.fft.rfft(x)
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

    xapprox = np.fft.irfft(out)

    if makeplot:
        t = np.arange(len(x), dtype=float)/Fs
        fig = plt.figure()
        plt.plot(t, x, label='original', lw=1)
        plt.plot(t, xapprox, label='approx', lw=1)
        plt.title('Approx signal with %d frequencies (%.2f%% of the total)'%(
            indmin, 100*frac))
        plt.xlabel('time (s)')

        plt.grid()
        leg = plt.legend(fancybox=True)
        leg.get_frame().set_alpha(0.5)

        fig = plt.figure()
        ax1 = plt.subplot(211)
        plt.psd(x, Fs=Fs)
        plt.ylabel('original')
        plt.title('Power spectrum of original and approx')
        plt.xlabel('')
        ax2 = plt.subplot(212,sharex=ax1)
        plt.psd(xapprox, Fs=Fs)
        plt.ylabel('approx')

    return xapprox
        
            
        
infile = 'test_mono.wav'
basename, ext = os.path.splitext(infile)
frac = 0.2

rate, x = wavfile.read(infile)

if len(x.shape)==2:
    # looks like a stereo wave
    print 'extracting mono channel'
    x = x[:,0]

xapprox = fourier_approx(x, frac=frac, makeplot=True)

# linearly rescale raw data to wav range and convert to integers
sound = xapprox.astype(np.int16)


wavfile.write('%s_frac%d.wav' % (basename, 100*frac), rate, sound)
 
plt.show()
