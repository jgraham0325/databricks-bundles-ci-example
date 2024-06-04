from main import get_taxis, get_spark


def test_get_taxis():
    taxis = get_taxis(get_spark())
    assert taxis.count() > 5
