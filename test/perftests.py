"""
verify that the filter() method behaves as expected
"""

import dicttools
import itertools
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

    def test_intersect_performance(self):
        total = 20000
        items1 = [ (x, float(x)) for x in range(0, total) ]
        items2 = [ (x, float(x)) for x in range(0, total) ]
        
        dict1 = dict(items1)
        dict2 = dict(items1)

        start = time.time()
        dicttools.intersect(dict1, dict2)
        dictionary_elapsed = time.time() - start

        start = time.time()
        [ filter(lambda element: element in items2, items1) ] 
        list_elapsed = time.time() - start
        print('\n dict intersect is %2.2fx slower than list intersect' % \
                                             (dictionary_elapsed/list_elapsed))

    def test_union_performance(self):
        total = 20000
        items1 = [ (x, float(x)) for x in range(0, total) ]
        items2 = [ (x, float(x)) for x in range(0, total) ]
        
        dict1 = dict(items1)
        dict2 = dict(items1)

        start = time.time()
        dicttools.union(dict1, dict2)
        dictionary_elapsed = time.time() - start

        start = time.time()
        set(itertools.chain(items1, items2))
        list_elapsed = time.time() - start
        print('\n dict union is %2.2fx slower than list union' % \
                                             (dictionary_elapsed/list_elapsed))


