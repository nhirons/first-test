from lab06 import *

## Extra Questions ##

## Optional List Mutation ##
def deep_map_mut(fn, lst):
    """Deeply maps a function over a Python list, replacing each item
    in the original list object.

    Does NOT create new lists by either using literal notation
    ([1, 2, 3]), +, or slicing.

    Does NOT return the mutated list object.

    >>> l = [1, 2, [3, [4], 5], 6]
    >>> deep_map_mut(lambda x: x * x, l)
    >>> l
    [1, 4, [9, [16], 25], 36]
    """
    "*** YOUR CODE HERE ***"
    for i in range(len(lst)):
        if type(lst[i]) == list:
            deep_map_mut(fn, lst[i])
        else:
            lst[i] = fn(lst[i])

def reverse(lst):
    """Reverses lst using mutation.

    >>> original_list = [5, -1, 29, 0]
    >>> reverse(original_list)
    >>> original_list
    [0, 29, -1, 5]
    >>> odd_list = [42, 72, -8]
    >>> reverse(odd_list)
    >>> odd_list
    [-8, 72, 42]
    """
    "*** YOUR CODE HERE ***"
    # midpoint = len(lst) // 2
    # last = len(lst) - 1
    # for i in range(midpoint):
    #     lst[i], lst[last - i] = lst[last - i], lst[i]
    if len(lst) > 1:
        temp = lst.pop()
        print(temp)
        reverse(lst)
        lst.insert(0, temp)
        print(lst)


## Optional Dictionaries ##

def counter(message):
    """ Returns a dictionary of each word in message mapped
    to the number of times it appears in the input string.

    >>> x = counter('to be or not to be')
    >>> x['to']
    2
    >>> x['be']
    2
    >>> x['not']
    1
    >>> y = counter('run forrest run')
    >>> y['run']
    2
    >>> y['forrest']
    1
    """
    word_list = message.split() # .split() returns a list of the words in the string. Try printing it!
    "*** YOUR CODE HERE ***"
    dict_count = {}
    for word in word_list:
        if word not in dict_count:
            dict_count[word] = 1
        else:
            dict_count[word] += 1
    return dict_count


