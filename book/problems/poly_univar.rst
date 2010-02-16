Univariate polynomials
======================

This continues our previous exercise with univariate polynomials, but in a
slightly more generalized formulation.  Now, consider solving the equation:

.. math::

   x^2 \sum_i{\frac{a_i}{a_i x + b_i}} = k

where $\mathbf a$, $\mathbf b$ are arrays and $k$ is a scalar.  Again, this can
be rewritten in terms of finding the roots of $R(x)$

.. math::

  R(x) \equiv x^2 P(x) - k Q(x)

outside of the roots of Q(x), where

.. math::

  P(x) = \sum_i a_i \prod_{j \neq i} a_j x+ b_j

and

.. math::

   Q(x)=\prod_i a_i x + b_i


In this problem, you must compute this polynomial R(x) using both numpy and
sympy, and then find its roots via numpy (sympy has limited support for
numerical root finding).

First, use :class:`np.poly1d` as before to construct $R(x)$, but now from a pair
of arrays $\mathbf a$ and $\mathbf b$. Normalize $R(x)$ so its leading
coefficient is 1 to avoid ambiguity.

As a validation reference, if the inputs are::

    a = np.array([3.4, 4.5, 3.2])
    b = np.array([2.1, 5.5, 4.5])
    k = 0.5

then you should obtain the following $R(x)$ and roots::


    Numpy, R(x) =
       4         3          2
    1 x + 1.997 x + 0.5731 x - 0.557 x - 0.1769

    Roots: [-1.32141936 -0.86720646 -0.30879126  0.50000423]

You must pay attention to the (unfortunate) fact that numpy's ``poly1d``
objects, when combined in binary operations like addition or multiplication
with scalars obtained from numpy arrays, behave in rather counterintuitive
ways.  Observe:

.. ipython::

   In [26]: p = np.poly1d([2, 3])

   In [27]: a = np.array([3.5, 4.5])

   In [28]: p + 3.5
   Out[28]: poly1d([ 2. ,  6.5])

   In [29]: p + a[0]
   Out[29]: poly1d([ 2. ,  6.5])

   In [30]: a[0] + p
   Out[30]: array([ 5.5,  6.5])

As you can see, addition is not commutative!  There's an obscure reason for
this behavior and an ongoing discussion on the numpy list on how to best
resolve it.  It should be noted that in newer versions of numpy (after February
2010), a new Polynomial class will be available that provides more
sophisticated behavior than the basic poly1d shown here.

In the meantime, the simple solution is to call :func:`float()` on all scalars
before combining them with ``poly1d`` objects:

.. ipython::

   In [31]: p + 3.5
   Out[31]: poly1d([ 2. ,  6.5])

   In [32]: p + float(a[0])
   Out[32]: poly1d([ 2. ,  6.5])

   In [33]: float(a[0]) + p
   Out[33]: poly1d([ 2. ,  6.5])

    
Next, use Sympy to construct a generic form of $R(x)$, that works both if the
``(a, b, k)`` are given, and if instead the user specifies only the number of
desired terms in the construction.  In this case, the returned value should be
a symbolic polynomial.  You can use the following signature and docstring to
get started.  Note that when a function has *all* of its arguments take a None
default value, it means that in order to actually use it users must supply at
least some of them, but they are mutually exclusive.  In this case, you must
provide *either* ``(na, nb, nk)`` as numerical arrays, *or* ``nterms``::

    def sym_rpoly(na=None, nb=None, nk=None, nterms=None):
	"""Compute the R polynomial as defined above.

	Internally the construction of R is done symbolically. If the numerical
	variables (na, nb, nk) were supplied, these values are substituted at the
	end and a sympy.Poly object with numerical coefficients is returned.  If
	(na, nb, nk) are not given, then nterms *must* be given, and a symbolic
	answer is returned.

	Parameters
	----------
	na : ndarray, optional
	  Numerical array of 'a' coefficients.

	nb : ndarray, optional
	  Numerical array of 'b' coefficients.

	k : float, optional
	  Numerical value of k.

	nterms : int, optional.
	  Number of terms. This is only used if na, nb and nk are *not* given, in
	  which case a symbolic answer is returned with nterms total.

	Returns
	-------
	poly : sympy.Poly instance
	  A univariate polynomial in x.

	Examples
	--------
	With only nterms, a symbolic polynomial is returned:
	>>> sym_rpoly(nterms=1)
	Poly(x**2 - k*x - b_0*k/a_0, x)

	But if numerical values are supplied, the output polynomial has numerical
	values:
	>>> sym_rpoly([2], [5], 3)
	Poly(x**2 - 3*x - 15/2, x)
	>>> sym_rpoly([1, 2], [4, 6], 1)
	Poly(x**3 + 3*x**2 - 7/2*x - 6, x)"""

For example, for 1 and 2 terms you should obtain::
    
    In [35]: sym_rpoly (nterms=1)
    Out[35]: Poly(x**2 - k*x - b_0*k/a_0, x)

    In [36]: sym_rpoly (nterms=2)
    Out[36]: Poly(x**3 + (a_0*b_1 + a_1*b_0 - a_0*a_1*k)/(2*a_0*a_1)*x**2 +
    (-a_0*b_1*k - a_1*b_0*k)/(2*a_0*a_1)*x - b_0*b_1*k/(2*a_0*a_1), x)


For this symbolic construction, you will find it useful to create arrays of
symbolic elements.  For this, you can use the following little utility in your
code (this has been included in Sympy itself as of Feb 15 2010)::

    def symarray(shape, prefix=''):
	"""Create a numpy ndarray of symbols (as an object array).

	The created symbols are named prefix_i1_i2_...  You should thus provide a
	non-empty prefix if you want your symbols to be unique for different output
	arrays, as Sympy symbols with identical names are the same object.

	Parameters
	----------

	shape : int or tuple
	  Shape of the created array.  If an int, the array is one-dimensional; for
	  more than one dimension the shape must be a tuple.

	prefix : string
	  A prefix prepended to the name of every symbol.

	Examples
	--------

	>>> symarray(3)
	array([_0, _1, _2], dtype=object)

	If you want multiple symarrays to contain distinct symbols, you *must*
	provide unique prefixes:
	>>> a = symarray(3)
	>>> b = symarray(3)
	>>> a[0] is b[0]
	True
	>>> a = symarray(3, 'a')
	>>> b = symarray(3, 'b')
	>>> a[0] is b[0]
	False

	Creating symarrays with a prefix:
	>>> symarray(3, 'a')
	array([a_0, a_1, a_2], dtype=object)

	For more than one dimension, the shape must be given as a tuple:
	>>> symarray((2,3), 'a')
	array([[a_0_0, a_0_1, a_0_2],
	       [a_1_0, a_1_1, a_1_2]], dtype=object)
	>>> symarray((2,3,2), 'a')
	array([[[a_0_0_0, a_0_0_1],
		[a_0_1_0, a_0_1_1],
		[a_0_2_0, a_0_2_1]],
	<BLANKLINE>
	       [[a_1_0_0, a_1_0_1],
		[a_1_1_0, a_1_1_1],
		[a_1_2_0, a_1_2_1]]], dtype=object)
	"""
	arr = np.empty(shape, dtype=object)
	for index in np.ndindex(shape):
	    arr[index] = sym.Symbol('%s_%s' % (prefix, '_'.join(map(str, index))))
	return arr

    
Finally, convert this symbolic object to a numerical :class:`np.poly1d` object
so you can validate your numpy solution against the symbolic one, and also
compute its roots (sympy only has limited support for polynomial root finding).

.. admonition:: Hint

   In sympy, you will find useful the following functions and methods:
   :func:`together`, :func:`fraction` and :meth:`subs`.

For the same inputs as above, sympy produces this polynomial object::

    In [41]: sym_rpoly(a, b, k)
    Out[41]: Poly(x**4 + 1.9974128540305*x**3 + 0.573052832244009*x**2 -
    0.55703635620915*x - 0.176930147058824, x)


.. only:: instructor

   Solution
   --------

   .. literalinclude:: examples/poly_univar.py

