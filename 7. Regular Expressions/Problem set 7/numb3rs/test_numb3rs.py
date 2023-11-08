import pytest
from numb3rs import validate

def test_happy_case():
    assert validate("20.20.20.20") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True

def test_bite_validation():
    assert validate(r"255.255.255.255") == True
    assert validate(r"800.1.1.1") == False
    assert validate(r"1.800.1.1") == False
    assert validate(r"1.1.800.1") == False
    assert validate(r"1.1.1.800") == False

def test_string_case():
    assert validate("cat") == False
    assert validate("cat.cat.cat.cat") == False

def test_combo():
    assert validate(",.,.,.,") == False
    assert validate("cat.1.1.1") == False
    assert validate(";.catcatcat") == False
    assert validate("'.'.cat.$%") == False
    assert validate("cat 1.1.1.1 cat") == False