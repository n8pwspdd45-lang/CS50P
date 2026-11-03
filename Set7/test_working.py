import pytest
from working import convert

def test_valid_hours():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("11 AM to 17 PM")

def test_format():
    with pytest.raises(ValueError):
        convert("9 to 5")
    with pytest.raises(ValueError):
        convert("9 - 5")
    with pytest.raises(ValueError):
        convert("17:00 to 19")
    with pytest.raises(ValueError):
        convert("9 AM to 17")

def test_valid_mins():
    with pytest.raises(ValueError):
        convert("9:60 AM to 10:99 PM")
