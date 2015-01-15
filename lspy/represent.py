""" :mod:`lspy.represent` --- convnert ``Inform`` to represent strings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
__all__ = 'only_names',


def only_names(informs):
    """Returns name of files or directorys

    :param list informs: a list of :attr:`lspy.dig.Inform` .
    :return: a list contains name of files or directorys
    :rtype: list
    """
    return [info.name for info in informs]
