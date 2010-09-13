.. _speedup:

=================================
Parallel Speedup and Amdahl's Law
=================================

Parallel Speedup Defined
========================

The speedup :math:`S` is one possible way of quantifying the performance of
a parallel program. The idea is to compare the execution time of the
parallel version, :math:`T_p`, with that of a serial version, :math:`T_s`.

* :math:`T_s` = serial time = time on one core/processor:
* :math:`T_p` = parallel time = time on :math:`N` cores/processors:

The speedup is defined as the ratio of the two:

.. math::

    S = \frac{T_s}{T_p}

Usually, the best speedup you can hope for is :math:`N`. This means that a
program will run :math:`N` times as fast on :math:`N` processors as it does on
1.

Amdahl's Law
============

Imagine hearing this:

    I just purchased an expensive new 512 core workstation and spent a month
    parallelizing my program. But it is only 10 times as fast, not 512 times.
    Did I just waste my entire budget on this workstation? What on earth is
    going on?

`Amdahl's law <http://en.wikipedia.org/wiki/Amdahl's_law>`_ gives a strict 
upper bound on the speedup :math:`S` you can get running on :math:`N` cores.

.. warning::

    Amdahl's law is *bad news*.

* :math:`P` = fraction of a program that can be parallelized.
* :math:`1-P` = fraction of a program that *cannot* be parallelized. This
  is the serial fraction.

Amdahl's law predicts the best case speedup the program will have when run on
:math:`N` processors:

.. math::

    S = \frac{1}{(1-P)+\frac{P}{N}}

.. plot:: code/speedup.py

But it gets worse. Amdahl's law predicts a maximum speedup as :math:`N`
goes to :math:`\infty`:

.. math::

    S_{max} = \lim_{N \to \infty} = \frac{1}{(1-P)}

Thus, no matter how many processors/cores you throw at your program, it won't
ever get faster than this!

.. plot:: code/max_speedup.py

.. note::
    Amdahl's law assume that the problem size remains fixed as the number
    of cores/processors is increased. Gustafson has derived a
    `less pessimistic <http://www.scl.ameslab.gov/Publications/Gus/AmdahlsLaw/Amdahls.html>`_,
    but equivalent, version of Amdahl's law by assuming that the problem size
    increases linearly with :math:`N` while keeping the total execution time 
    fixed.

Estimating the parallel faction
===============================

For a given program, it can be very difficult to determine the parallel
fraction :math:`P` required in Amdahl's law. Fortunately, there is a simple
way of estimating it. Here is how it works.

1. Run your program on :math:`N=1` core and record the execution time 
   :math:`T_1`.
2. Run your program in parallel on a specific number of cores :math:`N` and 
   record the execution time :math:`T_N`.
3. Compute the observed speedup: :math:`S=T_1/T_N`.

The estimated parallel fraction is then:

.. math::

    P = \frac{\frac{1}{S}-1}{\frac{1}{N}-1}

Obviously, this estimate is unable to distinguish between the speedup loses
due to the serial fraction and other factors like bottlenecks, sub-optimal 
parallel algorithms, communication overhead, etc. But, it is a starting point.


Summary
=======

* To get good parallel speedup, you want to maximize the parallel fraction 
  :math:`P`, and minimize the serial faction of your program.
* Minimally, you need to be realistic about how much speedup you will 
  observe when running your program on :math:`N` cores.
* Don't ignore Amdahl's law or you will be disappointed.

