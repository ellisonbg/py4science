.. _why_python:

=====================================
 Why Python for scientific computing
=====================================

.. todo::

    Notes for this chapter, mostly reminders for myself.  These can be toggled
    off via the todo_include_todos flag in conf.py.
    
    - Write a bit more about the history of computing in science?
    - How much to go back on computer language details?
    - How much history of Python to put in?

    
A bit of history
================
    
From their very inception computers have been linked to scientific work, so it
is worth noting that there is more than a bit of irony in the phrase
"Scientific Computing" we use today: originally *all* of computing was
scientific in nature.  The very first electronic computers were immediately
used for solving differential equations and other problems that required large
amounts of easy but repetitive numerical operations, a task that was both slow
and error prone :fperez:`find Feynman's original description of Los Alamos
computation rooms`.  For a long time, computing equipment was a a scarce and
expensive resource, and simple economics dictated that priority was given to
maximizing the efficiency in using this expensive hardware.  Whether
programming the computers in an efficient manner was an easy or difficult and
time-consuming process for the human programmer was therefore a secondary
consideration, and this meant that the first years of programming meant writing
essentially in the very language the machine was built to understand at the
hardware level.  This rapidly proved to be prohibitively difficult, and around
1954, John Backus started a project at IBM research that would revolutionize
computing: his team designed the Fortran programming language [#]_, the first
"high-level" computer programming language, meaning that it could be reasonably
written and read by humans, and an automatic tool (known as a compiler) would
translate it into a low-level form suitable for the computer to execute.

Over the years other languages were developed, but Fortran remained the
dominant tool for numerical and scientific work.  But the more computers became
available, the more Fortran began to feel still too "low-level", and even
higher-level languages were developed that made it easy to load data, perform
numerical operations with entire arrays of numbers without explicitly looping
over all of them, and visualize the results.  The most popular of these systems
today is Matlab(TM), invented in the late 1970's by Cleve Moler when he was a
professor at the University of New Mexico who wanted his numerical analysis
students to be able to focus on the mathematical core of the algorithms he was
teaching them rather than the pesky details of programming in Fortran.  Matlab,
short for MATrix LABoratory, was originally designed to make it very easy to
express linear algebra algorithms and access libraries of Fortran routines.  A
few key ideas that Matlab introduced, and that will be constant themes of this
book, were:

* An interactive environment where code could be typed and its results
  immediately viewed, without necessarily having to compile a program each
  time.

* High-level syntax to express whole-array operations, so that the sum
  $\mathbf{C}$ of two matrices $\mathbf{A}$ and $\mathbf{B}$ could be written
  simply as $\mathbf{C=A+B}$, for example, instead of a double loop over all
  the elements $c_{ij} = a_{ij} + b_{ij}$.

* Integrated access to many common algorithms, such as eigenvalue
  decompositions or linear solvers (and today, much more).

* Integrated visualization, so that results could not only be printed, but also
  plotted in many different ways, directly from within the interactive
  environment.

These features, combined, represented a dramatic improvement when compared to a
workflow based on explicitly writing programs in Fortran, linking to the
appropriate libraries, waiting for them to complete execution, and then loading
their outputs into separate plotting and visualization systems.  It is no
surprise that Matlab became wildly popular, with a company being built around
the original program that has grown to employing more than 2000 employees
worldwide as of 2009.  Although we have no space here for a comprehensive
history of mathematical computing, we should at least mention the existence of
a few other large, commercial systems whose use cases overlap with Matlab: IDL,
Mathematica and Maple.

IDL (short for Interactive Data Language) was born in a way broadly similar to
Matlab, but from the Laboratory for Atmospheric and Space Physics (LASP) at the
University of Colorado at Boulder.  It is also widely used today, especially in
the astronomy and earth sciences.  Mathematica and Maple have their roots in
symbolic manipulation and exact numerical operations (as opposed to the
floating-point-oriented nature of Matlab and IDL), but today have also grown to
offer extensive numerical support.

Python: a high-level language scientsts can use
===============================================

This is then the context where we encounter Python: one of scientists used to
systems that enable a rapid workflow of interactive and exploratory computing,
with built-in support for many numerical libraries and sophisticated
visualization.  As we will see in this book, Python offers all of these
features, but it was not developed as a numerical programming language from the
beginning.  Instead, Python was originally developed as a language to do
systems programming with a higher-level syntax than C.  We will briefly mention
a few highlights of Python's history, in particular as they are relevant to the
purpose of our book.  But we encourage you to visit the `History of Python`_
blog where Guido van Rossum, the creator of the language, presents a detailed
and fascinating personal account of Python's evolution.

.. _history of python: python_history_

Guido van Rossum worked at the CWI Dutch mathematics research institute and had
worked for a few years on a project to develop an educational programming
language called ABC.  In the late 1980's he joined a group developing a
distributed operating system called Amoeba, and found himself needing a way to
rapidly develop utilities for Amoeba that would fit the system's architecture
better than the Bourne shell and yet would be easier to use than pure C.  While
the ABC project had not been very successful in finding widespread adoption of
the language, Guido found a lot of useful ideas in its design, and decided to
develop a language that would "bridge the gap between C and the shell", taking
these good features from ABC and trying to address the shortcomings they had
found in it.  So in a sense, in the end ABC did turn out to be a success, if we
think of it as a laboratory where the design of Python incubated, allowing
Guido to start from a set of solid ideas for an easy to understand and use
language where programmers could be productive quickly, and that would encourage
the creation of clear and maintainable programs.

The first public release of Python was for version 0.9.0, which was posted to
the internet newsgroup ``alt.sources`` on February 20, 1991.  After that, the
internet dynamics of collaboration engaged, and Guido found interest,
encouragement and eventually contributions coming from many sides, leading to
what is today a project used worldwide in industry and academia.

It is worth noting that despite the fact that Python was designed as a support
tool for an operating systems research project, scientific institutions had a
close relationship with Python since the beginning: it was born at a
mathematics research center; the first Python workshop was held at the United
States' National Institute of Standards and Technology (NIST); the subsequent
development of Python and the initial effort on Jython, the Java port of
Python, were funded by the US Defense Advanced Research Projects Agency
(DARPA); the second and third Python workshops took place at the US Geological
Survey and the next at the Lawrence Livermore National Laboratory.

All of this is an indication that scientists rapidly saw value in Python's
clarity, though initially most of its use was as a 'computational steering'
language: basically as an easy to use language to drive the execution of
traditional high-performance codes written in Fortran, C and C++, preparing
their inputs and post-processing their outputs for analysis and visualization.
At the time, Python's facilities to express numerical array operations
effectively was somewhat limited, and there wasn't really too much support for
other scientific tools like complex numerical libraries, access to external
Fortran codes or data visualization.

:fperez:`check this part for accuracy, ask Eric and Travis for a quick review`

In the late 1990's, an MIT graduate student named Jim Hugunin decided that
Python could actually be useful directly for numerical work, but that for this
to be really practical it would need support for proper numerical arrays much
like those in Matlab or IDL.  From this, the ``Numeric`` array library was born
and was rapidly adopted by scientists, including strong support and development
contributions from Paul Dubois at Lawrence Livermore National Laboratory.
Numeric formed the structural backbone of Python as a language for direct
scientific work for a few years, and around the year 2000 Eric Jones, Travis
Vaught, Travis Oliphant and Pearu Peterson joined forces and various libraries
they had independently developed, critically including the ``f2py`` tool that
made it possible to easily wrap existing Fortran codes.  With ``f2py`` in their
arsenal, they were able to wrap a number of classic, battle-proven Fortran
libraries from Netlib_, including the key linear algebra LAPACK_ tools, and
thus was the Scipy_ project born.  Eric and Travis Vaught founded Enthought
Inc, a scientific computing and consulting company that provided much of the
initial support for Scipy, as they successfully combined their commercial
endeavors with a clear commitment to building the open source foundations of
Python for scientific work, offering hosting for related projects and making
all of the Scipy code open source since the beginning.

Initially, Scipy was a collection of packages built on top of Numeric that
combined numerical libraries with tools for interactive work and data
visualization, in a similar manner to Matlab.  In late 2001 one of us (F.P.)
started using Python for his PhD research work, and in the process started
developing IPython_, an improved interactive environment to facilitate the
workflows he was used to from IDL and Mathematica under Python.  Eric Jones
offered to host IPython at the Scipy project site, and IPython began to
accumulate both interactive and plotting features (by interfacing with the
venerable Gnuplot program).  In 2002 another one of us (J.D.H) needed to
improve IPython's plotting support to support Matlab-style syntax, and sent
to F.P. some contributions on this front, but unfortunately F.P. was at the
time too busy actually finishing up his PhD to be able to properly handle this,
and his reply was along the lines of "many thanks, but I can't look at your
code until I finish writing my dissertation".


Open source tools and scientific work
=====================================

There is a key aspect in which Python differs from the systems we described
above.  All of them are commercial products whose internal source code is
proprietary and not available to the normal user.  In contrast, the Python
language is created by an open group of developers who collaborate over the
Internet, and who make the entire system available to download, use and improve
free of any charge.  This has some very important consequences:

Financial
   The licensing cost to use one or one thousand copies of Python is the same:
   zero.  This can be a very important consideration if your budget is finite,
   as a commercial environment like the above, fully loaded with optional
   toolkits, can be extremely expensive.

Open access to methods and data
   The ability to understand validate and reproduce any result is one of the
   core tenets of the scientific method, so as a matter of principle black-box
   systems that are not open to inspection should not have a role in science.
   Even if in practice many constraints make it impossible to actually verify
   every result we read in the literature, at least we all agree on the
   principle that an author who *refuses* to explain his methods carries little
   scientific credibility.  Yet for the systems listed above, you are not
   allowed to inspect their internal workings (and in fact, legal clauses in
   their licenses prevent you from even attempting this).

   For example, data files saved in IDL are stored in a well-structured format,
   but they also contain the following notice: *IDL Save/Restore files embody
   unpublished proprietary information about the IDL program. Reverse
   engineering of this file is therefore forbidden under the terms of the IDL
   End User License Agreement.  [...] Non-RSI supplied software that reads or
   writes files in the IDL Save/Restore must have a license from Research
   Systems explicitly granting the right to do so.* Do you really want to be
   legally forbidden from accessing your own data in the future, if you need to
   do so with a different program?

Participatory position
   There is an important difference between purchasing a product for which you
   can only passively request help from a vendor, and using something to which
   from the very first day you are welcome to actively contribute.  While not
   all users may want to improve the tools they use, as scientists we are by
   definition pushing the limits of our tools, and as educators we want our
   students to become as actively engaged with the scientific process as
   possible.  All the projects and libraries we will present throughout this
   book encourage the participation of anyone interested and welcome new
   contributors.  This means that an interested student can easily become a key
   contributor to a project solely based on the quality of his or her work in
   an open community, instead of being relegated to the position of a consumer
   who is expected to renew a license (for a fee) at the end of each year.


   

Advantages of Python
====================

    The canonical, "Python is a great first language" elicited, "Python is a
    great last language!".
    
    Noah Spurrier

This quotation summarizes an important reason scientists migrate to Python as a
programming language. As a "great first language" Python has a simple,
expressive syntax that is accessible to the newcomer.  "Python as executable
pseudocode" reflects the fact that Python syntax mirrors the obvious and
intuitive pseudo-code syntax used in many journals :cite:`Strous2001`. As a
great first language, it does not impose a single programming paradigm on
scientists, as Java does with object oriented programming, but rather allows
one to code at many levels of sophistication, including BASIC/Fortran/Matlab
style procedural programming familiar to many scientists. Here is the canonical
first program ``hello world`` in Python::

    print 'hello world'

Contrast the simplicity of that program with the complexity of an equivalent
``hello world`` in Java:

.. sourcecode::
   java
   
   class myfirstjavaprog
   {  
     public static void main(String args[])
     {
       System.out.println("Hello World!");
     }
   } 

In addition to being accessible to new programmers and scientists, Python is
powerful enough to manage the complexity of large applications, supporting
functional programming, object orienting programming, generic programming and
metaprogramming. That Python supports these paradigms suggests why it is also a
"great last language": as one increases their programming sophistication, the
language scales naturally. By contrast, commercial languages like Matlab and
IDL, which also support a simple syntax for simple programs do not scale well
to complex programming tasks.

The built-in Python data-types and standard library provide a powerful
platform in every distribution :cite:`PyLibRef,Lundh2001`. The standard
data types encompass regular and arbitrary length integers, complex
numbers, floating point numbers, strings, lists, associative arrays,
sets and more. In the standard library included with every Python
distribution are modules for regular expressions, data encodings,
multimedia formats, math, networking protocols, binary arrays and
files, and much more. Thus one can open a file on a remote web server
and work with it as easily as with a local file::

    # this 3 line script downloads and prints the yahoo web site
    from urllib import urlopen
    for line in urlopen('http://yahoo.com').readlines():
       print line


* Quicksort
       
Complementing these built-in features, Python is also readily extensible,
giving it a wealth of libraries for scientific computing that have been in
development for many years :cite:`Dubois1996b,Dubois1996c`.  ``NumPy`` supports
large array manipulations, math, optimized linear algebra, efficient Fourier
transforms and random numbers. ``scipy`` is a collection of Python wrappers of
high performance Fortran code (eg LAPACK, ODEPACK) for numerical analysis
:cite:`LAPACK`. ``IPython`` is a command shell ala Mathematica, Matlab and IDL
for interactive programming, data exploration and visualization with support
for command history, completion, debugging and more.  ``Matplotlib`` is a 2D
graphics package for making publication quality graphics with a Matlab
compatible syntax that is also embeddable in applications. ``f2py``, ``SWIG``,
``weave``, and ``pyrex`` are tools for rapidly building Python interfaces to
high performance compiled code, ``MayaVi`` is a user friendly graphical user
interface for 3D visualizations built on top of the state-of-the-art
Visualization Toolkit :cite:`SchroederEtal2002`.  ``pympi``, ``pypar``,
``pyro``, ``scipy.cow``, and ``pyxg`` are tools for cluster building and doing
parallel, remote and distributed computations. This is a sampling of general
purpose libraries for scientific computing in Python, and does not begin to
address the many high quality, domain specific libraries that are also
available.

All of the infrastructure described above is open source software
that is freely distributable for academic and commercial use. In both
the educational and scientific arenas, this is a critical point. For
education, this platform provides students with tools that they can
take with them outside the classroom to their homes and jobs and careers
beyond. By contrast, the use commercial tools such as Matlab and IDL
limits access to major institutions. For scientists, the use of open
source tools is consistent with the scientific principle that all
of the steps in an analysis or simulation should be open for review,
and with the principle of reproducible research :cite:`BuckheitDonoho1995`.


Mixed Language Programming
--------------------------


The programming languages of each generation evolve in part to fix the problems
of those that came before :cite:`BerginEtal1996`. Fortran, the original high
level language of scientific computing :cite:`Rosen1967`, was designed to allow
scientists to express code at a level closer to the language of the problem
domain. ALGOL and its successor Pascal, widely used in education in the 1970s,
were designed to alleviate some of the perceived problems with Fortran and to
create a language with a simpler and more expressive syntax
:cite:`Backus1963,Naur1963`.  Object oriented programming languages evolved to
allow a closer correspondence between the code and the physical system it
models :cite:`GoldbergRobson1989`, and C++ provided a relatively high
performance object orientated implementation compatible with the popular C
programming language :cite:`Stroustrup1994,Stroustrup2000`.  But implementing
object orientation efficiently requires programmers stay close to the machine,
managing memory and pointers, and this created a lot of complexity in programs
while limiting portability.  Interpreted languages such as Tcl, Perl, Python,
and Java evolved to manage some of the low-level and platform specific details,
making programs easier to write and maintain, but with a performance penalty
:cite:`Ousterhout1998,ArnoldEtal2005`. For many scientists, however, pure
object oriented systems like Java are unfamiliar, and languages like Matlab and
Python provide the safety, portability and ease of use of an interpreted
language without imposing an object oriented approach to coding
:cite:`VanRossumDrake2003,HanselmanLittlefield2004`.

The result of these several decades is that there are many platforms for
scientific computing in use today. The number of man hours invested in
numerical methods in Fortran}, visualization libraries in C++, bioinformatics
toolkits in Perl, object frameworks in Java, domain specific toolkits in
Matlab, etc... requires an approach that integrates this work. Python is the
language that provides maximal integration with other languages, with tools for
transparently and semi-automatically interfacing with Fortran, C, C++, Java,
.NET, Matlab, and Mathematica code :cite:`Hugunin1997,Beazley1998`.  In our
view, the ability to work seamlessly with code from many languages is the
present and the future of scientific computing, and Python effectively
integrates these languages into a single environment.


.. Links

- http://www.paulgraham.com/power.html
- Peter Norvig's talk at scipy'09

.. [#] Fortran is an acronym for FORmula TRANslation, as the language was
   mostly designed to encode mathematical formulas for the computer.

.. include:: links.txt
