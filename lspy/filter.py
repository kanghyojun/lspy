""" :mod:`lspy.filter` --- filter of informs list
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
__all__ = 'hide_dot', 'find_filters',

def find_filters(all_=False):
    """Find appropriate filters.

    :param boolean all_: ``--all`` option
    :return: a list contains filter function
    :rtype: list
    """
    funcs = []
    if not all_:
        funcs.append(hide_dot)
    return funcs


def hide_dot(informs):
    """Hide file or directories starts with ``.`` .

    :param list informs: a list of :attr:`lspy.dig.Inform` .
    :return: a list contains name of files or directories
    :rtype: list
    """
    return [info for info in informs if not info.name.startswith('.')]
