"""
helper dictionary methods
"""

import functools

_map = map
_reduce = reduce

def filter(function, dictionary, recursive=True):
    """

    Return those items of the dictionary for which function(item) is true. The
    item is a tuple (key,value). If function is None, return the items with 
    keys that are true.
    """
    result = {}

    for key in dictionary:
        value = dictionary[key]

        if function(key, value):

            if recursive and type(value) == dict:
                value = filter(function, value)

            result[key] = value 

    return result

def map(function, dictionary, recursive=True):
    """

    Apply function to every value of dictionary and return a dictionary of the 
    results. 
    """
    result = {}

    if function == None:
        function = lambda x: x

    for key in dictionary:
        value = dictionary[key]

        if recursive and type(value) == dict:
            value = map(function, value)
        
        (key, value) = function(key, value)

        result[key] = value

    return result


def reduce(function, dictionary, initializer=None, recursive=True):
    """

    Apply function of two arguments cumulatively to the items of dictionary, 
    so as to reduce the dictionary to a single value. For example, 
    reduce(lambda acc, key, value: acc + key, { 1: None, 2: { 3: None }} ) 
    calculates (((1+2)+3)). The left argument, acc, is the accumulated value 
    and the other two arguments are the key and value of the dictionary entry. 
    If the optional initializer is present, it is placed before the items of 
    the dciontary in the calculation, and serves as a default when the 
    dictionary is empty. 
    """
    accum_value = initializer

    if recursive:
        for key in dictionary:
            value = dictionary[key]

            if type(value) == dict:
                accum_value = reduce(function,
                                     value,
                                     accum_value,
                                     recursive=recursive)

            accum_value = function(accum_value, key, value)
    else:
        for key in dictionary:
            value = dictionary[key]
            accum_value = function(accum_value, key, value)

    return accum_value

def min(dictionary, key=None, recursive=True):
    """

    Return the smallest item in a dictionary. The optional key argument 
    specifies a one-argument ordering function like that used for list.sort(). 
    The key argument, if supplied, must be in keyword form 
    (for example, min(dictionary, key=func)).
    """
    minimum = None

    if key == None:
        keyfunc = lambda key, _: key
    else:
        keyfunc = key

    for key in dictionary:
        value = dictionary[key]

        if minimum == None:
            minimum = keyfunc(key, value) 

        if recursive and type(value) == dict:
            sub_minimum = min(value, key=keyfunc, recursive=recursive)
            if sub_minimum != None and sub_minimum < minimum:
                minimum = sub_minimum

        current_min = keyfunc(key, value)
        if current_min < minimum:
            minimum = current_min

    return minimum

def max(dictionary, key=None, recursive=True):
    """

    Return the largest item in a dictionary. The optional key argument specifies 
    a one-argument ordering function like that used for list.sort().  The key 
    argument, if supplied, must be in keyword form (for example, 
    min(dictionary, key=func)).
    """
    maximum = None

    if key == None:
        keyfunc = lambda key, _: key
    else:
        keyfunc = key

    for key in dictionary:
        value = dictionary[key]

        if maximum == None:
            minimum = keyfunc(key, value) 

        if recursive and type(value) == dict:
            sub_maximum = max(value, key=keyfunc, recursive=recursive)
            if sub_maximum != None and sub_maximum > minimum:
                maximum = sub_maximum

        current_max = keyfunc(key, value)
        if current_max > maximum:
            maximum = current_max

    return maximum

def union(*dictionaries):
    """

    union of all entries in all of the dictionaries in the order provided where
    the last value of a given key in the provided dictionaries, will be the 
    value that is in the resulting dictionary. 
    
    Examples:
    --------
    > union({'a': 1}, {'a': 2})
    {'a': 2}

    > union({'a': 1}, {'b': 2})
    {'a': 1, 'b': 2}

    """
    result = {}

    for dictionary in dictionaries:
        result.update(dictionary)

    return result

def intersect(*dictionaries):
    """

    intersection of all entries in all of the dictionaries in the order 
    provided where entries are included in the resulting dictionary if they 
    have the exact same key and value.
    
    Examples:
    --------
    > intersect({'a': 1}, {'a': 2})
    {}

    > intersect({'a': 1, 'b': 2}, {'b': 2})
    {'b': 2}

    """
    result = {}

    first_dictionary = dictionaries[0]

    def reduce_dict(dictionary):
        """
        internal function reduce the logical
        """
        return _reduce(lambda x, y: x & y, dictionary)

    def dict_lookup(key, value, dictionary):
        """
        internal function to verify that the key,value are in the dictionary
        specified
        """
        return dictionary.get(key) == value

    for key in first_dictionary.keys():
        value = first_dictionary[key]

        lookup = functools.partial(dict_lookup, key, value)
        if reduce_dict(_map(lookup, dictionaries)):
            result[key] = first_dictionary[key]

    return result

# taken from 
# http://kiennt.com/blog/2012/06/14/python-object-and-dictionary-convertion.html
# which was adapted from stackoverflow:
# http://stackoverflow.com/questions/1305532/convert-python-dict-to-object/1305663#1305663

# convert a dictionary to a class
class Object(object):
    def __init__(self, adict):
        """Convert a dictionary to a class

        @param :adict Dictionary
        """
        self.__dict__.update(adict)
        for k, v in adict.items():
            if isinstance(v, dict):
                self.__dict__[k] = Object(v)

def to_object(dictionary):
    """
    Convert the provided dictionary into an class so that you can use the class
    point wise notation to reference the keys in the dictionary.

    Examples
    --------

    In [2]: x = dicttools.to_object({'a': 'b'})

    In [3]: x.a
    Out[3]: 'b'

    In [5]: x.a
    Out[5]: 'b'

    In [6]: y = dicttools.to_object({'a': {'b': True}})

    In [7]: y.a.b
    Out[7]: True

    @param :dictionary a python dictionary
    """
    return Object(dictionary)

