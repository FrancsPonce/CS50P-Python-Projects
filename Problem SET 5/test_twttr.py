from twttr import shorten


def main():
    test_twttr_words()
    test_twttr_nmbr()
    test_twttr_punct()



def test_twttr_words():
    assert shorten("francisco") == "frncsc"
    assert shorten("frAncIscO") == "frncsc"
    assert shorten("Francsco") == "Frncsc"

def test_twttr_nmbr():
    assert shorten("0123456789") == "0123456789"

def test_twttr_punct():
    assert shorten(".,'") == ".,'"




