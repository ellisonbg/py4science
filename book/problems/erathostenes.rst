.. F Perez

.. _erathostenes:

Prime numbers and the sieve of Erathostenes
===========================================

The sieve of Erathostenes is a simple and famous algorithm for factoring prime
numbers.  Try to implement it in Python (look it up first), and think of
different data structures you may use to do this.

Time the various implementations, do some analysis of the run times of each.

.. only:: instructor

   Solution
   --------

   .. literalinclude:: examples/erathostenes.py
   
   After calling ``time_sieves()``, we can see how much impact different data
   structure choices can have on algorithm run time:

   .. figure:: fig/erathostenes_timings.png
      :width: 4in
