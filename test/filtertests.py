"""
verify that the filter() method behaves as expected
"""

import dicttools
import time
import unittest

class FilterTests(unittest.TestCase):

    def test_filter_odd_keys(self):
        """
        simple test to filter keys that are odd from the elements in the 
        specified dictionary
        """
        dictionary = {
                        0: { 1: {}, 2: {} },
                        1: { 2: {}, 3: {}, 5: {} },
                     }

        expected =  {
                        1: { 3: {}, 5: {} },
                    }
        
        # filter out the odd elements
        actual = dicttools.filter(lambda key, _: key % 2 != 0,dictionary)
        self.assertEquals(expected, actual, msg="%s != %s" % (expected, actual))

    def test_filter_values_with_multiple_keys(self):
        """
        simple test to filter keys that at least 2 underlying elements associated
        with that key
        """
        dictionary = {
                        0: { 1: {}, 2: {} },
                        1: { 3: {}, 5: {} },
                        2: { 5: {} },
                        3: { 7: { 8: {}, 9: {}} },
                     }

        expected =  {
                        0: { },
                        1: { },
                    }
        
        # filter out the values that only have 1 underlying set of values
        actual = dicttools.filter(lambda _, value: len(value) > 1,
                                  dictionary)

        self.assertEquals(expected, actual, msg="%s != %s" % (expected, actual))

