""" :mod:`lspy.represent` --- convnert ``Inform`` to represent strings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
import stat

__all__ = 'only_names', 'long_repr', 'find_represent', 'size_represent',


def find_represent(long_=False, changed=False, accessed=False, human=False):
    funcs = []
    if long_:
        if changed:
            setattr(long_repr, 'represent_time', 'changed_at')
        elif accessed:
            setattr(long_repr, 'represent_time', 'accessed_at')
        if human:
            setattr(long_repr, 'human_readable', True)
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
    rt = getattr(long_repr, 'represent_time', 'modified_at')
    human_readable = getattr(long_repr, 'human_readable', False)
    result = []
    for info in informs:
        represent = '{permission} {uname} {gname} {size} {time} {name}'.format(
            permission=stat.filemode(info.mode),
            uname=info.owner['uname'],
            gname=info.owner['gname'],
            size=size_represent(info.size, human_readable),
            time='{d.month} {d.day} {d:%H}:{d:%M}'.format(d=getattr(info, rt)),
            name=info.name
        )
        result.append(represent)
    return result


def size_represent(size, human_readable):
    """Find human readable bytes.

    .. sourcecode::python

       assert 512 == size_represent(512, False)
       assert '512.0B' == size_represent(512, True)
       assert '1.0K' == size_represent(1024, True)
       assert '1.0M' == size_represent(1024 ** 2, True)
       assert '1.0G' == size_represent(1024 ** 3, True)
       assert '1.0P' == size_represent(1024 ** 4, True)
       assert '1024.0P' == size_represent(1024 ** 5, True)
    """
    if not human_readable:
        return size
    block = 1024
    postfixs = ['B', 'K', 'M', 'G', 'P']
    for i, postfix in enumerate(postfixs):
        if size < block ** (i + 1):
            div = block ** i
            return '{0:.1f}{1}'.format(size / div, postfix)
    return '{0:.1f}{1}'.format(size / (block ** (len(postfixs) - 1)),
                               postfixs[-1])
