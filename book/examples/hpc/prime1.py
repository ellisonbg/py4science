"""prime1.py: Pure Python versions of isprime and sum_primes."""

import math

def isprime(n):
    """Returns 1 if n is prime and 0 otherwise."""
    if not isinstance(n, int):
        raise TypeError("'int' expected, got: %r" % n)
    if n < 2:
        return 0
    if n == 2:
        return 1
    max = int(math.ceil(math.sqrt(n)))
    i = 2
    result = 1
    while i <= max:
        if n % i == 0:
            result = 0
            break
        i += 1
    return result

def sum_primes(n):
    """Returns the sum of the primes less than n."""
    return sum(i for i in xrange(2,n) if isprime(i))