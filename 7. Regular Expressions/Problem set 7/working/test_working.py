import pytest
from working import convert

def test_happy_hours ():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:00 PM to 5:00 AM") == "21:00 to 05:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 PM to 5 AM") == "21:00 to 05:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_happy_minutes ():
    assert convert("9:01 AM to 5:59 PM") == "09:01 to 17:59"
    assert convert("9:01 PM to 5:59 AM") == "21:01 to 05:59"

def test_format_hours ():
    with pytest.raises(ValueError):
        assert convert("13:00 AM to 5:00 PM")
        assert convert("9:00 AM to 13:00 PM")
        assert convert("13 AM to 5 PM")
        assert convert("9 AM to 13 PM")

def test_format_minutes ():
    with pytest.raises(ValueError):
        assert convert("9:60 AM to 5:00 PM")
        assert convert("9:00 AM to 5:60 PM")
        assert convert("9:60 AM to 5 PM")
        assert convert("9 AM to 5:60 PM")

def test_format_empty ():
    with pytest.raises(ValueError):
        assert convert("9:00  to 5:00 PM")
        assert convert("9:00 AM  5:00 PM")
        assert convert("9:00 AM to 5:00 ")
        assert convert("9  to 5 PM")
        assert convert("9 AM  5 PM")
        assert convert("9 AM to 5")

def test_input_format ():
    with pytest.raises(ValueError):
        assert convert ("cat")
        assert convert ("9:00 AM to cat")