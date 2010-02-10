==============
 Problem sets
==============

The index* files in this folder are used to create problem sets, with each
problem living in a file by itself so they can be easily assembled into
different problem sets.

The conf.py file is set up to generate student/instructor versions of the
problems; to switch between the student and instructor version of a file,
comment out the necessary lines in conf.py that add tags to the ``tags``
variable.

To include the solution for the instructor, you can include text conditionally
using::

    .. only:: instructor

       Solution
       --------

       A solution to this problem is here:

       .. literalinclude:: examples/wordfreqs.py

Note, however, that if you do this, any headings in the conditional section
*must* be one level deeper than those in the main text.  This is a sphinx
limitation.  If you want conditional text that has headings at the same level,
put the contents in a second file and include it like this::

    .. only:: instructor

       .. toctree::

	  bessel_sol
	  
and the _sol file can have any markup/directives you want, and headings at any
level.

There should be one index file per desired problem set, and the conf.py file
should be adapted to list these.  You can keep in the final latex_documents
variable only the ones you wish to actually compile to pdf, as the main book
build is rather lengthy.

The name of the generated pdf is defined in the conf.py file, it doesn't need
to match the name of the index file.
