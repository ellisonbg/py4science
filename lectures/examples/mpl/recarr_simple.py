"""Utility module to load measurements into Numpy record arrays.

Loading measurement files with the format:

#Station  Lat    Long   Elev 
BIRA	26.4840	87.2670	0.0120
BUNG	27.8771	85.8909	1.1910
etc...

These are seismic measurement stations in the Himalaya.  If you have the
basemap matplotlib toolkit installed, this will show a real map and overlay the
station locations on top of that.
"""
import os

import numpy as np
import matplotlib.pyplot as plt
try:
    from mpl_toolkits.basemap import Basemap
    have_basemap = True
except ImportError:
    have_basemap = False

# Find our directory and assume data file is next to us.  This makes this
# script work regardless of where it is run from.
dir, fname = os.path.split(os.path.abspath(__file__))
data_fname = os.path.join(dir, 'recarr_simple_data.txt')

# Data descriptor to make a proper array.
dt = [('station','S4'), ('lat',np.float32),
      ('lon',np.float32), ('elev',np.float32) ]
# This is an alternate and fully equivalent form:
dt = dict(names = ('station','lat','lon','elev'),
          formats = ('S4',np.float32,np.float32,np.float32) )

tab = np.loadtxt(data_fname, dt).view(np.recarray)

sizes = 30*(tab.elev+1)
title = 'Seismic stations in the Himalaya'

if 0:
    print 'Stations:', tab.station
    print 'Elevations:', tab.elev
    print 'First station:', tab[0]
    print 'Mean latitude:', tab.lat.mean()

    f1 = plt.figure()
    ax = f1.add_subplot(111)
    s = ax.scatter(tab.lon, tab.lat, s=sizes, c=tab.elev)
    f1.colorbar(s)
    f1.suptitle(title)

if have_basemap:
    # Draw the stations on a real map of the Earth.
    # Find boundaries 
    lon0 = 0.99*tab.lon.min()
    lon1 = 1.01*tab.lon.max()
    lat0 = 0.99*tab.lat.min()
    lat1 = 1.01*tab.lat.max()
    # Geographic grid to draw
    parallels = np.linspace(lat0, lat1, 5)
    meridians = np.linspace(lon0, lon1, 5)

    # Resolution of the basemap to load ('f' is *very* expensive)
    resolution = 'i' # intermediate resolution for mab info

    f2 = plt.figure()
    ax2 = f2.add_subplot(111)
    m = Basemap(lon0, lat0, lon1, lat1, resolution=resolution, ax=ax2)
    m.drawcountries(color=(1,1,0))  # country boundaries in pure yellow
    m.drawrivers(color=(0,1,1))  # rivers in cyan
    m.bluemarble()  # NASA bluemarble image
    m.drawparallels(parallels, labels=[1,0,0,0], fmt='%.2f')
    m.drawmeridians(meridians, labels=[0,0,0,1], fmt='%.2f')
    s = m.scatter(tab.lon, tab.lat, s=sizes, c=tab.elev, zorder=10, alpha=0.5)
    f2.colorbar(s)
    f2.suptitle(title)
    
    
plt.show()
