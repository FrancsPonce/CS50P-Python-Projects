from bank import value


def main():
    test_corner_W()



def test_corner_W():
    assert value("Hello") == 0
    assert value("Hola") == 20
    assert value("SADASD") == 100

