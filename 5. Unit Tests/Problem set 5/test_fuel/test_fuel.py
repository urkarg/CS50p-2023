from fuel import convert
from fuel import gauge
import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        assert convert("1/0")

def test_conversion_value_error():
    with pytest.raises(ValueError):
        assert convert("cat/dog")

def test_fuel_vlaue_error():
    with pytest.raises(ValueError):
        assert convert("7/6")

def test_correct_int():
    assert convert("3/6") == 50

def test_empty():
    for i in [0,1]:
        assert gauge(i) == "E"

def test_full():
    for i in [99,100]:
        assert gauge(i) == "F"

def test_percent():
    assert gauge(50) == "50%"