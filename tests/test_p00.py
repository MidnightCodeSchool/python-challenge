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
    assert "one" in p00_variable_type.a_dict
    assert "two" in p00_variable_type.a_dict
    assert "three" in p00_variable_type.a_dict
    assert p00_variable_type.a_dict["one"] == 1
    assert p00_variable_type.a_dict["two"] == 2.0
    assert p00_variable_type.a_dict["three"] == "3"


def test_a_tuple():
    assert isinstance(p00_variable_type.a_tuple, tuple)
    assert len(p00_variable_type.a_tuple) == 3
    assert isinstance(p00_variable_type.a_tuple[0], int)
    assert isinstance(p00_variable_type.a_tuple[1], float)
    assert isinstance(p00_variable_type.a_tuple[2], str)


def test_a_set():
    assert isinstance(p00_variable_type.a_set, set)
    assert len(p00_variable_type.a_set) == 3
    expected_elements = {1, "two", 3.0}
    assert p00_variable_type.a_set == expected_elements


def test_a_none():
    assert p00_variable_type.a_none is None
