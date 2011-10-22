# <nbformat>2</nbformat>

# <markdowncell>

# # Introduction to numpy
# 

# <codecell>

import numpy as np

# <markdowncell>

# ## Inspecting arrays
# 
# * shape, size, dtype

# <codecell>

x = np.random.randn(10, 2)
print 'shape', x.shape
print 'dtype', x.dtype

# <markdowncell>

# ## Creating arrays
# * arange
# * zeros and ones, by type
# * random arrays
# * arrays from files

# <codecell>

x = np.zeros(10)

# <markdowncell>

# ## Slicing arrays
# * strides
# * views
# * RGBA example

# <codecell>

x = np.arange(36)
X = x.resize(9,4)

# <markdowncell>

# ## Logical masks
# * Creating masks and indexing with them
# * Combining masks
# * Using masks for analysis (stock demo)

# <codecell>

x = np.random.randn(10000)
mask = x>2
mask.sum()

# <markdowncell>

# ## Structured arrays and record arrays
# * dtypes
# * from CSV files
# * with masking

# <codecell>

r = mlab.csv2rec('data/crox.csv')
r.dtype

