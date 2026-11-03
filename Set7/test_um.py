from um import count

def test_case_insensitivity():
    assert count("um") == 1
    assert count("UM") == 1
    assert count("Um") == 1

def test_counts():
    assert count("um?") == 1
    assert count("Um, thanks, um...") == 2

def test_um_not_in_words():
    assert count("um, thanks for the album.") == 1
    assert count("yummy") == 0
