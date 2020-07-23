def get_alarm_level(fire_confidence):
    # Todo: Triangulate sequential steps
    # ...
    return 'green'


def test_level_green():
    assert 'green' == get_alarm_level(0)

def test_level_red():
    assert 'red' == get_alarm_level(100)
