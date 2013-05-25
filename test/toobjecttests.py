"""
verify that the filter() method behaves as expected
"""

import dicttools
import unittest

class ToObjectTests(unittest.TestCase):

    def test_simple_to_object_usage(self):
        dict1 = {
                 'name': 'alice',
                 'age': 23,
                 'eyes': 'brown',
                 'hair': 'black',
                 'location': { 'lat': -82.86275 , 'lon': -135.00000 }
                }
                  
        obj = dicttools.to_object(dict1)
        self.assertEquals(obj.name, 'alice')
        self.assertEquals(obj.age, 23)
        self.assertEquals(obj.location.lat,  -82.86275)
        self.assertEquals(obj.location.lon, -135.00000)
