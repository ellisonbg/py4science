"""Reading and writing numpy arrays to wav files for sound playback. """

# NOTE: this script has been converted to a notebook.  Do NOT update further
# here, this will be removed once the notebook machinery is fully in shape.

#-----------------------------------------------------------------------------
# Library imports
#-----------------------------------------------------------------------------

import numpy as np
from matplotlib import pyplot as plt
from scipy.io import wavfile

#-----------------------------------------------------------------------------
# Function definitions
#-----------------------------------------------------------------------------

def synthetic(name, T, rate, base_freq = 1000):
    valid_names = set(['tone', 'chirp', 'laser'])
    
    nsamples = int(round(rate*T))
    t = np.linspace(0, T, nsamples)

    if name == 'tone':
        # A simple tone with just one frequency
        y = np.sin(2*np.pi*base_freq*t)
    elif name == 'chirp':
        # a chirp
        freq = base_freq*t
        y = np.sin(2*np.pi*freq*t)
    elif name == 'laser':
        # a 'laser': 1/t frequency shift
        freq = base_freq/(t+1)
        y = np.sin(2*np.pi*freq*t)

    # linearly rescale raw data to wav range and convert to integers
    scale_fac = 2**15
    sound = (scale_fac*y).astype(np.int16)
    return sound

def viz_sound(sound, name, npts=1000):
    plt.figure()
    plt.specgram(sound)
    plt.title(name)

    plt.figure()
    plt.plot(sound[:npts])
    plt.title(name)
    

#-----------------------------------------------------------------------------
# Main script
#-----------------------------------------------------------------------------

if __name__ == '__main__':
    
    # Generate a synthetic signal
    rate = 2*11025 # Hz
    T = 2 # s
    base_freq = 1000
    name = 'tone'
    name = 'chirp'
    name = 'laser'
    sound = synthetic(name, T, rate)

    wavfile.write('sample_%s.wav' % name, rate, sound)
    viz_sound(sound, name)

    # Now read a sound file
    fname = 'laser'
    fname = 'train'
    rate2, sound2 = wavfile.read('bookdata/%s.wav' % fname)
    viz_sound(sound2,  fname)

    plt.show()
