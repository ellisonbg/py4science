#!/usr/bin/env python
"""Word frequencies - count word frequencies in a string."""

def word_freq(text):
    """Return a dictionary of word frequencies for the given text."""

    freqs = {}
    for word in text.split():
        freqs[word] = freqs.get(word, 0) + 1        
    return freqs

def print_vk(lst):
    """Print a list of value/key pairs nicely formatted in key/value order."""

    # Find the longest key: remember, the list has value/key paris, so the key
    # is element [1], not [0]
    #longest_key = max(map(lambda x: len(x[1]),lst))
    longest_key = max([len(word) for count, word in lst])
    # Make a format string out of it
    fmt = '%'+str(longest_key)+'s -> %s'
    # Do actual printing
    for v,k in lst:
        print fmt % (k,v)

def freq_summ(freqs,n=10):
    """Print a simple summary of a word frequencies dictionary.

    Inputs:
      - freqs: a dictionary of word frequencies.

    Optional inputs:
      - n: the number of """

    words,counts = freqs.keys(),freqs.values()
    # Sort by count
    items = zip(counts,words)
    items.sort()

    print 'Number of words:',len(freqs)
    print
    print '%d least frequent words:' % n
    print_vk(items[:n])
    print
    print '%d most frequent words:' % n
    print_vk(items[-n:])

if __name__ == '__main__':
    import gzip
    text = gzip.open('HISTORY.gz').read()
    freqs = word_freq(text)
    freq_summ(freqs,20)
