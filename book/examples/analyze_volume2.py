import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

if 1:
    r = mlab.csv2rec('csco.csv')

v = r.volume

# print some stats about volume
print 'min=%.1f, max=%.1f, mean=%.1f'%(
    v.min(), v.max(), v.mean())

# print the date of the maximum
indmax = v.argmax()
print 'date max: %s'%r.date[indmax]

# single-pass
nsamples = np.zeros(12)
volumes = np.zeros(12)
volumes2 = np.zeros(12)

for row in r:
    month = row.date.month-1
    vol = float(row.volume)
    nsamples[month] += 1
    volumes[month] += vol
    volumes2[month] += vol**2

means = volumes/nsamples
sigmas = np.sqrt(volumes2/nsamples - means**2)
means_err = sigmas/np.sqrt(nsamples-1)



# display results
fig = plt.figure()
ax = fig.add_subplot(111)

ax.bar(np.arange(1,13), means/1e6, yerr=means_err/1e6)

ax.set_xticks(np.arange(1,13))
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr',
                    'May', 'Jun', 'Jul', 'Aug',
                    'Sep', 'Oct', 'Nov', 'Dec'])

for label in ax.get_xticklabels():
    label.set_rotation(30)

plt.show()
