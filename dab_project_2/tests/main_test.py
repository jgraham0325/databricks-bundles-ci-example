from main import get_taxis, get_spark
import pytest


@pytest.mark.skip(reason="This test is currently disabled because Databricks workspace is blocking the IP of the build agent")
def test_get_taxis():
    taxis = get_taxis(get_spark())
    assert taxis.count() > 5
