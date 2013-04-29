"""
verify that the filter() method behaves as expected
"""
import unittest

import dicttools

class ReduceTests(unittest.TestCase):

    def test_reduce_sum_keys(self):
        """
        simple test to reduce a dictionary to the sum of its keys
        """
        dictionary = {
                        1: { 2: {}, 3: {} },
                        2: { 4: {}, 6: {} },
                     }

        
        # filter out the odd elements
        actual = dicttools.reduce(lambda acc, key, _: acc + key,
                                  dictionary,
                                  initializer=0)
        self.assertEquals(18, actual, msg="%s != %s" % (actual, 18))

    def test_reduce_calculate_debt(self):
        """
        reduce a dictionary of user transactions to the amount owed by all 
        users
        """
        dictionary = {
                        'user1': {
                            'transactions' : [ -100, 50, 25 ]
                         },
                        'user2': {
                            'transactions' : [ -200, 200, -100 ]
                         },
                     }
        
        def calculate_debt(acc, key, value):
            """
            calculate from the various transactions the current debt of all 
            users
            """
            if key == 'transactions':
                for amount in value:
                    acc += amount 

            return acc
        
        # filter out the odd elements
        actual = dicttools.reduce(calculate_debt, dictionary, initializer=0)
        self.assertEquals(-125, actual, msg="%s != %s" % (actual, -125))

