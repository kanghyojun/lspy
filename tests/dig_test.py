import pytest

from lspy.dig import get_fileinfo

def test_has_key_get_fileinfo(f_777_filename):
    keys = [
        'permission', 'owner', 'size', 'is_dir', 'modified_at', 'accesed_at',
        'created_at'
    ]
    info = get_fileinfo(f_777_filename)
    for key in keys:
        assert hasattr(info, key)


def test_raise_notfound():
    with pytest.raises(FileNotFoundError):
        info = get_fileinfo('foobaz')
