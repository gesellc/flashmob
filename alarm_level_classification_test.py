def get_alarm_level(fire_confidence):
    # Todo: Triangulate sequential steps
    # ...
    if fire_confidence == 0:
        return 'green'
    else:
        return 'red'


def test_level_green():
    assert 'green' == get_alarm_level(0)

def test_level_red():
    assert 'red' == get_alarm_level(100)
    assert 'red' == get_alarm_level( 69)

def test_level_yellow():
    assert '' == get_alarm_level(68)