from datetime import timedelta

from pytest import mark

from lspy.dig import Inform
from lspy.represent import only_names, long_repr, find_represent

def test_only_names(f_infos):
    assert ['a', 'foo'] == only_names(f_infos)


def test_long_repr(f_infos):
    expect = [
        'drwxr-xr-x {uname} {gname} 102 1 15 15:38 a',
        '-rw-r--r-- {uname} {gname} 0 1 15 15:19 foo'
    ]
    long_reprs = long_repr(f_infos)
    for i, (represent, info) in enumerate(zip(long_reprs, f_infos)):
        expected = expect[i].format(uname=info.owner['uname'],
                                    gname=info.owner['gname'])
        print(represent)
        assert expected == represent


@mark.parametrize('represent_time', ('changed_at', 'accessed_at'))
def test_with_time_long_repr(f_infos, represent_time):
    two_days_ago = getattr(f_infos[1], represent_time) - timedelta(days=2)
    info = f_infos[1]._replace(changed_at=two_days_ago)
    t = getattr(info, represent_time)
    expected = '-rw-r--r-- {uname} {gname} 0 {time} {name}'.format(
        uname=info.owner['uname'],
        gname=info.owner['gname'],
        time='{d.month} {d.day} {d:%H}:{d:%M}'.format(d=t),
        name=info.name
    )
    kwargs = {'long_': True}
    kwargs[represent_time[:-3]] = True
    result = find_represent(**kwargs)[0]([info])
    assert expected == result[0]
