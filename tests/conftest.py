from pathlib import Path

from pytest import fixture

from lspy.dig import listing_informs

@fixture
def f_777_filename():
    return str(Path('./tests/assets/777_file'))


@fixture
def f_tree_path():
    return str(Path('./tests/assets/tree'))


@fixture
def f_infos(f_tree_path):
    return listing_informs(f_tree_path)
