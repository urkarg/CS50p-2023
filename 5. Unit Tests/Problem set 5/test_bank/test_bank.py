from bank import value


def test_lowercase():
    assert value("hello") == 0

def test_uppercase():
    assert value("HELLO") == 0

def test_starts_with_h():
    assert value("Help me") == 20

def test_doesnt_start_with_h():
    assert value("don't help me") == 100

def test_strips_spaces():
    assert value("what's up     ") == 100

def test_ignores_alphanum():
    assert value("h100200,,..:'") == 20