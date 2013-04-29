"""
verify that the filter() method behaves as expected
"""
import unittest

import dicttools

class MinTests(unittest.TestCase):

    def test_min_keys(self):
        """
        verify that you can find the minimum value burried deep in the 
        dictionary.
        """
        dictionary = {
                        1: { 2: {}, 3: {} },
                        2: { 4: {}, -1: {} },
                     }

        
        # filter out the odd elements
        actual = dicttools.min(dictionary)
        self.assertEquals(-1, actual, msg="%s != %s" % (actual, -1))

    def test_min_non_recursive_keys(self):
        """
        verify that you can find the minimum value without recursion at the 
        top level.
        """
        dictionary = {
                        1: { 2: {}, 3: {} },
                        2: { 4: {}, 6: {} },
                     }

        
        # filter out the odd elements
        actual = dicttools.min(dictionary, recursive=False)
        self.assertEquals(1, actual, msg="%s != %s" % (actual, 1))

