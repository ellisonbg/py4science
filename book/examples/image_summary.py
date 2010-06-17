#!/usr/bin/env python
"""Visual summary of an image.

Usage:
  image_summary.py [filename]

If no filename is given, the script looks for images stored in the py4science
bookdata directory.
"""
#-----------------------------------------------------------------------------
# Library imports
#-----------------------------------------------------------------------------

import sys

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import cm

#-----------------------------------------------------------------------------
# Function definitions
#-----------------------------------------------------------------------------

def image_load(fname, max_size=1200):
    """Load an image, downsampling if needed to keep within requested size.
    """
    img = plt.imread(fname)
    shape = np.array(img.shape, dtype=float)
    sample_fac = int(np.ceil((shape/max_size).max()))
    if sample_fac > 1:
        new_img = img[::sample_fac, ::sample_fac, ...]
        print 'Downsampling %sX:'% sample_fac, img.shape, '->', new_img.shape
        return new_img
    else:
        return img

#-----------------------------------------------------------------------------
# Main script
#-----------------------------------------------------------------------------

if __name__ == '__main__':
    try:
        fname = sys.argv[1]
    except IndexError:
        fname = 'bookdata/stained_glass_barcelona.png'
        #fname = 'bookdata/dessert.png'

    img = image_load(fname)

    # Extract each color channel
    red, green, blue = [ img[:,:,i] for i in range(3) ]

    # Create a figure with 4 subplots, one for each channel
    f = plt.figure()
    axes = [f.add_subplot(1,4,1)]
    axes += [f.add_subplot(1,4,i+1, sharex=axes[0], sharey=axes[0] )
             for i in range(1,4)]

    # With newer versions of matplotlib
    # f, axes = plt.subplots(1, 4, sharex=True, sharey=True)

    # Display the full color figure and the color channels
    axes[0].imshow(img)
    axes[1].imshow(red, cmap=cm.Reds)
    axes[2].imshow(green, cmap=cm.Greens)
    axes[3].imshow(blue, cmap=cm.Blues)

    # Turn off tick labels and allow free-form zooming
    for ax in axes:
        ax.set_xticklabels([])
        ax.set_yticklabels([])
        ax.set_aspect('auto')

    # Make a new figure and display luminosity and per-channel histograms
    f2 = plt.figure()
    axes2 = [f2.add_subplot(4,1,1)]
    axes2 += [f2.add_subplot(4,1,i+1, sharex=axes2[0]) for i in range(1,4)]

    # With newer versions of matplotlib, the same can be done as:
    # f2, axes2 = plt.subplots(4, 1, sharex=True)

    # We want the tick labels to be invisible
    for ax in axes2[:-1]:
        for label in ax.get_xticklabels():
            label.set_visible(False)

    # PNG images sometimes have a 4th transparency channel, sometimes not.  To
    # be safe, we generate a luminosity array consisting of only the first 3
    # channels.
    lumi = img[:,:,:3].mean(axis=2)

    # Now, display a histogram for each channel.  Note that jpeg images come
    # back as integer images with a luminosity range of 0..255 while pngs are
    # read as floating point images in the 0..1 range.  So we adjust the
    # histogram range accordingly:
    hrange = (0.0, 1.0) if lumi.max()<=1.0 else (0.0, 255.0)

    # Display the luminosity and per-channel histograms:
    axes2[0].hist(lumi.flatten(), 256, range=hrange, facecolor='k',
                  edgecolor='k')
    axes2[1].hist(red.flatten(), 256, range=hrange, facecolor='r',
                  edgecolor='r')
    axes2[2].hist(green.flatten(), 256, range=hrange, facecolor='g',
                  edgecolor='g')
    axes2[3].hist(blue.flatten(), 256, range=hrange, facecolor='b',
                  edgecolor='b')

    # Final show
    plt.show()
