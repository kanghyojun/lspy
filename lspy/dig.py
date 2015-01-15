""" :mod:`lspy.dig` --- dig file to get information.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from collections import namedtuple
from datetime import datetime
from pathlib import Path

import os
import stat

__all__ = 'get_fileinfo', 'Inform',

#: `namedtuple` that contains information of file or directory
Inform = namedtuple('namedtuple', ['permission', 'owner', 'size',
                                   'is_dir', 'modified_at', 'accesed_at',
                                   'created_at'])

def get_fileinfo(filename):
    """Return information ( permission, owner, ... ) of file or directory.

    :param str filename: a filename or directory that want to know.
    :return: information of file.
    :rtype: dict
    """
    path = Path(filename)
    if not path.exists():
        raise FileNotFoundError('No such file or directory: {}'.format(filename))
    status = os.stat(filename)
    return Inform(
        permission='',
        owner='',
        size=status.st_size,
        is_dir=stat.S_ISDIR(status.st_mode),
        created_at=datetime.fromtimestamp(status.st_ctime),
        modified_at=datetime.fromtimestamp(status.st_mtime),
        accesed_at=datetime.fromtimestamp(status.st_mtime),
    )
