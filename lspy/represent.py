""" :mod:`lspy.represent` --- convnert ``Inform`` to represent strings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
import stat

__all__ = 'only_names', 'long_repr', 'find_represent',


def find_represent(long_=False):
    funcs = []
    if long_:
        funcs.append(long_repr)
    else:
        funcs.append(only_names)
    return funcs


def only_names(informs):
    """Returns name of files or directories

    :param list informs: a list of :attr:`lspy.dig.Inform` .
    :return: a list contains name of files or directories
    :rtype: list
    """
    return [info.name for info in informs]


def long_repr(informs):
    """Return long informat of files or directories

    :param list informs: a list of :attr:`lspy.dig.Inform` .
    :return: a list contains long information of files or directories
    :rtype: list
    """
    result = []
    for info in informs:
        represent = '{permission} {uname} {gname} {size} {time} {name}'.format(
            permission=stat.filemode(info.mode),
            uname=info.owner['uname'],
            gname=info.owner['gname'],
            size=info.size,
            time='{d.month} {d.day} {d:%H}:{d:%M}'.format(d=info.created_at),
            name=info.name
        )
        result.append(represent)
    return result
