"""Image denoising of moon landing photo.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.mlab as mlab

# Load data
im = plt.imread('bookdata/moonlanding.png')

# Fourier transform
im_f = np.fft.fft2(im)

# Power spectrum of the image
power = abs(im_f)

# Copy im_f so we can retain the original for display
im_f_clean = im_f.copy()
im_f_clean[:,50:-50] = 0
im_f_clean[50:-50,:] = 0

# Reconstruct the image from the clipped FT data
im_new = np.fft.ifft2(im_f_clean).real

# Make a single figure summarizing all the results
plt.close('all')
fig, ax = plt.subplots(2,2)

# Fine-tune the figure so the titles don't overlap by making the  font smaller
# and the height between plots larger
plt.rc('font',size=8)
fig.subplots_adjust(hspace=0.25)

# Make the four panels
ax[0,0].set_title('Original Image')
ax[0,0].imshow(im, cmap=cm.gray)

ax[0,1].set_title('Power spectrum')
img = ax[0,1].imshow(power, cmap=cm.Blues)

# Show only where 95% of the power is, because there are a few huge spikes that
# otherwise make it impossible to see anything
power_cut = 95.0
clipped_power = mlab.prctile(power.flatten(), power_cut)
img.set_clim(0, clipped_power)

ax[1,1].set_title('Filtered Spectrum')
img = ax[1,1].imshow(abs(im_f_clean), cmap=cm.Blues)
img.set_clim(0, clipped_power)

ax[1,0].set_title('Reconstructed Image')
ax[1,0].imshow(im_new, cmap=cm.gray)

plt.show()
