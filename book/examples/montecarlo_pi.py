#!/usr/bin/env python
"""Simple generation of pi via MonteCarlo integration.

We compute pi as the area of a unit circle, and we compute this area by
integration:

A = pi = 4*int_0^1{sqrt(1-x^2)}

This integral is then done via MonteCarlo integration.

In this example, we do it both in pure Python and then by calling weave.inline
to speed up the loop.
"""

import math
import random

import numpy as np

from scipy import weave


def v1(n = 100000):
    """Approximate pi via monte carlo integration"""

    rand = random.random
    sqrt = math.sqrt
    sm   = 0.0
    for i in xrange(n):
        sm += sqrt(1.0-rand()**2)
    return 4.0*sm/n

    
def v2(n = 100000):
    """Implement v1 above using weave for the C call"""
    
    support = "#include <stdlib.h>"
    
    code = """
    double sm;
    float rnd;
    srand(1); // seed random number generator
    sm = 0.0;
    for(int i=0;i<n;++i) {
        rnd = rand()/(RAND_MAX+1.0);
        sm += sqrt(1.0-rnd*rnd);
    }
    return_val =  4.0*sm/n;"""
    return weave.inline(code,('n'),support_code=support)

if __name__ == '__main__':

    # Monte Carlo Pi:
    print 'pi is:', math.pi
    print 'pi - python:',v1()
    print 'pi - weave :',v2()

    from timeit import timeit
    tpy = timeit('v1()','from montecarlo_pi import v1', number=10)/10.0
    tw = timeit('v2()','from montecarlo_pi import v2', number=10)/10.0
    print 'Python time %.2g s' % tpy
    print 'Weave time %.2g s' % tw
    print 'Weave speedup:',tpy/tw
