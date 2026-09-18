from plates import is_valid

def test_alnum():
    assert is_valid("aA876") == True
    assert is_valid("Ac44;") == False
    assert is_valid("Ac ui7") == False

def test_startswith():
    assert is_valid("98gd") == False
    assert is_valid("A7") == False
    assert is_valid("AAb") == True
    assert is_valid(" jjie") == False


def test_min():
    assert is_valid("a") == False
    assert is_valid("") == False

def test_max():
    assert is_valid("AA") == True
    assert is_valid("Ad4") == True
    assert is_valid("AAAAAA") == True
    assert is_valid("AA666666") == False

def test_numbers():
    assert is_valid("Abh033") == False
    assert is_valid("AB990") == True
    assert is_valid("Ab999a") == False
