def test_file_exists():
    global p001_variable_operation
    try:
        import p001_variable_operation
    except ModuleNotFoundError as e:
        fname = str(e).split(" ")[-1]
        raise FileNotFoundError(
            f"{fname} not found. Are you naming the file correctly?"
        )


def test_variables_exist():
    assert hasattr(p001_variable_operation, 'a')
    assert hasattr(p001_variable_operation, 'b')
    assert hasattr(p001_variable_operation, 'c')
    assert isinstance(p001_variable_operation.a, int)
    assert isinstance(p001_variable_operation.b, int)
    assert isinstance(p001_variable_operation.c, int)


def test_sum():
    assert p001_variable_operation.d == (
        p001_variable_operation.a + p001_variable_operation.b)


def test_difference():
    assert p001_variable_operation.e == (
        p001_variable_operation.a - p001_variable_operation.b)


def test_product():
    assert p001_variable_operation.f == (
        p001_variable_operation.a * p001_variable_operation.b)


def test_division():
    assert p001_variable_operation.g == (
        p001_variable_operation.a / p001_variable_operation.b)


def test_remainder():
    assert p001_variable_operation.h == (
        p001_variable_operation.a % p001_variable_operation.b)


def test_power():
    assert p001_variable_operation.i == (
        p001_variable_operation.a ** p001_variable_operation.b)


def test_division_rounded():
    assert p001_variable_operation.j == round(
        p001_variable_operation.a / p001_variable_operation.b)
