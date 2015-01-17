""" :mod:`lspy.sort` --- sorting informs list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
__all__ = 'find_sort',

def find_sort():
    """Find sort functions.

    :return: a list contains lambda has sort function.
    :rtype: list
    """
    key = 'name'
    funcs = []
    key_func = lambda inform: getattr(inform, key)
    return [lambda informs: sorted(informs, key=key_func)]
