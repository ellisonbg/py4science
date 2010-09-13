"""prime1_mp.py: Parallelize prime1 using multiprocessing."""

from timeit import default_timer as timer
from multiprocessing import Pool, cpu_count
from prime1 import isprime, sum_primes

ncpus = cpu_count()

if __name__ == '__main__':
    pool = Pool()

    # Serial calculations
    t1 = timer()
    map(isprime, xrange(20000))
    t2 = timer()
    serial_isprime = t2-t1
    print "Serial isprime time: ", serial_isprime

    t1 = timer()
    map(sum_primes, xrange(5000))
    t2 = timer()
    serial_sum_primes = t2-t1
    print "Serial sum_primes time: ", serial_sum_primes

    # Parallel calculations
    t1 = timer()
    pool.map(isprime, xrange(0,20000))
    t2 = timer()
    parallel_isprime = t2-t1
    print "Parallel isprime time: ", parallel_isprime

    t1 = timer()
    pool.map(sum_primes, xrange(0,5000))
    t2 = timer()
    parallel_sum_primes = t2-t1
    print "Parallel sum_primes time: ", parallel_sum_primes

    print "Speedup of isprime on %i cores: %f" % \
        (ncpus, serial_isprime/parallel_isprime)

    print "Speedup of sum_primes on %i cores: %f" % \
        (ncpus, serial_sum_primes/parallel_sum_primes)