import numpy as np
import matplotlib.mlab as mlab
import os
outdir = 'stockdata'
#ticker = 'CROX'

tickers = 'CROX,AAPL,INTC,GOOG,DRYS,LULU,CMG,MCD,PLM,XOM,VZ,BZ,JAMN,UTOG'.split(',')

recs = []
for ticker in tickers:
    outfile = os.path.join(outdir, '%s.csv'%ticker)

    r = mlab.csv2rec(outfile)
    r.sort(order='date')

    print 'parsing ticker=%s, numrows=%d' % (ticker, len(r))

    prices = r.close[:-1]
    returns = (r.adj_close[1:] - r.adj_close[:-1]) / r.adj_close[:-1]
    rdata = np.rec.fromarrays([r.date[:-1], prices, returns], names='date,price,dreturn')
    recs.append(rdata)

rall = np.concatenate(recs)
print 'concantenated all; numrows=%d'%len(rall)

mlab.rec2csv(rall, os.path.join(outdir, 'stocks_combined.csv'))

np.save(os.path.join(outdir, 'stocks_combined.npy'), rall)
