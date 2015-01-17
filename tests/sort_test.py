from collections import namedtuple
from datetime import datetime, timedelta

from pytest import fixture, mark

from lspy.sort import find_sort
from lspy.dig import Inform
from lspy.cli import apply_funcs

def test_sort_by_name():
    informs = []
    for x in range(9, 0, -1):
        inform = Inform(
            name='file{}'.format(x),
            mode=0o100777,
            permission=0o777,
            owner={
                'uid': 0,
                'gid': 0,
                'uname': 'foo',
                'gname': 'bar'
            },
            size=0,
            is_dir=False,
            changed_at=datetime.now(),
            modified_at=datetime.now(),
            accessed_at=datetime.now(),
        )
        informs.append(inform)
    sort_func = find_sort()
    sorted_informs = sort_func[0](informs)
    for x in range(1, 10):
        assert 'file{}'.format(x) == sorted_informs[x - 1].name


def test_sort_reverse():
    T = namedtuple('T', ['name'])
    test_datas = [T(name=x) for x in range(1, 10)]
    print(test_datas)
    d = apply_funcs(find_sort(reverse=True), test_datas)
    for result, expected in zip(d, range(9, 0, -1)):
        assert expected == result.name


@fixture
def f_sort_inform():
    one = timedelta(days=1)
    two = timedelta(days=2)
    accessed = Inform(
        name='accessed',
        mode=0o100777,
        permission=0o777,
        owner={
            'uid': 0,
            'gid': 0,
            'uname': 'foo',
            'gname': 'bar'
        },
        size=0,
        is_dir=False,
        changed_at=datetime.now(),
        modified_at=datetime.now() - one,
        accessed_at=datetime.now() - two,
    )
    changed = Inform(
        name='changed',
        mode=0o100777,
        permission=0o777,
        owner={
            'uid': 0,
            'gid': 0,
            'uname': 'foo',
            'gname': 'bar'
        },
        size=0,
        is_dir=False,
        changed_at=datetime.now() - two,
        modified_at=datetime.now(),
        accessed_at=datetime.now() - one,
    )
    modified = Inform(
        name='modified',
        mode=0o100777,
        permission=0o777,
        owner={
            'uid': 0,
            'gid': 0,
            'uname': 'foo',
            'gname': 'bar'
        },
        size=0,
        is_dir=False,
        changed_at=datetime.now() - one,
        modified_at=datetime.now() - two,
        accessed_at=datetime.now(),
    )
    return [accessed, changed, modified]


@mark.parametrize('k, result', [
    ('changed', ['changed', 'modified', 'accessed']),
    ('time_', ['modified', 'accessed', 'changed']),
    ('accessed', ['accessed', 'changed', 'modified'])
])
def test_sort_by_times(f_sort_inform, k, result):
    key = {}
    key[k] = True
    d = apply_funcs(find_sort(**key), f_sort_inform)
    for result, expected in zip(d, result):
        assert expected == result.name


@mark.parametrize('k, result', [
    ('changed', ['accessed', 'changed', 'modified']),
    ('accessed', ['accessed', 'changed', 'modified'])
])
def test_sort_by_force_name(f_sort_inform, k, result):
    """With --long: show ctime and  sort  by  name
    """
    key = {'long_': True}
    key[k] = True
    d = apply_funcs(find_sort(**key), f_sort_inform)
    for result, expected in zip(d, result):
        assert expected == result.name


@mark.parametrize('k, result', [
    ('changed', ['changed', 'modified', 'accessed']),
    ('accessed', ['accessed', 'changed', 'modified'])
])
def test_sort_with_lt(f_sort_inform, k, result):
    """With --long --time: sort by, and show, ctime
    """
    key = {'time_': True, 'long_': True}
    key[k] = True
    d = apply_funcs(find_sort(**key), f_sort_inform)
    for result, expected in zip(d, result):
        assert expected == result.name
