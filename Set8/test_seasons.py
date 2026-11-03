from seasons import get_minutes
import pytest

def test_one_year():
    assert get_minutes("2025-10-26") == "Five hundred twenty-five thousand, six hundred minutes"

def test_two_years():
    assert get_minutes("2024-10-26") == "One million, fifty-one thousand, two hundred minutes"

def test_invalid_date():
    with pytest.raises(ValueError):
        get_minutes("January 1, 1999") == "Invalid date"
    with pytest.raises(ValueError):
        get_minutes("26/10/2024") == "Invalid date"
    with pytest.raises(ValueError):
        get_minutes("2024-26-10") == "Invalid date"

