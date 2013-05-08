"""
verify that the filter() method behaves as expected
"""

import dicttools
import unittest

class IntersectTests(unittest.TestCase):

    def test_basic_dictionaries(self):
        dict1 = { 0: 0, 1: 1 }
        dict2 = { 1: 1, 2: 2 }

        actual = dicttools.intersect(dict1, dict2)
        expected = { 1: 1 }
        self.assertEquals(actual, expected, msg="%s != %s" % (expected, actual)) 

    def test_nested_dictionaries(self):
        dict1 = { 0: { 1: False }, 2: {} }
        dict2 = { 0: { 1: False }, 3: True }

        actual = dicttools.intersect(dict1, dict2)
        expected = { 0: { 1: False} }
        self.assertEquals(actual, expected, msg="%s != %s" % (expected, actual)) 

