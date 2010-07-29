=======================================
 F2Py: using Fortran codes from Python
=======================================

Python is a very flexible tool for numerical work, and with Numpy arrays under
the hood, it is often fast enough for serious usage. Still, there are many
valid reasons to ask for Fortran support: you may need to use an existing
library written in Fortran, collaborate with a colleague who doesn't program in
Python or want to write a low-level set of routines in Fortran so they can
benefit other Fortran-using colleagues as well as being available to Python.
While Numpy itself only uses C and Python, the Scipy package is built on a
large foundation of Fortran code, wrapping many well-tested, highly valuable
libraries such as LAPACK, FITPACK, ODRPACK and more.  It would be madness to
abandon the knowledge embedded in these tools, which have stood the test of
time and are still very useful for many purposes.  With Python, we can continue
to benefit from them while using them as part of a modern worfklow, thanks to
Numpy's f2py tool.

As we said, Numpy itself doesn't need Fortran at all, but it does provide the
f2py wrapper generator, so that by installing Numpy you automatically have the
tools needed to create Python wrappers for Fortran libraries (thus making it
possible to compile Scipy).  F2py was originally developed by Pearu Peterson;
here we will only present a brief tutorial introduction of its basic usage and
we refer our readers to the official documentation for complete details.

Further ahead we provide a description intended for readers comfortable with
the Python distutils machinery, who simply want a quick guide to f2py.  An
introductory tutorial with examples follows now.


The basic idea behind f2py
--------------------------

In a nutshell, f2py is a tool to auto-generate, based on Fortran sources, C
files that can be compiled into a Python extension module.  This module is then
imported in Python with the normal ``import`` statement, and it contains
functions that call into the original Fortran functions and subroutines.  This
process consists of two main steps:

1. Create an interface file that describes how the Fortran routines should
appear to the Python side, and the name of the Python module that will be
imported.  The interface file has a ``.pyf`` extension and its syntax is mostly
that of Fortran 90; f2py is capable of auto-generating it or it can be manually
written.  In practice, we have found that the best approach is to use the
auto-generated file as a starting point and then manually fine-tune some
details.

2. Generate, using the interface file from the previous step, a set of C source
files that can then be compiled into an extension module.  Once this extension
module is located in a location that Python can find, it can be imported just
like any other module.  This extension module contains C functions that
correspond to the underlying Fortran routines, but whose call signature is that
specified in the pyf interface file.

We will now illustrate the process with a few simple examples.


A first f2py example: Fibonacci numbers
---------------------------------------

The Fibonacci numbers, defined by the recursion

.. math::

    f_i = f_{i-1} + f_{i-2}

can be computed with the following simple Fortran code:

.. literalinclude:: examples/f2py/example1/fib.f
   :language: fortran
   :start-after: C FILE
   :end-before: C END FILE

If this code is in the ``fib.f`` file, then we can generate automatically the
sources for a Python module named ``pyfib`` with::

    f2py fib.f -h fib.pyf -m pyfib

In this command ``-h fib.pyf`` generates an interface file named ``fib.pyf``
from the Fortran sources in ``fib.f``.  This interface will declare a Python
module named ``pyfib``, specified with the ``-m pyfib`` flag.  After running
this command, the generated ``fib.pyf`` file is (stripped of some comments for
brevity): 

.. sourcecode:: fortran

   python module pyfib ! in 
       interface  ! in :pyfib
	   subroutine fib(f,n) ! in :pyfib:fib.f
	       real*8 dimension(n) :: f
	       integer optional,check(len(f)>=n),depend(f) :: n=len(f)
	   end subroutine fib
       end interface
   end python module pyfib

   
This is the file that will then tell f2py how to generate C sources that can
map Python arguments with numpy arrays into pointers that Fortran can interpret
as arrays.  For a function as simple as ``FIB(F, N)``, f2py is capable of
creating a good interface automatically. Each parameter of the Fortran
interface must be provided based on Python variables, but f2py is capable of
using the structure of Numpy arrays to help in this process.  For example, the
lines:

.. sourcecode:: fortran

       real*8 dimension(n) :: f
       integer optional,check(len(f)>=n),depend(f) :: n=len(f)
	       
mean that the variable ``f`` is a real array of dimension ``n``, and that the
integer parameter ``n`` can be computed as the length of ``f``.  Since from the
Python side the variable corresponding to ``f`` will be a Numpy array, and
Numpy arrays carry dimension information with them, f2py can compute ``n`` with
the code  ``n=len(f)``, and it can make ``n`` be an optional argument on the
python side.

The next step is to generate the actual C sources for the ``pyfib`` module and
to compile them; this is done with::

    f2py -c fib.pyf fib.f

Using the generated interface file and the Fortran sources, f2py will then
automatically generate and compile temporary C files that will produce the
requested Python extension module, ``pyfib.so``.  In our example, the module
will contain just one function, ``fib``, as indicated by its docstring::

    This module 'pyfib' is auto-generated with f2py (version:2).
    Functions:
      fib(f,n=len(f))
    .

And the ``fib`` function's interface will be::

    fib - Function signature:
      fib(f,[n])
    Required arguments:
      f : input rank-1 array('d') with bounds (n)
    Optional arguments:
      n := len(f) input int

The following simple makefile summarizes the process:

.. literalinclude:: examples/f2py/example1/Makefile
   :language: make

including a call to a short demonstration script, ``fibdemo.py``:
      
.. literalinclude:: examples/f2py/example1/fibdemo.py
   
While here we have illustrated the process with just one Fortran file, in
general, we start by building a scratch signature file automatically from our
Fortran sources::

    f2py -m MODULENAME -h MODULENAME.pyf *.f

We only need to list the Fortran files that we want to explicitly expose to
Python, any routines that are only used internally by the Fortran code do not
need to be listed (they will obviously need to be linked at runtime as a
library, but here we are only talking about the creation of a Python
interface).
    
This call writes the file ``MODULENAME.pyf``, making the best guesses it can
from the Fortran sources.  It builds an interface for the module to be accessed
as ``import MODULENAME`` from python.


Fine-tuning the interfaces
--------------------------

For most non-trivial codes, we will likely want to fine-tune the interface
generated by f2py based on our knowledge of the functions.  This means for
example making unnecessary scratch areas or array dimensions hidden, or making
certain parameters be optional and take a default value.  There are two ways to
achieve this: we can add special directives to the Fortran sources or we can
edit the auto-generated ``.pyf`` file.

In general, we recommend the latter approach because it is more explicit and
easier to debug.  But for very simple interfaces where the only thing needed is
perhaps to compute a couple of array dimensions return an array of this size,
with the values in it.  We can achieve this cleaner interface fairly easily, by
adding just a few Cf2py directives as shown here:


.. literalinclude:: examples/f2py/example2/fib2.f
   :language: fortran
   :start-after: C FILE
   :end-before: C END FILE

This file can now be directly compiled into a Python extension module with::

    f2py -c fib2.f -m pyfib2

and it results in:

.. ipython::

   In [5]: from pyfib2 import fib

   In [6]: fib?
   Type:		fortran
   String Form:	<fortran object at 0x935e8c0>
   Namespace:	Interactive
   Docstring:
       fib - Function signature:
	 a = fib(n)
       Required arguments:
	 n : input int
       Return objects:
	 a : rank-1 array('d') with bounds (n)


   In [7]: fib(10)
   Out[7]: array([  0.,   1.,   1.,   2.,   3.,   5.,   8.,  13.,  21.,  34.])

   
For a slightly more involved example, consider the following Fortran signature:

.. sourcecode:: fortran

	subroutine phipol(j,mm,nodes,wei,nn,x,phi,wrk)

	implicit real *8 (a-h, o-z)
	real *8 nodes(*),wei(*),x(*),wrk(*),phi(*)
	real *8 sum, one, two, half

The above is correctly handled by f2py, but it can't know what is meant to be
input/output and what the relations between the various variables are (such as
integers which are array dimensions).  If we add the following f2py directives,
the generated Python interface is a lot nicer:

.. sourcecode:: fortran

    subroutine phipol(j,mm,nodes,wei,nn,x,phi,wrk)
    
    c       Lines with Cf2py in them are directives for f2py to generate a better
    c	python interface.  These must come _before_ the Fortran variable
    c       declarations so we can control the dimension of the arrays in Python.
    c
    c       Inputs:
    Cf2py   integer check(0<=j && j<mm),depend(mm) :: j
    Cf2py   real *8 dimension(mm),intent(in) :: nodes
    Cf2py   real *8 dimension(mm),intent(in) :: wei
    Cf2py   real *8 dimension(nn),intent(in) :: x
    c
    c       Outputs:
    Cf2py   real *8 dimension(nn),intent(out),depend(nn) :: phi
    c
    c       Hidden args:
    c       - scratch areas can be auto-generated by python
    Cf2py   real *8 dimension(2*mm+2),intent(hide,cache),depend(mm) :: wrk
    c       - array sizes can be auto-determined
    Cf2py   integer intent(hide),depend(x):: nn=len(x)
    Cf2py   integer intent(hide),depend(nodes) :: mm = len(nodes)
    c
    implicit real *8 (a-h, o-z)
    real *8 nodes(*),wei(*),x(*),wrk(*),phi(*)
    real *8 sum, one, two, half


The f2py directives should come immediately after the 'subroutine' line and
before the Fortran variable lines. This allows the f2py dimension directives to
override the Fortran var(*) directives.

If the Fortran code uses var(N) instead of var(*), the f2py directives can be
placed after the Fortran declarations.  This mode is preferred, as there is
less redundancy overall.  The result is much simpler:

.. sourcecode:: fortran

    subroutine phipol(j,mm,nodes,wei,nn,x,phi,wrk)
    c
    implicit real *8 (a-h, o-z)
    real *8 nodes(mm),wei(mm),x(nn),wrk(2*mm),phi(nn)
    real *8 sum, one, two, half
    c
    c       The Cf2py lines allow f2py to generate a better Python interface.
    c
    c       Inputs:
    Cf2py   integer check(0<=j && j<mm),depend(mm) :: j
    Cf2py   intent(in) :: nodes
    Cf2py   intent(in) :: wei
    Cf2py   intent(in) :: x
    c
    c       Outputs:
    Cf2py   intent(out) :: phi
    c
    c       Hidden args:
    c       - scratch areas can be auto-generated by python
    Cf2py   intent(hide,cache) :: wrk
    c       - array sizes can be auto-determined
    Cf2py   integer intent(hide),depend(x):: nn=len(x)
    Cf2py   integer intent(hide),depend(nodes) :: mm = len(nodes)


Since python can automatically manage memory, it is possible to hide the need
for manually passed 'work' areas.  The C/python wrapper to the underlying
fortran routine will allocate the memory for the needed work areas on the fly.
This is done by specifying ``intent(hide,cache)``.  ``hide`` tells f2py to
remove the variable from the argument list and ``cache`` tells it to
auto-generate it.

In cases where the allocation cost becomes a performance problem, one can
remove the ``hide`` part and make it an optional argument.  In this case it
will only be generated if not given.  For this, the line above should be
changed to:

.. sourcecode:: fortran

    Cf2py   real *8 dimension(2*mm+2),intent(cache),optional,depend(mm) :: wrk

Note that this should only be done after _proving_ that the scratch areas are
causing a performance problem.  The ``cache`` directive causes f2py to keep
cached copies of the scratch areas, so no unnecessary mallocs should be
triggered.

With all this, the resulting f2py-generated docstring becomes::

    phipol - Function signature:
      phi = phipol(j,nodes,wei,x)
    Required arguments:
      j : input int
      nodes : input rank-1 array('d') with bounds (mm)
      wei : input rank-1 array('d') with bounds (mm)
      x : input rank-1 array('d') with bounds (nn)
    Return objects:
      phi : rank-1 array('d') with bounds (nn)

      
Fortran 90
----------

F2py understands almost all F90 constructs (with some limitations in the use of
derived types), and as we have already seen, f2py directives are basically F90
expressions with an additional allowance for small snippets of code to extract
information from numpy arrays.  It should then come as no surprise that if you
use F90 sources and declare your variable intents explicitly at the Fortran
level, this will help f2py even more when generating the interface, minimizing
the required amount of manual intervention.

A complete example
------------------

Now we show a short but complete example that includes the necessary
``setup.py`` file so that the resulting extension can be installed like any
other python package.  If we have the source file ``simple.f90``:

.. literalinclude:: examples/f2py/example4/simple.f90
   :language: fortran

and the interface file ``simple.pyf``:
   
.. literalinclude:: examples/f2py/example4/simple.pyf
   :language: fortran

we only need to write a ``setup.py`` file using distutils, and list the
``.pyf`` file along with the Fortran sources it is meant to wrap.  f2py will
build the module for us automatically, respecting all the interface
specifications we made in the ``.pyf`` file.  Here is the necessary
``setup.py``:

.. literalinclude:: examples/f2py/example4/setup.py
   

Debugging
---------

For debugging, use the ``--debug-capi`` option to f2py.  This causes the
extension modules to print detailed information while in operation.  In
distutils, this must be passed as an option in the f2py_options to the
Extension constructor.
