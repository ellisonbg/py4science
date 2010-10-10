"""Utility module to load measurements into Numpy record arrays.

Loading measurement files with the format:

#Station  Lat    Long   Elev 
BIRA	26.4840	87.2670	0.0120
BUNG	27.8771	85.8909	1.1910
etc...

Extension of the previous example to illustrate simple event handling.
"""

import os
import sys

import numpy as np
import pylab as plt

class StationPicker(object):
    def __init__(self, figure, stations, eps=0.10, axis=None):
        self.figure = figure
        self.stations = stations
        self.cid = figure.canvas.mpl_connect('button_press_event', self)
        if axis is None:
            axis = figure.axes[0]
        self.axis = axis
        self.eps = eps

    def __call__(self, event):
        #print 'click', event  # dbg
        if event.inaxes != self.axis:
            return
        self.figure.canvas.draw()
        # Compute the distance from the click to all stations
        lats = self.stations['lat']
        longs = self.stations['lon']
        click_lat, click_long = event.xdata, event.ydata
        lat_d = lats - click_lat
        lon_d = longs - click_long
        dist = np.sqrt(lat_d**2 + lon_d**2)
        nearest_i = dist.argmin()
        near_dist = dist[nearest_i]
        nearest = self.stations[nearest_i]
        #print 'Nearest distance:', near_dist  # dbg
        if near_dist < self.eps:
            print "HIT! You clicked on", nearest['station']
        else:
            print "No hit, nearest is:", nearest['station']
            print "It is at:", nearest['lat'], nearest['lon']
            print "Distance to it:", near_dist
        sys.stdout.flush()
        

# Find our directory and assume data file is next to us.  This makes this
# script work regardless of where it is run from.
dir, fname = os.path.split(os.path.abspath(__file__))
data_fname = os.path.join(dir, 'recarr_simple_data.txt')

# Data descriptor to make a proper array.
dt = [('station','S4'), ('lat',np.float32),
      ('lon',np.float32), ('elev',np.float32)]

tab = np.loadtxt(data_fname, dt)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(tab['lat'], tab['lon'], 30*(tab['elev']+1), c=tab['elev'] )

# Make a picker with that binds the figure and the data
StationPicker(fig, tab)

plt.show()
