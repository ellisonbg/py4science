"""vector_add.py: A nogil Cython function to add two vectors together.

To build using pyximport simply do::

    >>> import pyximport
    >>> pyximport.install(setup_args=dict(include_dirs=[numpy.get_include()]))
    >>> import vector_add
"""


import numpy as np
cimport numpy as np
cimport cython

@cython.boundscheck(False) 
@cython.wraparound(False)
def vector_add(np.ndarray[np.double_t, ndim=1] a,
    np.ndarray[np.double_t, ndim=1] b, np.ndarray[np.double_t, ndim=1] c):
    """Add two double precision vectors."""
    cdef int i
    cdef int n = a.size
    with nogil:
        # The following code can run concurrently and in parallel with other 
        # Python threads! This is possible because Cython uses the type
        # declarations above to write the following code without making
        # any calls to the Python/C API.
        for i in range(n):
            c[i] = a[i] + b[i]

