import twttr
from twttr import shorten

def test_default():
    assert shorten("Hello") == "Hll"

def test_uppercase():
    assert shorten("HELLO") == "HLL"

def test_lowercase():
    assert shorten("hello") == "hll"

def test_nonalpha():
    assert shorten("12345,./") == "12345,./"