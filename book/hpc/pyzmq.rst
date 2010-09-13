.. _pyzmq_chapter:

=====
PyZMQ
=====

This chapter describes a relatively new message passing library, called
`ØMQ <http://www.zeromq.org/>`_ or "ZeroMQ", and its Python wrappers
`PyZMQ <http://github.com/ellisonbg/pyzmq>`_.

ØMQ
===

* C++ messaging library.
* Extremely simple, but powerful API.
* Dead simple binary wire protocol. You get to pick your own serialization
  technique (JSON, XML, Protocol Buffers).
* A lightweight socket-like API.
* Fully distributed, broker-less design, so no single point of failure.
* Supports different messaging patterns: publish/subscribe, request/reply, etc.
* Super fast.  Designed for low latency applications.
* "Sockets on steroids", "Pimped socket interface".
* 15 language bindings.
* The anti-MPI in term of being flexible and dynamic.
* Runs on different network interconnects.

For a great overview, see this `blog post
<http://nichol.as/zeromq-an-introduction>`_ by Nicholas Peil.

PyMZQ
=====

* Cython based Python wrapper to 0MQ.
* No problems with the GIL!
* Near C++ performance.
* Integration with Tornado web server.
* See my talk later this week!