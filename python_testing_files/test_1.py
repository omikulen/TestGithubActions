from pytest import raises


def    add(a, b):
    return  a   +b


def test_add(mocker  ):
    assert add(1, 2
               ) == 3
    assert raises(
        TypeError, add, 1, "2")
