from lspy.represent import only_names

def test_only_names(f_infos):
    assert ['a', 'foo'] == only_names(f_infos)
