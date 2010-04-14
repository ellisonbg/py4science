"""Record array illustration doing basic analysis of stock trading volumes.

- load crox.csv.  Look at its dtype.  Those fields are accessible as attribues
  of the loaded object from mlab.csv2rec.
       
- sort it,

- plot the adj_close vs date (closing share price adjusted for splits vs
  date).
       
- The daily traded volume is the product of the volume (# shares) times the
  close (price per share).  Find the mean volume, the max volume and the day
  when the max occured.
       
- Plot the daily volume vs date. Then, overlay red dots on the days when the
  volume was in the upper 50% range (> than 0.5 of the max). Make this a
  parameter.
"""

from __future__ import print_function

from matplotlib import mlab
import matplotlib.pyplot as plt

# Name of file to load
fname = 'crox.csv'
# Highlight days where trading volume was above this fraction of max
high_mark = 0.4

# Load and sort data
s = mlab.csv2rec(fname)
s.sort()

# Basic plot
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax1.plot(s.date, s.adj_close)
ax1.set_ylabel('Stock Price (adj)')
ax1.set_title('Points above %.2f range marked' % high_mark)
ax1.grid(True)

# Simple trading volume analysis
dv = s.volume*s.close
print('Min volume: $ %6.3f Million, on %s' %
      (dv.min()/1e6, s.date[dv.argmin()]) )
print('Max volume: $ %6d Million, on %s' %
      (int(dv.max()/1e6),s.date[dv.argmax()]) )

# Plot trading volume, mark high-volume days
mask = dv > high_mark*dv.max()

# Share x axes so zooming is coordinated
ax2 = fig.add_subplot(212, sharex=ax1)
ax2.plot(s.date, dv/1e6)
ax2.scatter(s.date[mask], dv[mask]/1e6, color='r',zorder=10)
ax2.set_ylabel('Volume (1e6 $)')
ax2.grid(True)

# Add the same markers to price plot so we can see them on both.
ax1.scatter(s.date[mask], s.adj_close[mask], color='r',zorder=10)

# Fine-tune figure:
# Make subplots close to each other (do not use hspace exactly zero!)
fig.subplots_adjust(hspace=0.0001)
# Hide ax1 x ticks
plt.setp(ax1.get_xticklabels(), visible=False)
# orient dates nicely
fig.autofmt_xdate()

plt.show()
