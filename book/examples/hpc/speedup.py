"""speedup.py: A Script to plot the speedup from Amdahls law."""

from pylab import *

def speedup(P, N):
    return 1.0/((1-P) + P/N)

Nvals = [2**n for n in range(2,13)]
Pvals = [0.5, 0.75, 0.9, 0.95]

for P in Pvals:
    Svals = [speedup(P,N) for N in Nvals]
    semilogx(Nvals, Svals, basex=2, label="P=%s" % P)

title("Speedup versus number of cores")
xlabel("Number of cores $N$")
ylabel("Speedup $S$")
yticks(arange(0.0,20.0,2.0))
grid(True)
legend()

show()