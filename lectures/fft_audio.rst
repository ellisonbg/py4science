=====================
FFT Audio Compression
=====================
.. ipython::
   :suppress:

   # set up ipython for plotting in pylab
   In [3]: from pylab import *

   In [4]: plt.close('all')

   In [5]: ion()

   In [6]: bookmark ipy_start

The Fourier Transform (FFT) is the basis for many compression
algorithms.  The basic idea is simple: by decomposing a signal into a
sum of sinusoids, we can reduce the size of the signal by removing
frequencies deemed too small to add meaningfully to the perception of
the signal.  For example, in audio compression, we might eliminate all
frequencies above 20kHz, the upper end of the range that humans can
detect (though it would surely ruin the tunes for bats, which can hear
up to 120kHz).  Alternatively, we might sort the amplitudes of the
sinusoids, and keep only the components with the largest amplitudes,
regardless of frequency.  

The `MP3 <http://en.wikipedia.org/wiki/Mp3>`_ standard for audio
compression works on a different principle, relying on a perceptual
masking that occurs in human auditory perception where certain
frequencies in a sound mask higher frequencies at established ratios,
enabling the compressor to remove the higher masked frequencies.
However, the `JPEG <http://en.wikipedia.org/wiki/Jpeg>`_ standard
works exactly this way: the human visual system is more sensitive to
low frequencies variations of color and brightness over wide areas
than to sharp high frequency transitions in the image, so the JPEG
algorithm reduces the contribution of the high frequency components.
The results in a lossy image that nonetheless looks good for images of
some types, particularly for natural scenes, but not so good for
others, such as line art, text and images with sharpe features like a
checkerboard.

In this example we will sketch how one might use the FFT for an audio
compression routine.  It is not a full blown solution since we will
not develop the storage format that stores the compressed audio.  But
we will do a spectral decomposition of an audio signal and show how to
extract just the largest amplitude components, and play back the
compressed sound with just these components to assess how much
degradation there is for various amounts of compression.  A full blown
solution would also have to establish a storage format which indicates
the frequencies and amplitudes of the preserved components, which is a
useful exercise for the reader (one has to be mindful of the
compactness of this storage format since it does little good if we
remove needless components but then use a bloated format to store the
reduced data).

Obtaining a sample
==================

For this example, we will use the Skype incoming ring wav file, which
is available in the book data directory and is called
:file:`CallRingingIn.wav`.  You may want to record your own wave file
speaking or singing because it may make the playback of the compressed
and uncompressed versions more entertaining to you and your family and
friends.

.. note:

  On a UNIX box, you can use the old command line work-horses ``rec``
  and ``play`` to record a wav file.  In the example below, we set the
  sampling frequency at 16kHz, and the number of channels to 1 (mono).
  When you are done performing, hit CTRL-C to stop the recording::
    
    # record the wav file
    > rec -r16k -c1 test.wav

    # play back the wav file
    > play test.wav

  You may need to check your audio mixer settings and increase the
  microphone volume if the recording sounds too faint.
   

To read and write wav files, you need to import ``scipy.io.wavfile``
-- the ``io`` module in scipy is filled with utilities to read and
write many data formats.  In the IPython session below, we first play
the wav file, then load it and inspect what we get back

.. ipython::
   
   # the !play makes a system call to the UNIX play and may be
   # different on your system
   @verbatim
   In [27]: !play CallRingingIn.wav
   CallRingingIn.wav:
    File Size: 117k      Bit Rate: 256k
     Encoding: Signed PCM    
     Channels: 1 @ 16-bit   
   Samplerate: 16000Hz      
   Replaygain: off         
     Duration: 00:00:03.66  
   In:100%  00:00:03.66 [00:00:00.00] Out:58.6k [      |      ]        Clip:0    
   Done.

   In [28]: import scipy.io.wavfile as wavfile

   In [29]: cd ../book/bookdata/
   /home/msierig/py4science/book/bookdata

   In [30]: rate, data = wavfile.read('CallRingingIn.wav')

   In [31]: rate
   Out[31]: 16000

   In [32]: data
   Out[32]: array([34, 40, 41, ..., -1,  0,  2], dtype=int16)



The time series of the audio track is easily plotted

.. ipython::

   @suppress
   In [45]: plt.close('all')

   @suppress
   In [45]: plt.figure((4,4))

   In [36]: t = np.arange(len(data))/float(rate)

   In [37]: plt.plot(t, data);
   
   @savefig fft_audio_timeseries.png   
   In [38]: plt.xlabel('time (s)');


But more interesting is the spectrogram, which shows the power spectra 
density as it evolves over time.  The spectral power (intensity at a
give frequency) is color coded using matplotlib's default colormap
``cm.jet``, so red is high intenisty and blue is low intensity.  The
y-axis gives the frequencies, and the x-axis shows time.

.. ipython::

   @suppress
   In [45]: plt.close('all')

   @suppress
   In [45]: plt.figure((4,4))

   In [46]: plt.specgram(data, Fs=rate);

   In [47]: plt.xlabel('time (s)');

   @savefig fft_audio_specgram.png
   In [48]: plt.ylabel('Freq (Hz)');


One can see broad spectrum sharp vertical bursts at the onset and
termination of each ring, first starting around 0.25s, and then banded
harmonics of the primary tone of the ring, first starting around 375
Hz.




.. ipython::
   :suppress:

   # return to home -- w/o this I was getting a crash
   In [6]: cd ../../lectures
