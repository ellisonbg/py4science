"""prime2.pyx: Fast Cython versions of isprime and sum_primes."""

cimport cython
import math

cdef extern from "math.h" nogil:
    double ceil(double)
    double sqrt(double)

# This decorator is needed to disable ZeroDivisionError being raised while
# the GIL is released in the ``if n % i == 0`` line.
@cython.cdivision(True)
cdef int _isprime(unsigned long long n) nogil:
    """Fast, pure C version of isprime."""
    if n < 2:
        return 0
    if n == 2:
        return 1
    cdef unsigned long long max = <unsigned long long>ceil(sqrt(<double>n))
    cdef unsigned long long i = 2
    cdef int result = 1
    while i <= max:
        if n % i == 0:
            result = 0
            break
        i += 1
    return result

def isprime(unsigned long long n):
    """Returns 1 if n is prime and 0 otherwise."""
    cdef int result
    with nogil:
        result = _isprime(n)
    return result

def sum_primes(unsigned long long n):
    """Returns the sum of the primes less than n."""
    cdef unsigned long long result = 0
    cdef unsigned long long i
    with nogil:
        for i in range(2,n):
            if _isprime(i) == 1:
                result += i
    return result
