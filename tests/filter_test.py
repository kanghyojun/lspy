from pytest import fixture

from lspy.dig import listing_informs
from lspy.filter import hide_dot

@fixture
def f_filter_infos(f_filter_path):
    return listing_informs(f_filter_path)


def test_hide_dot(f_filter_infos):
    flag = False
    for info in f_filter_infos:
        flag = flag or info.name.startswith('.')
    assert flag
    flag = False
    for info in hide_dot(f_filter_infos):
        flag = flag or info.name.startswith('.')
    assert not flag
