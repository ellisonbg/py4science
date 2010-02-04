#!/usr/bin/env python
"""Simple image denoising example using 2-dimensional FFT."""

import sys

import numpy as np
from matplotlib import pyplot as plt

def plot_spectrum(F, amplify=1000):
    """Normalise, amplify and plot an amplitude spectrum."""

    # Note: the problem here is that we have a spectrum whose histogram is
    # *very* sharply peaked at small values.  To get a meaningful display, a
    # simple strategy to improve the display quality consists of simply
    # amplifying the values in the array and then clipping.

    # Compute the magnitude of the input F (call it mag).  Then, rescale mag by
    # amplify/maximum_of_mag.  Numpy arrays can be scaled in-place with ARR *=
    # number.  For the max of an array, look for its max method.
    mag = abs(F) #@
    mag *= amplify/mag.max() #@
    
    # Next, clip all values larger than one to one.  You can set all elements
    # of an array which satisfy a given condition with array indexing syntax:
    # ARR[ARR<VALUE] = NEWVALUE, for example.
    mag[mag > 1] = 1 #@

    # Display: this one already works, if you did everything right with mag
    plt.imshow(mag, plt.cm.Blues)

if __name__ == '__main__':

    try:
        # Read in original image, convert to floating point for further
        # manipulation; imread returns a MxNx4 RGBA image.  Since the image is
        # grayscale, just extract the 1st channel
        #@ Hints:
        #@  - use plt.imread() to load the file
        #@  - convert to a float array with the .astype() method
        #@  - extract all rows, all columns, 0-th plane to get the first
        #@    channel
        #@  - the resulting array should have 2 dimensions only
        im = plt.imread('moonlanding.png').astype(float) #@
        print "Image shape:",im.shape
    except:
        print "Could not open image."
        sys.exit(-1)

    # Compute the 2d FFT of the input image
    #@ Hint: Look for a 2-d FFT in np.fft.
    #@ Note: call this variable 'F', which is the name we'll be using below.
    F = np.fft.fft2(im)  #@

    # In the lines following, we'll make a copy of the original spectrum and
    # truncate coefficients.  NO immediate code is to be written right here.

    # Define the fraction of coefficients (in each direction) we keep
    keep_fraction = 0.1

    # Call ff a copy of the original transform.  Numpy arrays have a copy
    # method for this purpose.
    ff = F.copy() #@

    # Set r and c to be the number of rows and columns of the array.
    #@ Hint: use the array's shape attribute.
    r,c = ff.shape #@

    # Set to zero all rows with indices between r*keep_fraction and
    # r*(1-keep_fraction):
    ff[r*keep_fraction:r*(1-keep_fraction)] = 0  #@

    # Similarly with the columns:
    ff[:, c*keep_fraction:c*(1-keep_fraction)] = 0 #@

    # Reconstruct the denoised image from the filtered spectrum, keep only the
    # real part for display.
    #@ Hint: There's an inverse 2d fft in the np.fft module as well (don't
    #@ forget that you only want the real part).
    #@ Call the result im_new, 
    im_new = np.fft.ifft2(ff).real  #@
    
    # Show the results
    #@ The code below already works, if you did everything above right.
    plt.figure()

    plt.subplot(221)
    plt.title('Original image')
    plt.imshow(im, plt.cm.gray)

    plt.subplot(222)
    plt.title('Fourier transform')
    plot_spectrum(F)

    plt.subplot(224)
    plt.title('Filtered Spectrum')
    plot_spectrum(ff)

    plt.subplot(223)
    plt.title('Reconstructed Image')
    plt.imshow(im_new, plt.cm.gray)

    # Adjust the spacing between subplots for readability 
    plt.subplots_adjust(hspace=0.32)
    plt.show()
