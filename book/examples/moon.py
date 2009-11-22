"""Image denoising of moon landing photo.

etc...
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.mlab as mlab

plt.close('all')
im = plt.imread('moonlanding.png')

plt.imshow(im,cmap=cm.gray)


im_f = np.fft.fft2(im)

power = abs(im_f)

cut95 = mlab.prctile(power.flatten(), 95.0)


plt.figure()
plt.imshow(abs(im_f), cmap=cm.Blues)
plt.clim(0,cut95)


im_f[:,50:-50] = 0
im_f[50:-50,:] = 0

plt.figure()
plt.imshow(abs(im_f), cmap=cm.Blues)
plt.clim(0,cut95)

# Reconstruct the image from the clipped FT data
im_new = np.fft.ifft2(im_f).real
plt.figure()
plt.imshow(im_new,cmap=cm.gray)

plt.show()

