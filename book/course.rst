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

7. Poly homework quick review. Poly1d objects, binops with scalars.

   Sympy.  Introduction, together, apart, fraction, simplify, expand.

   - Show tutorial, gotchas page.
   - Symbol(), symbols, var.
   - Eq().
   - Discuss symarray(). Process.-+
   

   A little on testing and docstrings.  Doctests. Interactive debugging with
   %debug, and %run -d script.py.

   Fix script, %run -t.


   Homework: symbolic polynomials, validation. Newton root finding.

   
8. Discuss tdd.py, exercise (finish it).

   I/O: text & binary.

       np.loadtxt, np.load,
       np.savetxt, np.save, np.savez
       mlab.csv2rec

       Record arrays.
       
   Exercise:
     - load crox.csv.  Look at its dtype.  Those fields are accessible as
       attribues of the loaded object from mlab.csv2rec.
     - sort it,
     - plot the adj_close vs date (closing share price adjusted for splits vs
       date).
     - The daily traded volume is the product of the volume (# shares) times
       the close (price per share).  Find the mean volume, the max volume and
       the day when the max occured.
     - Plot the daily volume vs date. Then, overlay red dots on the days when
       the volume was in the upper 50% range (> than 0.5 of the max).

Code:

s = mlab.csv2rec ('crox.csv')
s.sort()
plot(s.date, s.adj_close)
gcf().autofmt_xdate()
draw()
dv = s.volume*s.close
dv.min()
dv.max()
dv.argmax ()
mask = dv > 0.5*dv.max()
figure()
plot(s.date, dv)
gcf().autofmt_xdate()
draw()
ax = gca()
plot(s.date, dv)
gcf().autofmt_xdate()
ax = gca()
ax.scatter(s.date[mask], dv[mask], color='r',zorder=10)
draw()
  
   Exceptions, classes and OO programming.

   Homework: data problem (descriptive stats)

9. Presented by Jorge and Diego (I'm gone)


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
