==============
Course outline
==============

Week 1
======

1. Intro lecture, course logistics, class names/background, general Q&A.

2. Workflow introduction, basic types of the language, using ipython, reading a
   traceback, etc.. Qsort exercise for them.

   Homework: wallis pi, wordfreqs, numerical_chaos.

3. Discuss homework problems, recap basic types, sets and tuples, intro to
   numpy arrays slides.

   Hw: trapezoid integration.

   
Week 2
======

4. Simple arrays, creation, methods, display. Arrays vs lists, views vs
   copies. Simple dtypes.

   Discussion of trapezoid integration homework.

   Array creation and elementary uses:

   * created from scratch using ``np.array``, ``np.zeros``, ``np.ones`` and
     ``np.empty``, and their ``_like`` counterparts.

   * monotonic samples using ``np.arange`` and ``np.linspace``

   Exercise: make a simple function plot of $f(x) = \sin(x)$ or $\sin(x^2)$.
   
   * from random deviates using ``np.random``: ``rand``, ``randn``,
     ``uniform``, ``normal``, show others.

   Exercise: verify mean/stdev for a normal distribution.  See normal docstring.

   Matplotlib intro with stinkbug tutorial:
   http://matplotlib.sourceforge.net/users/image_tutorial.html
   
   Homework: Bessel functions.  Log plots, scatter plots.

5. Discuss hw (bessel). Give link to stinkbug tut online.

   More matplotlib intro.  Pylab vs axis creation, some examples.  set*
   methods.

   Homework: FFT image denoising. 

6. Enthought Webinar: numpy and statistics.  Descriptive stats materials.
  
   Homework: Descriptive statistics,  Polynomial roots?

   
Week 3
======

7. Sympy.

   I/O: text & binary. Record arrays. Web data, urrlib, financial data.

   Running scripts with errors, interactive debugging.

   A little on testing and docstrings.  Doctests. Interactive debugging with
   %debug, and %run -d.

   Homework: symbolic polynomials, validation. Newton root finding.

   
8. Exceptions, classes and OO programming.

   Homework: eigenfaces, data problem.

9. Presented by Manuel Paez (I'm gone)


Week 4
======

10. f2py, cython and weave.

    Homework: 

11. Parallel computing: multiprocessing, ipython.

    Homework:
    
12. Demos: Sage, mayavi.  Wrapup.


Extras
======

#. mpl2: glass dots, event handling.
