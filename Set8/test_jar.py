from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(3)
    assert jar.size == 3

    with pytest.raises(ValueError):
        assert jar.deposit(14) == "Too many cookies"


def test_withdraw():
    jar = Jar()
    jar.deposit(8)
    jar.withdraw(5)
    assert jar.size == 3

    with pytest.raises(ValueError):
            assert jar.withdraw(5) == "Not enough cookies"
