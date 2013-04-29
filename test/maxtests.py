"""
verify that the filter() method behaves as expected
"""
import unittest

import dicttools

class MaxTests(unittest.TestCase):

    def test_max_keys(self):
        """
        verify that you can find the maximum value burried deep in the 
        dictionary.
        """
        dictionary = {
                        1: { 2: {}, 3: {} },
                        2: { 4: {}, 7: {} },
                     }

        
        # filter out the odd elements
        actual = dicttools.max(dictionary)
        self.assertEquals(7, actual, msg="%s != %s" % (actual, 7))

    def test_max_non_recursive_keys(self):
        """
        verify that you can find the maximum value without recursion at the 
        top level.
        """
        dictionary = {
                        1: { 2: {}, 3: {} },
                        3: { 4: {}, 6: {} },
                     }

        
        # filter out the odd elements
        actual = dicttools.max(dictionary, recursive=False)
        self.assertEquals(3, actual, msg="%s != %s" % (actual, 3))

