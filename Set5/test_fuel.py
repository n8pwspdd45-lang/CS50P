import pytest
from fuel import convert
from fuel import gauge

def test_convert():
    assert convert("1/4") == 25
    assert convert("1/3") == 33
    assert convert("4/8") == 50

def test_ValueError():
    for i in ["4/3", "-3/4", "3/-4", "1.5/4", "-3/-4"]:
        with pytest.raises(ValueError):
            convert(i)

def test_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
    with pytest.raises(ZeroDivisionError):
        convert("0/0")

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(25) == "25%"
    assert gauge(33) == "33%"

