from twttr import shorten

def test_uppercase():
    assert shorten("LUCE") == "LC"
    assert shorten("TWITTER") == "TWTTR"

def test_lowercase():
     assert shorten("mamma") == "mmm"

def test_mix():
     assert shorten("") == ""
     assert shorten("Mamma") == "Mmm"

def test_number():
     assert shorten("1234") == "1234"
     assert shorten("H3llo") == "H3ll"

def test_punctuation():
     assert shorten("Hello, World!") == "Hll, Wrld!"
     assert shorten("Bye bye, Marie...") == "By by, Mr..."
