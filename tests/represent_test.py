from lspy.represent import only_names, long_repr

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
