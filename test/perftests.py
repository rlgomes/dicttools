"""
verify that the filter() method behaves as expected
"""

import dicttools
import time
import unittest

class PerfTests(unittest.TestCase):

    def test_filter_performance(self):
        total = 1000000
        items = [ (x, float(x)) for x in range(0, total) ]
        dictionary = dict(items)

        start = time.time()
        dicttools.filter(lambda x, y: x < total/2, dictionary)
        dictionary_elapsed = time.time() - start

        start = time.time()
        filter(lambda (x, y): x < total/2, items)
        list_elapsed = time.time() - start

        print('\n dict filter is %2.2fx slower than list filter' % \
                                             (dictionary_elapsed/list_elapsed))

        start = time.time()
        dicttools.filter(lambda x, y: x < total/2, dictionary, recursive=False)
        dictionary_elapsed = time.time() - start
        print(' dict filter(recursive=False) is %2.2fx slower than list filter' % \
                                             (dictionary_elapsed/list_elapsed))

    def test_reduce_performance(self):
        total = 3000000
        items = [ (x, float(x)) for x in range(0, total) ]
        dictionary = dict(items)

        start = time.time()
        dicttools.reduce(lambda acc, x, y: acc + x, dictionary, initializer=0)
        dictionary_elapsed = time.time() - start

        start = time.time()
        reduce(lambda acc, (x,y): acc + x, items, 0)
        list_elapsed = time.time() - start

        print('\n dict reduce is %2.2fx slower than list reduce' % \
                                             (dictionary_elapsed/list_elapsed))

        start = time.time()
        dicttools.reduce(lambda acc, x, y: acc + x,
                         dictionary,
                         initializer=0,
                         recursive = False)
        dictionary_elapsed = time.time() - start
        print(' dict reduce(recursive=False) is %2.2fx slower than list reduce' % \
                                             (dictionary_elapsed/list_elapsed))

    def test_map_performance(self):
        total = 1000000
        items = [ (x, float(x)) for x in range(0, total) ]
        dictionary = dict(items)

        start = time.time()
        dicttools.map(lambda x, y: (x, y < total/2), dictionary)
        dictionary_elapsed = time.time() - start

        start = time.time()
        map(lambda (x, y): (x, y < total/2), items)
        list_elapsed = time.time() - start

        print('\n dict map is %2.2fx slower than list map' % \
                                             (dictionary_elapsed/list_elapsed))

        start = time.time()
        dicttools.map(lambda x, y: (x, y < total/2),
                      dictionary,
                      recursive=False)
        dictionary_elapsed = time.time() - start
        print(' dict map(recursive=False) is %2.2fx slower than list map' % \
                                             (dictionary_elapsed/list_elapsed))

