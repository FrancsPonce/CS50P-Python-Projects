from seasons import check_format

def main():
    test_check_format()

def test_check_format():
    assert check_format("1998-07-03") == ("1998", "07", "03")
    assert check_format("1998-7-3") == None
    assert check_format("May of 2998") == None
