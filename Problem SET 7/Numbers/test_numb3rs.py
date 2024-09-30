from numb3rs import validate


def main():
    test_validate_format()
    test_validate_BIG()
    test_validate_SMLL()


def test_validate_BIG():
    assert validate(r"255.255.255.255") == True
    assert validate(r"300.255.255.255") == False
    assert validate(r"1.300.255.255") == False
    assert validate(r"1.1.300.255") == False
    assert validate(r"1.1.1.300") == False
def test_validate_SMLL():
    assert validate(r"1.1.1.1") == True
    assert validate(r"1.-1.1.1") == False
    assert validate(r"1.1.-1.1") == False
    assert validate(r"1.1.1.-1") == False

def test_validate_format():
    assert validate(r"1.2.3.4") == True
    assert validate(r"1.2.3") == False
    assert validate(r"1.2") == False
    assert validate(r"1") == False
