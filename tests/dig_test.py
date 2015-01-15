from datetime import datetime
from pathlib import Path

import os

import pytest

from lspy.dig import get_fileinfo, Inform, listing_informs

def test_has_key_get_fileinfo(f_777_filename):
    keys = [
        'permission', 'owner', 'size', 'is_dir', 'modified_at', 'accesed_at',
        'created_at', 'mode', 'name'
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
    assert '777_file' == info.name
    assert isinstance(info, Inform)
    assert status.st_mode == info.mode
    assert 0o777 == info.permission
    assert 0 == info.size
    assert not info.is_dir
    assert atime == info.accesed_at
    assert mtime == info.modified_at
    assert ctime == info.created_at


def test_listing_informs(f_tree_path):
    list_infos = listing_informs(f_tree_path)
    root = Path(f_tree_path)
    expected_info = [
        get_fileinfo(str(root / 'a')),
        get_fileinfo(str(root / 'foo'))
    ]
    assert 2 == len(list_infos)
    for expected, result in zip(expected_info, list_infos):
        assert expected.name == result.name
        assert expected.permission == result.permission
        assert expected.owner == result.owner
        assert expected.is_dir == result.is_dir
        assert expected.modified_at == result.modified_at
        assert expected.accesed_at == result.accesed_at
        assert expected.created_at == result.created_at
