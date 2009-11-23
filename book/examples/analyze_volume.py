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

# get an array of months
months = np.array([d.month for d in r.date])
means = []
sigmas = []
nsamples = []
for month in range(1,13):
    mask = months==month
    mu = v[mask].mean()
    sigma = v[mask].std()    
    means.append(mu)
    sigmas.append(sigma)
    nsamples.append(mask.sum())

means = np.array(means)/1e6
sigmas = np.array(sigmas)/1e6
nsamples = np.array(nsamples)



fig = plt.figure()
ax = fig.add_subplot(111)

ax.bar(np.arange(1,13), means, yerr=sigmas/np.sqrt(nsamples-1))

ax.set_xticks(np.arange(1,13))
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr',
                    'May', 'Jun', 'Jul', 'Aug',
                    'Sep', 'Oct', 'Nov', 'Dec'])

for label in ax.get_xticklabels():
    label.set_rotation(30)


plt.show()
    
