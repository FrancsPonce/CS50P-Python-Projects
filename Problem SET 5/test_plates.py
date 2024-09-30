from plates import is_valid


def main():
    test_min_max()
    test_two_letters()
    test_wrong_N()
    test_zero()
    test_spcl_characters()

def test_min_max():
    assert is_valid("AA") == True
    assert is_valid('AAAAAA') == True
    assert is_valid('a') == False
    assert is_valid('aaaaaaaaaaaa') == False

def test_two_letters():
    assert is_valid('AA') == True
    assert is_valid('A2') == False
    assert is_valid('3a') == False
    assert is_valid('33') == False

def test_wrong_N():
    assert is_valid('AA3A') == False
    assert is_valid('AAA33A') == False


def test_zero():
    assert is_valid('CS50') == True
    assert is_valid('CS05') == False

def test_spcl_characters():
    assert is_valid('CS.32') == False
    assert is_valid('CS,32') == False
    assert is_valid('CS!32') == False
    assert is_valid('CS 32') == False
