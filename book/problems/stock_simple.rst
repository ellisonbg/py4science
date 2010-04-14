Simple Stock Analysis
=====================

In class we did the following exercise:

- load ``crox.csv``.  Look at its dtype.  Those fields are accessible as
  attribues of the loaded object from ``mlab.csv2rec``.
  
- sort it

- plot the adj_close vs date (closing share price adjusted for splits vs date).
  
- The daily traded volume is the product of the volume (# shares) times the
  close (price per share).  Find the mean volume, the max volume and the day
  when the max occured.
  
- Plot the daily volume vs date. Then, overlay red dots on the days when the
  volume was in the upper 50% range (> than 0.5 of the max).

For that we used this code (OK for pasting into IPython)::

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

Now, modify this code to have both plots on a single plot that share the x axis
(i.e., so that zooming in one plot zooms the other on the x axis). Add the
markers for high-volume days to both plots and make the filename and threshold
(in this case 50%) parameters so they can be easily changed.

Also print the dates (the actual date, not the index) when the min/max trading
volumes occurred.

You should obtain a printout similar to::

    In [3]: run stock_simple.py
    Min volume: $  0.560 Million, on 2008-12-24
    Max volume: $   2887 Million, on 2007-11-01

and figure like this (already zoomed to the high-volume days):

.. figure:: fig/stock_simple_zoomed.png

.. only:: instructor

   Solution
   --------

   .. literalinclude:: examples/stock_simple.py
   