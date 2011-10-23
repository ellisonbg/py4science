import matplotlib.pyplot as plt
from matplotlib import mlab

import numpy as np
import os
outdir = 'stockdata'

if 1:
    rall = np.load(os.path.join(outdir, 'stocks_combined.npy')).view(np.recarray)

if 1:
    fig = plt.figure()
    plt.plot(rall.price, rall.dreturn, 'o')

    fig = plt.figure()
    plt.hist(rall.price, 20)


data = []
ranges = [(0, 1), (1, 2), (2, 5), (5, 10), (10, 20), (20, 100), (100, np.inf)]
for price_min, price_max in ranges:
    mask = (rall.price > price_min) & (rall.price <= price_max)
    rmask = rall[mask]
    prices = rmask.price
    dreturn = rmask.dreturn * 100
    median = np.median(dreturn)
    mean = np.mean(dreturn)
    count =  len(dreturn)
    std = np.std(dreturn)
    rar = mean / std

    data.append((price_min, price_max, count, mean, median, std, rar))

rsummary = np.rec.fromrecords(data, names='price_min,price_max,count,mean,median,std,rar')

print mlab.rec2txt(rsummary)
plt.show()
