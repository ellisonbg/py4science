#!/usr/bin/env python
"""Simple example implementations of the Sieve of Erathostenes."""

__author__ = "Fernando Perez <Fernando.Perez@colorado.edu>"

import sys
import math

import numpy as np

def sieve_quad(nmax):
    """Return a list of prime numbers up to nmax.

    Naive, O(N^2) implementation using the Sieve of Erathostenes."""

    # Sanity checks
    assert nmax>1, "nmax must be > 1"
    if nmax == 2: return [2]
    
    # For nmax>3, do full sieve
    primes_head = [2]
    first = 3
    primes_tail = np.arange(first,nmax+1,2)
    while first <= round(math.sqrt(primes_tail[-1])):
	first = primes_tail[0]
	primes_head.append(first)
	non_primes = first * primes_tail
	primes_tail = np.array([ n for n in primes_tail[1:]
                                if n not in non_primes ])

    return primes_head + primes_tail.tolist()


def sieve_quad2(nmax):
    """Return a list of prime numbers up to nmax.

    A slightly more readable implementation, still O(N^2)."""

    # Sanity checks
    assert nmax>1, "nmax must be > 1"
    if nmax == 2: return [2]
    
    # For nmax>3, do full sieve
    primes_head = [2]
    first = 3
    primes_tail = np.arange(first,nmax+1,2)
    while first <= round(math.sqrt(primes_tail[-1])):
	first = primes_tail[0]
	primes_head.append(first)
	non_primes = first * primes_tail
        primes_tail = np.array(list(set(primes_tail[1:])-set(non_primes)))
        primes_tail.sort()

    return primes_head + primes_tail.tolist()


def sieve(nmax):
    """Return a list of prime numbers up to nmax, using Erathostenes' sieve.

    This is a more efficient implementation than sieve_quad: we combine a
    set with an auxiliary list (kept sorted)."""

    # Sanity checks
    assert nmax>1, "nmax must be > 1"
    if nmax == 2: return [2]
    
    # For nmax>3, do full sieve
    primes_head = [2]
    first = 3

    # The primes tail will be kept both as a set and as a sorted list
    primes_tail_lst = range(first,nmax+1,2)
    primes_tail_set = set(primes_tail_lst)

    # optimize a couple of name lookups from loops
    tail_remove = primes_tail_set.remove
    head_append = primes_head.append
    sqrt = math.sqrt
	
    # Now do the actual sieve
    while first <= round(sqrt(primes_tail_lst[-1])):
	# Move the first leftover prime from the set to the head list
	first = primes_tail_lst[0]
	tail_remove(first)  # remove it from the set
	head_append(first) # and store it in the head list

	# Now, remove from the primes tail all non-primes.  For us to be able
	# to break as soon as a key is not found, it's crucial that the tail
	# list is always sorted.
	for next_candidate in primes_tail_lst:
	    try:
		tail_remove(first*next_candidate)
	    except KeyError:
		break
            
	# Build a new sorted tail list with the leftover keys
	primes_tail_lst = list(primes_tail_set)
	primes_tail_lst.sort()

    return primes_head + primes_tail_lst

if __name__ == '__main__':
    # A simple test suite.
    import unittest

    # Make the generic test NOT be a subclass of unittest.TestCase, so that it
    # doesn't get picked up automatically.  Each subclass will specify an
    # actual sieve function to test.
    class sieveTestBase:

        def test2(self):
            self.assert_(self.sieve_func(2)==[2])

        def test100(self):
            primes100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                         43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
            self.assert_(self.sieve_func(100)==primes100)

    # These subclasses define the actual sieve function to test.  Note that it
    # must be set as a staticmethod, so that the 'self' instance is NOT passed
    # to the called sieve as first argument.
    class sieveTestCase(sieveTestBase,unittest.TestCase):
        sieve_func = staticmethod(sieve)

    class sieve_quadTestCase(sieveTestBase,unittest.TestCase):
        sieve_func = staticmethod(sieve_quad)

    class sieve_quad2TestCase(sieveTestBase,unittest.TestCase):
        sieve_func = staticmethod(sieve_quad2)

    # Other code for demonstration purposes
    def time_rng(fun,nrange,ret_both=0,verbose=1):
        """Time a function over a range of parameters.

        Returns the list of run times.

        The function should be callable with a single argument: it will be
        called with each entry from nrange in turn.

        If verbose is true, at each step the value of nrange and time for the
        call is printed."""

        def time_n(n):
            "Simple closure for local timings"
            import time
            t0 = time.clock()
            fun(n)
            return time.clock() - t0
        
        times = []
        write = sys.stdout.write
        flush = sys.stdout.flush
        for n in nrange:
            t = time_n(n)
            if verbose:
                if verbose==1:
                    write('.')
                elif verbose>1:
                    print n,t
                flush()
            if t==0: t = 1e-9
            times.append(t)

        if ret_both:
            return nrange,times
        else:
            return times

    def time_sieves():
        "simple timing demo"

        def plot_sieve(sieve,label):
            r,t = time_rng(sieve,rng,1,2)
            plt.plot(r,t,label=label)

        from matplotlib import pyplot as plt
        
        rng = np.linspace(1000,5000,20).astype(int)
        plt.figure()
        plt.title('Sieve of Erathostenes')
        plt.xlabel('Size')
        plt.ylabel('t(s)')

        plot_sieve(sieve,'Set-based')
        plot_sieve(sieve_quad,'Quad')
        plot_sieve(sieve_quad,'Quad2')

        plt.legend()
        plt.show()
        
    # This must be called LAST, because no code after it will be seen.
    print "To see timings comparison, call time_sieves()"
    unittest.main()
