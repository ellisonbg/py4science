"""prime1_mec.py: Parallelize prime1 using IPython's MultiEngineClient interface."""

from timeit import default_timer as timer
from IPython.kernel import client

from prime1 import isprime, sum_primes


if __name__ == '__main__':
    mec = client.MultiEngineClient()
    mec.execute('from prime1 import isprime, sum_primes')

    # We need to split the data in this way because the MultiEngineClient
    # won't load balance the inputs. This is needed because is takes longer
    # to sum the primes for alrger numbers.
    data = range(5000)
    data = data[0::2] + data[1::2]

    # Serial calculations
    t1 = timer()
    map(sum_primes, data)
    t2 = timer()
    serial_sum_primes = t2-t1
    print "Serial sum_primes time: ", serial_sum_primes

    # Parallel calculations
    t1 = timer()
    mec.map(sum_primes, data)
    t2 = timer()
    parallel_sum_primes = t2-t1
    print "Parallel sum_primes time: ", parallel_sum_primes

    print "Speedup of sum_primes on %i cores: %f" % \
        (len(mec), serial_sum_primes/parallel_sum_primes)
