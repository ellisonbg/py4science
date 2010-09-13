"""max_speedup.py: A script to plat the max speedup of Amdahl's law."""

from pylab import *

def max_speedup(P):
    return 1.0/(1.0-P)


Pvals = arange(0.0,1.0,0.01)
Smax = max_speedup(Pvals)

plot(Pvals, Smax)
title("Max Speedup versus Parallel Fraction")
xlabel("Parallel Fraction $P$")
ylabel("Max Speedup $S_{max}$")
yticks(arange(0.0,100.0,10.0))
xticks(arange(0.0,1.0,0.1))
grid(True)
show()