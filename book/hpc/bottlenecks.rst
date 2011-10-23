.. _bottlenecks:

=======================
Performance Bottlenecks
=======================

There is some computational resource (CPU cycles, memory speed,
disk IO, network IO) that prevents your program from being any faster
than it is. This is the bottleneck in your program, and you need to understand
it to improve its performance through parallelism.

.. warning::
    It is quite easy to assume that the bottleneck in a program is raw CPU
    cycles. But, with the architecture of today's CPUs, in particular the 
    memory subsystem, this is not always the case. Many computations are
    memory or IO bound, especially on multicore CPUs.

In this section, we give a brief qualitative description of the various
bottlenecks and how they are remediated or worsened on various parallel
hardware platforms.

Bottlenecks
===========

Raw CPU cycles
--------------

The most common bottleneck we think of is raw CPU cycles. The usual measure
of CPU cycles is FLOPS:

FLOPS
    The Floating Point Operation Per Second that a CPU is capable of performing.

Most CPUs are in the 1-2 GLOPS per core range currently.

.. warning::
    On a multicore CPU, you need to be very careful when looking at FLOPS
    to see if they are quoted on a per core, per CPU or per system
    basis.

Memory bandwidth
----------------

A given motherboard, CPU, and memory combination can only move data between
the CPU and main memory at a certain rate, called the memory bandwidth. If the
memory bandwidth is low, the memory subsystem won't be able to keep up with
the CPU's requests for data. In this situation, the CPU will literally sit
idle, starving for more data to chomp on.

The most important thing to know about memory bandwidth is that in current
CPUs is that memory bandwidth per FLOP is low. This means that many
calculations have a memory bandwidth bottleneck, rather than a CPU (FLOPS)
bottleneck. If your computation does relatively few arithmetic operations for
each memory access, you are likely in this regime. To speed up calculations
that have this characteristic, you don't need more cores, you need more memory
bandwidth!

For an overview of this issue, see Francesc Alted's `article
<http://www.pytables.org/docs/CISE-12-2-ScientificPro.pdf>`_ entitled "Why
Modern CPUs Are Starving and What Can Be Done About It."

.. warning::
    Because of complex, and rapidly changing, memory subsystems (multichannel
    memory, per core/GPU shared caches, NUMA) on current generation CPUs, it
    is a nightmare to interpret memory bandwidth numbers on multicore CPUs.

Disk IO
-------

Disks are capable of reading and writing a certain number of bytes per second.
Here are common bandwidths:

+----------+----------+
| SATA I   | 1.5 Gb/s |
+----------+----------+
| SATA II  | 3 Gb/    |
+----------+----------+
| SATA III | 6 Gb/s   |
+----------+----------+
| SAS I    | 3 Gb/s   |
+----------+----------+
| SAS II   | 6 Gb/s   |
+----------+----------+

Network IO
----------

We are all familiar with the bottleneck of network bandwidth.  Here are 
common bandwidths:

+------------------------------+--------------+
| Internet (US, Speedtest.net) | 10 Mb/s      |
+------------------------------+--------------+
| 100Mb Ethernet               | 100Mb/s      |
+------------------------------+--------------+
| 802.11n                      | 150-300 Mb/s |
+------------------------------+--------------+
| 1Gb Ethernet                 | 1Gb/s        |
+------------------------------+--------------+
| Infiniband (SDRx1)           | 2Gb/s        |
+------------------------------+--------------+
| Infiniband (QDRx4)           | 40 Gb/s      |
+------------------------------+--------------+

Bottlenecks and parallel hardware architectures
===============================================

It is important to understand how these bottlenecks are affected by various
parallel hardware architectures. The hope is that parallel hardware will
remove or remediate the bottlenecks and thus improve the performance of the
program when it is parallelized. As we will see, however, in some cases
parallel hardware will worsen existing bottlenecks and even create new ones.

Multicore CPUs and multiple CPUs Systems
----------------------------------------

* Multicore CPUs have greater FLOPS.  The number of FLOPS increases linearly
  with the number of cores.
* Multicore CPUs have very complex memory subsystems. In general, the total
  memory bandwidth is shared between the cores, so the bandwidth per core
  *decreases* as you increase the core count.
* No change in disk or network bandwidth.
* Very low communications latencies between cores which is great for 
  message passing.

Thus, multicore CPUs will:

* Help a CPU bottleneck.
* Likely not help a memory bandwidth bottleneck.

Cluster or supercomputer
------------------------

Typical clusters or supercomputers have a large number nodes, each with
multiple, multicore CPUs.

* Clusters have greater FLOPS. The number of FLOPS increases linearly with
  the total nusmber of cores.
* Cluster have greater memory bandwidth. The bandwidth increases linearly
  with the total number of nodes.
* The aggregate disk and network bandwidth of the cluster increases linearly
  with the number of nodes.
* Shared files systems, such as NFS, are a new bottleneck caused by the limited
  network bandwidth of the file server. This creates a massive bottleneck 
  for reading and writing files to the shared file system.
* Higher communications latency which is bad for message passing. Bandwidth
  and latency of node-to-node communications is determined by the network
  interconnect.

Thus clusters or supercomputers will:

* Help a CPU bottleneck.
* Help a memory bandwidth bottleneck.
* Help a disk IO bottleneck if you can use local disks.
* Create a new bottleneck in the shared filesystem.

Graphics Processing Units
-------------------------

* Great for FLOPS (above 1TFLOPS)
* Great memory bandwidth (many times that of modern CPUs) on the GPU.
* They have a new memory bottleneck between the GPU and main system memory.
* No disk or network IO improvements.
