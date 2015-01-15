from pathlib import Path

from pytest import fixture

@fixture
def f_777_filename():
    return str(Path('./tests/assets/777_file'))


@fixture
def f_tree_path():
    return str(Path('./tests/assets/tree'))
