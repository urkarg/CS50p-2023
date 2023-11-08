from plates import is_valid


def test_number_start():
    assert is_valid("123233") == False

def test_len_larger():
    assert is_valid("AAADDDS") == False

def test_len_smaller():
    assert is_valid("D") == False

def test_more_numbers():
    assert is_valid("AA22A2") == False

def test_is_alphanum():
    assert is_valid("AA,AA") == False

def test_first_nr_not_zero():
    assert is_valid("AAD019") == False