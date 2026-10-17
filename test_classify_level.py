import pytest
from SmartHomeTesting.classify_level import classify_level

@pytest.mark.parametrize("value,expected",
                         [(35.0,'alert'),
                          (30.0,'warning'),
                          (25.0,'warning'),
                          (20.0,'normal'),
                          (20.1,'warning'),
                          (10.0,'normal'),
                          (0.0,'normal'),
                          (-10.0,'normal'),
                          (1000.0,'alert'),],
                          ids=["above30",
                               "boundary-30-warning",
                               "mid-20-normal",
                               "boundary-20-normal",
                               "boundary-20.1-warning",
                               "mid-10-normal",
                               "zero",
                               "negative",
                               "very-large",])
def test_classify_level(value,expected):
    assert classify_level(value)==expected

def test_classify_level_none():
    with pytest.raises(TypeError):
        classify_level(None)