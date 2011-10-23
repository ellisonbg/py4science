import numpy as np
import matplotlib.pyplot as plt

import scipy.signal as sig

def winspect(win, name=None):
    """Inspect a window by showing it and its spectrum"""
    npts = len(win)
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,4))
    ax1.plot(win)
    if name:
        tt = 'Window: %s' % name
    else:
        tt = 'Window'
    ax1.set_title(tt)
    ax1.set_xlim(0, npts)
    wf = np.fft.fft(win)
    ax2.plot(np.log(np.abs(np.fft.fftshift(wf).real)))
    ax2.axhline(0, color='k')
    ax2.axhline(-5, color='k')
    ax2.set_xlim(0, npts)
    ax2.set_title('Window spectrum')
    ax2.grid()
    plt.show()


def kaiser_inspect(npts, beta):
    name = r'Kaiser, $\beta=%1.1f$' % beta
    winspect(sig.kaiser(npts, beta), name)

if __name__ == '__main__':

    # Window size
    npts = 128

    # Boxcar with zeroed out fraction
    b = sig.boxcar(npts)
    zfrac = 0.15
    zi = int(npts*zfrac)
    b[:zi] = b[-zi:] = 0
    name = 'Boxcar - zero fraction=%.2f' % zfrac
    winspect(b, name)

    # Hanning
    winspect(sig.hanning(npts), 'Hanning')

    # Various Kaiser windows
    kaiser_inspect(npts, 0.1)
    kaiser_inspect(npts, 1)
    kaiser_inspect(npts, 10)
    kaiser_inspect(npts, 100)
