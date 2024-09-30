from working import convert
import pytest

def main():
    test_format()
    test_time()
    test_h()
    test_m()

def test_format():
    with pytest.raises(ValueError):
        convert("9 AM - 9 PM")

def test_time():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"

def test_h():
    with pytest.raises(ValueError):
        convert("9 AM - 17 PM")
def test_m():
    with pytest.raises(ValueError):
        convert("9:60 AM - 9:60 PM")
