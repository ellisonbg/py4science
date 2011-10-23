.. _conclusion:

===================
Concluding thoughts
===================

The tools
=========

* Unlike just a few years ago, there are many tools for parallelizing Python
  code. Many others (`parallel python <http://www.parallelpython.com/>`_, 
  `Disco <http://discoproject.org/>`_, ...) that we haven't mentioned.
* I get the feeling that we are still in the dark ages though.
* The GIL in CPython is hindering, but not stopping, efforts to create better
  tools for parallelizing Python code. Jython and IronPython present
  interesting opportunities in this regard.

Parallelizing your code
=======================

* No "one size fits all" tool or approach.
* No magic "go parallel" button or switch.
* Pay attention to things like bottlenecks, Amdahl's law and hardware
  architecture.
* Think differently about your programs and algorithms.
