import numpy as np
ra = np.random
la = np.linalg

def GOE(N):
    """Creates an NxN element of the Gaussian Orthogonal Ensemble"""
    m = ra.standard_normal((N,N))
    m += m.T
    return m

def sorted_real_eigvals(mat):
    return np.sort(la.eigvals(mat)).real

def eigvals_from_dim(N):
    mat = GOE(N)
    return sorted_real_eigvals(mat)

def center_eigval_diff(mat):
    """Compute the eigvals of mat and then find the center eigval difference."""
    N = len(mat)
    evals = np.sort(la.eigvals(mat))
    diff = evals[N/2] - evals[N/2-1]
    return diff.real

def ensemble_diffs(num, N):
    """Return an array of num eigenvalue differences for the NxN GOE
    ensemble."""
    diffs = np.empty(num)
    for i in xrange(num):
        mat = GOE(N)
        diffs[i] = center_eigval_diff(mat)
    return diffs

def normalize_diffs(diffs):
    """Normalize an array of eigenvalue diffs."""
    return diffs/diffs.mean()

def normalized_ensemble_diffs(num, N):
    """Return an array of num normalized eigenvalue differences for the NxN
    GOE ensemble."""
    diffs = ensemble_diffs(num, N)
    return normalize_diffs(diffs)

def wigner_dist(s):
    """Returns (s, rho(s)) for the Wigner GOE distribution."""
    return (np.pi*s/2.0) * np.exp(-np.pi*s**2/4.)


def generate_wigner_data():
    s = np.linspace(0.0,4.0,400)
    rhos = wigner_dist(s)
    return s, rhos
    

# def serialDiffs(num, N):
#     diffs = ensembleDiffs(num, N)
#     normalizedDiffs = normalizeDiffs(diffs)
#     return normalizedDiffs
# 
# 
# def parallelDiffs(rc, num, N):
#     nengines = len(rc.get_ids())
#     num_per_engine = num/nengines
#     print "Running with", num_per_engine, "per engine."
#     rc.push(dict(num_per_engine=num_per_engine, N=N))
#     rc.execute('diffs = ensembleDiffs(num_per_engine, N)')
#   # gather blocks always for now
#     pr = rc.gather('diffs')
#     return pr.r
# 
# 
# # Main code
# if __name__ == '__main__':
#     rc = client.MultiEngineClient()
#     print "Distributing code to engines..."
#     r = rc.run('rmtkernel.py')
#     rc.block = False
# 
#     # Simulation parameters
#     nmats = 100
#     matsize = 30
#     
#     %timeit -n1 -r1 serialDiffs(nmats,matsize)
#     %timeit -n1 -r1 parallelDiffs(rc, nmats, matsize)
# 
#     # Uncomment these to plot the histogram
#     # import pylab
#     # pylab.hist(parallelDiffs(rc,matsize,matsize))
