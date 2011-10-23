import urllib
import os
tickers = 'CROX,AAPL,INTC,GOOG,DRYS,LULU,CMG,MCD,PLM,XOM,VZ,BZ,JAMN,UTOG'.split(',')


outdir = 'stockdata'
if not os.path.exists(outdir):
    os.makedirs(outdir)


#ticker = 'CROX'

for ticker in tickers:
    url_template = 'http://ichart.finance.yahoo.com/table.csv?s=%s&d=9&e=22&f=2011&g=d&a=1&b=8&c=2006&ignore=.csv'
    url = url_template % ticker

    outfile = os.path.join(outdir, '%s.csv'%ticker)
    if os.path.exists(outfile):
        print 'already have %s'%ticker
    else:
        print 'fetching %s'%ticker
        urllib.urlretrieve(url, outfile)
