=======================
 Interactive materials
=======================

1 and 1/2 day workshop, undergraduate level
===========================================

Day 1
-----

**9:00**

* FP - Python for scientific computing: A high-level overview of the topic of
  Python in a scientific context ( simple 30 minute talk).

* Interlude: installfest, 15 minutes, Win and Mac EPD, linux apt-get.
  
* JDH Appetizer: visual example (may type along). Matplotlib stinkbug image
  tutorial - 15 minutes.

**10:15 - coffee break**

**10:30**

* FP Workflow, guided by a simple examples and students typing along.  Will show
  basics of everyday workflow as we cover the core concepts.

  Topics not to forget:

    * Working interactively to learn, ipython.

    * Getting help.  Introspection, tab, ?, help().

    * Magic functions.

    * Using -pylab: plotting, builtin numerical and graphing names.

    * Writing scripts is different, only builtins available.

    * Using %run.

  Concept outline, using the numerical chaos example.

  * Basic scalar types: numbers (int, float, complex).

  * First demo, do it interactively.  Then load into an editor.

  * Quick review of control flow: if, for, range, while, break, continue.  Use
    iterative maps to illustrate, change example, test fixed point behavior
    (stop within epsilon of fp), etc.

  * Defining functions. Arguments and docstrings. Keywords.  Make mu an
    argument, add a docstring...

  * Basic collections: lists.  In numchaos we had one, play with it.  Show
    quicksort...


**Lunch**

* JDH More basics...

  * Opening a file, reading text.  Strings.
    
  * Basic collections, dicts: simplified wordfreqs.
    
  * Exceptions: a core concept in Python, you really can't use the language
    without them.

  * Debugging your programs 1:
  
    * What is a traceback? How do you read it? Typo, indentation errors,
      NameErrors.
    * %xmode verbose
    * Ye olde print statement.


* FP Introduction to NumPy arrays.

  * Creating arrays: array(), ones, zeros, random, ?_like(), loadtxt
  * dtype, shape: 1d, 2d.
  * Basic operations: arithmetic and slicing.
  * attributes, tab complete on them.
  * mean, std, axis= operations
  * Saving and reloading arrays on disk.


* JDH Working with data
  * Reading files.
  * Web resources
  * Simple text parsing.
  * CSV files.
  * Matplotlib's data loader.
  * Record arrays. Stock demo.
  * Exercise: compute monthly trading volume average.
  
* FP FFT image denoising.


Day 2
-----

* FP: 
  * monthly averages with arrays of zeros, single-pass implementation.
  * numpy load/save - random numbers compare to txt

  * dicts - ? Words?
  * functions - args, keywords, docstrings

* JDH: random walkers

* FP: Glass dots

Topics not covered
------------------

* FP  Statistics:
  - review basic descriptive statistics
  - stats distributions of neuron spiking/radioactive decay

* FP Logistic map, fancier

* JDH ODEs: the Lotka-Volterra system.


Notes
-----

- To stop scripts mid-way:
  raise SystemExit(0)  # also see %run -e

- %logstart

- Missed on intro

  * sine wave
  * exponential
  * add noise to it
  * random matrix (uniform, normal). Show histograms.
  * row, column operations
  * reshape an array 1, 2, 3d
  * flat views

  
1 day workshop, introductory level
==================================

basic language types
control flow
defining functions
numpy arrays
basic plotting
reading/writing data

* Appetizer: visual example (may type along). Matplotlib stinkbug image
  tutorial - 15 minutes.
  
  bug = imread()
  bug.shape
  get luminance
  histogram
  im = imshow(bug)
  im.set_clim()
  im.set_cmap('hot')

* Workflow, guided by a simple examples and students typing along.  Will show
  basics of everyday workflow as we cover the core concepts.

  Topics not to forget:

    * Working interactively to learn, ipython.

    * Getting help.  Introspection, tab, ?, help().

    * Magic functions.

    * Using -pylab: plotting, builtin numerical and graphing names.

    * Writing scripts is different, only builtins available.

    * Using %run.

  Concept outline, using the numerical chaos example.

  * Basic scalar types: numbers (int, float, complex).

  * First demo, do it interactively.  Then load into an editor.

  * Quick review of control flow: if, for, range, while, break, continue.  Use
    iterative maps to illustrate, change example, test fixed point behavior
    (stop within epsilon of fp), etc.

  * Defining functions. Arguments and docstrings. Keywords.  Make mu an
    argument, add a docstring...

  * Basic collections: lists.  In numchaos we had one, play with it.  Show
    quicksort...


**Lunch**

* More basics...

  * Opening a file, reading text.  Strings.
    
  * Basic collections, dicts: simplified wordfreqs.
    
  * Exceptions: a core concept in Python, you really can't use the language
    without them.

  * Debugging your programs 1:
  
    * What is a traceback? How do you read it? Typo, indentation errors,
      NameErrors.
    * %xmode verbose
    * Ye olde print statement.


* Introduction to NumPy arrays.

  * Creating arrays: array(), ones, zeros, random, ?_like(), loadtxt
  * dtype, shape: 1d, 2d.
  * Basic operations: arithmetic and slicing.
  * attributes, tab complete on them.
  * mean, std, axis= operations
  * Saving and reloading arrays on disk.


* Working with data
  * Reading files.
  * Web resources
  * Simple text parsing.
  * CSV files.
  * Matplotlib's data loader.
  * Record arrays. Stock demo.
  * Exercise: compute monthly trading volume average.
  
* FP FFT image denoising.


* FP: 
  * monthly averages with arrays of zeros, single-pass implementation.
  * numpy load/save - random numbers compare to txt

  * dicts - ? Words?
  * functions - args, keywords, docstrings

* JDH: random walkers

* FP: Glass dots

Notes
-----

- To stop scripts mid-way:
  raise SystemExit(0)  # also see %run -e

- %logstart

- Missed on intro

  * sine wave
  * exponential
  * add noise to it
  * random matrix (uniform, normal). Show histograms.
  * row, column operations
  * reshape an array 1, 2, 3d
  * flat views
