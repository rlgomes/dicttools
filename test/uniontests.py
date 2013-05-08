"""
verify that the filter() method behaves as expected
"""

import dicttools
import unittest

class UnionTests(unittest.TestCase):

    def test_basic_dictionaries(self):
        dict1 = { 0: 0, 1: 0 }
        dict2 = { 1: 1, 2: 2 }

        actual = dicttools.union(dict1, dict2)
        expected = { 0: 0, 1: 1, 2: 2 }
        self.assertEquals(actual, expected, msg="%s != %s" % (expected, actual)) 

    def test_nested_dictionaries(self):
        dict1 = { 0: { 1: False } }
        dict2 = { 0: { 1: True } }

        actual = dicttools.union(dict1, dict2)
        expected = { 0: { 1: True} }
        self.assertEquals(actual, expected, msg="%s != %s" % (expected, actual)) 

