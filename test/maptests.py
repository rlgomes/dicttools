"""
verify that the filter() method behaves as expected
"""

import dicttools
import unittest

class MapTests(unittest.TestCase):

    def test_map_add_one_to_keys(self):
        dictionary = {
                        0: { 1: {}, 2: {} },
                        1: { 2: {}, 3: {}, 5: {} },
                     }
        expected = {
                       1: { 2: {}, 3: {} },
                       2: { 3: {}, 4: {}, 6: {} },
                    }

        actual = dicttools.map(lambda x, y: (x + 1, y), dictionary)
        self.assertEquals(expected, actual, msg="%s != %s" % (expected, actual))

    def test_map_replace_empty_dict_with_None(self):
        dictionary = {
                        0: { 1: {}, 2: {} },
                        1: { 2: {}, 3: {}, 5: {} },
                     }
        expected = {
                       0: { 1: None, 2: None },
                       1: { 2: None, 3: None, 5: None },
                    }

        def replace_empty_dict(key, value):
            if value == {}:
                return (key, None)
            else:
                return (key, value)

        actual = dicttools.map(replace_empty_dict, dictionary)
        self.assertEquals(expected, actual, msg="%s != %s" % (expected, actual))

    def test_map_create_new_nodes(self):
        dictionary = {
                        0: { 1: {}, 2: {} },
                        1: { 2: {}, 3: {}, 5: {} },
                     }
        expected = {
                       0: { 1: { 0: {}}, 2: { 0: {}} },
                       1: { 2: { 0: {}}, 3: { 0: {}}, 5: { 0: {}} },
                    }

        def replace_empty_dict(key, value):
            if value == {}:
                return (key, { 0: {}})
            else:
                return (key, value)

        actual = dicttools.map(replace_empty_dict, dictionary)
        self.assertEquals(expected, actual, msg="%s != %s" % (expected, actual))

