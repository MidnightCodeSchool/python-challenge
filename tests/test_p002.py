import pytest


def test_file_exists():
    global p002_function
    try:
        import p002_function
    except ModuleNotFoundError as e:
        fname = str(e).split(" ")[-1]
        raise FileNotFoundError(
            f"{fname} not found. Are you naming the file correctly?"
        )


def test_add():
    assert p002_function.add(1, 2) == 3
    assert p002_function.add(-1, 1) == 0
    assert p002_function.add(0, 0) == 0


def test_subtract():
    assert p002_function.subtract(5, 3) == 2
    assert p002_function.subtract(-1, 1) == -2
    assert p002_function.subtract(0, 0) == 0


def test_multiply():
    assert p002_function.multiply(2, 3) == 6
    assert p002_function.multiply(-1, 1) == -1
    assert p002_function.multiply(0, 100) == 0


def test_divide():
    assert p002_function.divide(6, 3) == 2
    assert p002_function.divide(-6, 3) == -2
    assert p002_function.divide(5, 2) == 2.5
    with pytest.raises(ValueError):
        p002_function.divide(1, 0)


def test_power():
    assert p002_function.power(2, 3) == 8
    assert p002_function.power(3, 2) == 9
    assert p002_function.power(2, 0) == 1
    assert p002_function.power(0, 2) == 0
