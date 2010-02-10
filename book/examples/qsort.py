"""Simple quicksort implementation.

From http://en.wikipedia.org/wiki/Quicksort we have this pseudocode (see also
the C implementation for comparison).

Note: what follows is NOT python code, it's meant to only illustrate the
algorithm for you.  Below you'll need to actually implement it in real Python.
You may be surprised at how close a working Python implementation can be to
this pseudocode.


function quicksort(array)
     var list less, greater
     if length(array) <= 1  
         return array  
     select and remove a pivot value pivot from array
     for each x in array
         if x <= pivot then append x to less
         else append x to greater
     return concatenate(quicksort(less), pivot, quicksort(greater))
"""

def qsort(lst):
    """Return a sorted copy of the input list.

    Input:

      lst : a list of elements which can be compared.

    Examples:

    >>> qsort([])
    []

    >>> qsort([3,2,5])
    [2, 3, 5]
    """

    if len(lst) <= 1:
        return lst

    pivot, rest   = lst[0],lst[1:]
    less_than     = [ lt for lt in rest if lt < pivot ]
    greater_equal = [ ge for ge in rest if ge >= pivot ]

    return qsort(less_than) + [pivot] + qsort(greater_equal)


#-----------------------------------------------------------------------------
# Tests
#-----------------------------------------------------------------------------
import random

import nose
import nose, nose.tools as nt

def test_sorted():
    seq = range(10)
    sseq = qsort(seq)
    nt.assert_equal(seq,sseq)

def test_random():
    tseq = range(10)
    rseq = range(10)
    random.shuffle(rseq)
    sseq = qsort(rseq)
    nt.assert_equal(tseq,sseq)

# If called from the command line, run all the tests
if __name__ == '__main__':
    # This call form is ipython-friendly
    nose.runmodule(argv=['-s','--with-doctest'],
                   exit=False)
