from numb3rs import validate

def test_numeri_giusti():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("512.1.1.1") == False

def test_zero_iniziali():
    assert validate("192.168.001.1") == False

def test_troppe_cifre():
    assert validate("1.2.3.1000") == False

def test_non_numeri():
    assert validate("cat") == False
    assert validate("cat.dog.2.4") == False

def test_no_punti():
    assert validate("12344") == False
    assert validate("876.23.21") == False
    assert validate("222.2") == False



