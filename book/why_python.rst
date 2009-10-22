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

From their very inception computers have been linked to scientific work, so it
is worth noting that there is more than a bit of irony in the phrase
"Scientific Computing" we use today.  The very first electronic computers were
immediately used for solving differential equations and other problems that
required  large amounts of easy but repetitive numerical operations, a task
that was both slow and error prone (fperez - find Feynman's original
description of Los Alamos computation rooms).
    

Advantages of Python
--------------------


\begin{quotation}
*The canonical, \char`\"{}Python is a great first language\char`\"{*,
elicited, \char`\"{}Python is a great last language!\char`\"{}} --
Noah Spurrier 
\end{quotation}
This quotation summarizes an important reason scientists migrate to
Python as a programming language. As a {}``great first language''
Python has a simple, expressive syntax that is accessible to the newcomer.
{}``Python as executable pseudocode'' reflects the fact that Python
syntax mirrors the obvious and intuitive pseudo-code syntax used in
many journals \cite{Strous2001}. As a great first language, it does
not impose a single programming paradigm on scientists, as Java does
with object oriented programming, but rather allows one to code at
many levels of sophistication, including BASIC/FORTRAN/Matlab style
procedural programming familiar to many scientists. Here is the canonical
first program {}``hello world'' in Python:

\noindent {\small \begin{verbatim}
# Python
print 'hello world'
\end{verbatim}}  Contrast the simplicity of that program with the complexity {}``hello
world'' in Java  {\small \begin{verbatim}
// java 
class myfirstjavaprog
{  
  public static void main(String args[])
  {
    System.out.println("Hello World!");
  }
} 
\end{verbatim}} 

\noindent In addition to being accessible to new programmers and scientists,
Python is powerful enough to manage the complexity of large applications,
supporting functional programming, object orienting programming, generic
programming and metaprogramming. That Python supports these paradigms
suggests why it is also a {}``great last language'': as one increases
their programming sophistication, the language scales naturally. By
contrast, commercial languages like Matlab and IDL, which also support
a simple syntax for simple programs do not scale well to complex programming
tasks.

The built-in Python data-types and standard library provide a powerful
platform in every distribution \cite{PyLibRef,Lundh2001}. The standard
data types encompass regular and arbitrary length integers, complex
numbers, floating point numbers, strings, lists, associative arrays,
sets and more. In the standard library included with every Python
distribution are modules for regular expressions, data encodings,
multimedia formats, math, networking protocols, binary arrays and
files, and much more. Thus one can open a file on a remote web server
and work with it as easily as with a local file \begin{verbatim}
# this 3 line script downloads and prints the yahoo web site
from urllib import urlopen
for line in urlopen('http://yahoo.com').readlines():
   print line
\end{verbatim}

Complementing these built-in features, Python is also readily extensible,
giving it a wealth of libraries for scientific computing that have
been in development for many years \cite{Dubois1996b,Dubois1996c}.
``NumPy`` supports large array manipulations, math,
optimized linear algebra, efficient Fourier transforms and random
numbers. ``scipy`` is a collection of Python wrappers of high
performance FORTRAN code (eg LAPACK, ODEPACK) for numerical analysis
\cite{LAPACK}. ``IPython`` is a command shell ala Mathematica,
Matlab and IDL for interactive programming, data exploration and visualization
with support for command history, completion, debugging and more.
``Matplotlib`` is a 2D graphics package for making publication
quality graphics with a Matlab compatible syntax that is also embeddable
in applications. ``f2py}, \texttt{SWIG}, \texttt{weave``, and
``pyrex`` are tools for rapidly building Python interfaces to
high performance compiled code, ``MayaVi`` is a user friendly
graphical user interface for 3D visualizations built on top of the
state-of-the-art Visualization Toolkit \cite{SchroederEtal2002}.
``pympi}, \texttt{pypar}, \texttt{pyro}, \texttt{scipy.cow``,
and ``pyxg`` are tools for cluster building and doing parallel,
remote and distributed computations. This is a sampling of general
purpose libraries for scientific computing in Python, and does not
begin to address the many high quality, domain specific libraries
that are also available.

All of the infrastructure described above is open source software
that is freely distributable for academic and commercial use. In both
the educational and scientific arenas, this is a critical point. For
education, this platform provides students with tools that they can
take with them outside the classroom to their homes and jobs and careers
beyond. By contrast, the use commercial tools such as Matlab and IDL
limits access to major institutions. For scientists, the use of open
source tools is consistent with the scientific principle that all
of the steps in an analysis or simulation should be open for review,
and with the principle of reproducible research \cite{BuckheitDonoho1995}.


Mixed Language Programming
--------------------------


The programming languages of each generation evolve in part to fix
the problems of those that came before \cite{BerginEtal1996}. \textsc{FORTRAN},
the original high level language of scientific computing \cite{Rosen1967},
was designed to allow scientists to express code at a level closer
to the language of the problem domain. \textsc{ALGOL} and its successor
Pascal, widely used in education in the 1970s, were designed to alleviate
some of the perceived problems with \textsc{FORTRAN} and to create
a language with a simpler and more expressive syntax \cite{Backus1963,Naur1963}.
Object oriented programming languages evolved to allow a closer correspondence
between the code and the physical system it models \cite{GoldbergRobson1989},
and C++ provided a relatively high performance object orientated implementation
compatible with the popular C programming language \cite{Stroustrup1994,Stroustrup2000}.
But implementing object orientation efficiently requires programmers
stay close to the machine, managing memory and pointers, and this
created a lot of complexity in programs while limiting portability.
Interpreted languages such as Tcl, Perl, Python, and Java evolved
to manage some of the low-level and platform specific details, making
programs easier to write and maintain, but with a performance penalty
\cite{Ousterhout1998,ArnoldEtal2005}. For many scientists, however,
pure object oriented systems like Java are unfamiliar, and languages
like Matlab and Python provide the safety, portability and ease of
use of an interpreted language without imposing an object oriented
approach to coding \cite{VanRossumDrake2003,HanselmanLittlefield2004}.

The result of these several decades is that there are many platforms
for scientific computing in use today. The number of man hours invested
in numerical methods in \textsc{FORTRAN}, visualization libraries
in C++, bioinformatics toolkits in Perl, object frameworks in Java,
domain specific toolkits in Matlab, etc\dots requires an approach
that integrates this work. Python is the language that provides maximal
integration with other languages, with tools for transparently and
semi-automatically interfacing with \textsc{FORTRAN}, C, C++, Java,
.NET, Matlab, and Mathematica code \cite{Hugunin1997,Beazley1998}.
In our view, the ability to work seamlessly with code from many languages
is the present and the future of scientific computing, and Python
effectively integrates these languages into a single environment.


.. Links

- http://www.paulgraham.com/power.html
- Peter Norvig's talk at scipy'09