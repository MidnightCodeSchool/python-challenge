import p00_variable_type


def test_an_int():
    assert isinstance(p00_variable_type.an_int, int)


def test_a_float():
    assert isinstance(p00_variable_type.a_float, float)


def test_a_string():
    assert isinstance(p00_variable_type.a_string, str)


def test_a_bool():
    assert isinstance(p00_variable_type.a_bool, bool)


def test_a_list():
    assert isinstance(p00_variable_type.a_list, list)
    assert len(p00_variable_type.a_list) == 3
    assert isinstance(p00_variable_type.a_list[0], int)
    assert isinstance(p00_variable_type.a_list[1], float)
    assert isinstance(p00_variable_type.a_list[2], str)


def test_a_dict():
    assert isinstance(p00_variable_type.a_dict, dict)
    assert len(p00_variable_type.a_dict) == 3


def test_a_tuple():
    assert isinstance(p00_variable_type.a_tuple, tuple)


def test_a_set():
    assert isinstance(p00_variable_type.a_set, set)


def test_a_none():
    assert p00_variable_type.a_none is None
