from pytest import raises


def some_other_function(x):
    if x == 42:
        return True
    if x == 41:
        return False
    if x == 43:
        return None
    raise ValueError("What? Babka ne chue, dev`jat chy desyat?")


# Path: python_testing_files/test3.py
def test_some_other_function(mocker):
    assert some_other_function(42)
    assert not some_other_function(41)
    assert some_other_function(43) is None
    assert raises(ValueError, some_other_function, 44)
