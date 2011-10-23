import scipy.io.wavfile as wavfile
import numpy as np
import matplotlib.pyplot as plt
rate, x = wavfile.read('CallRingingIn.wav')

Nx = len(x)
if (Nx%2)==1:
    # make sure x is even
    x = x[:-1]
    Nx -= 1
    

F = np.fft.rfft(x)
magnitude = np.abs(F)
ind = magnitude.argsort()

# zero out half of the smallest frequencies
Fc = F.copy()
remove = int(.95 * len(Fc))
Fc[ind[:remove]] = 0.

xapprox = np.fft.irfft(Fc)

plt.figure()
plt.subplot(211)
plt.specgram(x)
plt.colorbar()
plt.clim(0, 80)

plt.subplot(212)
plt.specgram(xapprox)
plt.colorbar()
plt.clim(0, 80)

wavfile.write('CallFiltered.wav', rate, xapprox.astype(np.int16))


plt.show()
