from um import count

def test_um_start ():
    assert count("um") == 1
    assert count("um yea") == 1
    assert count("um no") == 1

def test_um_middle ():
    assert count("Please, um, now") == 1
    assert count("what um now?") == 1

def test_um_end ():
    assert count("What now, um") == 1

def test_um_punct_marks():
    assert count("um!") == 1
    assert count("um,") == 1
    assert count("um ") == 1
    assert count("um?") == 1

def test_no_um ():
    assert count("u") == 0
    assert count("this has no") == 0

def test_um_inside_word ():
    assert count("yummy") == 0
    assert count("tummy") == 0
    assert count("magnum") == 0

def test_more_um ():
    assert count("um um") == 2
    assert count("um, what now, um?") == 2

def test_case_um ():
    assert count("UM") == 1
    assert count("Um") == 1
    assert count("uM") == 1
    assert count("um") == 1