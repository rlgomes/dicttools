"""
helper dictionary methods
"""

def filter(function, dictionary, recursive=True):
    """

    Return those items of the dictionary for which function(item) is true. The
    item is a tuple (key,value). If function is None, return the items with 
    keys that are true.
    """
    result = {}

    for (key, value) in dictionary.items():
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

    for (key, value) in dictionary.items():

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

    for (key, value) in dictionary.items():

        if recursive and type(value) == dict:
            accum_value = reduce(function,
                                 value,
                                 initializer=accum_value,
                                 recursive=recursive)

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

    for (key, value) in dictionary.items():

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

    for (key, value) in dictionary.items():

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


