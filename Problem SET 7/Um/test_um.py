from um import count

def main():
    test_CASE()
    test_um()
    test_space()


def test_CASE():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, um, UM ...") == 3

def test_um():
    assert count("yummi") == 0
    assert count("um?") == 1
def test_space():
    assert count("aaa um aaaaa") == 1
