from datetime import datetime

import os

import pytest

from lspy.dig import get_fileinfo

def test_has_key_get_fileinfo(f_777_filename):
    keys = [
        'permission', 'owner', 'size', 'is_dir', 'modified_at', 'accesed_at',
        'created_at', 'mode'
    ]
    info = get_fileinfo(f_777_filename)
    for key in keys:
        assert hasattr(info, key)
    assert 'uid' in info.owner
    assert 'uname' in info.owner
    assert 'gid' in info.owner
    assert 'gname' in info.owner


def test_raise_notfound():
    with pytest.raises(FileNotFoundError):
        info = get_fileinfo('foobaz')


def test_get_fileinfo_right_value(f_777_filename):
    status = os.stat(f_777_filename)
    atime = datetime.fromtimestamp(status.st_atime)
    mtime = datetime.fromtimestamp(status.st_mtime)
    ctime = datetime.fromtimestamp(status.st_ctime)
    info = get_fileinfo(f_777_filename)
    assert status.st_mode == info.mode
    assert 0o777 == info.permission
    assert 0 == info.size
    assert not info.is_dir
    assert atime == info.accesed_at
    assert mtime == info.modified_at
    assert ctime == info.created_at
