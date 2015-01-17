""" :mod:`lspy.sort` --- sorting informs list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
__all__ = 'find_sort',

def find_sort(
        long_=False, time_=False, accessed=False, changed=False,
        reverse=False):
    """Find sort functions.

    :param boolean long_:
    :param boolean time_:
    :param boolean accessed:
    :param boolean changed:
    :param boolean reverse:
    :return: a list contains lambda has sort function.
    :rtype: list
    """
    key = 'name'
    if time_ and long_ or not (time_ or long_):
        if accessed:
            key = 'accessed_at'
        elif changed:
            key = 'changed_at'
    if time_ and not accessed and not changed:
        key = 'modified_at'
    key_func = lambda inform: getattr(inform, key)
    funcs = [lambda informs: sorted(informs, key=key_func)]
    if reverse:
        funcs.append(lambda x: x[::-1])
    return funcs
