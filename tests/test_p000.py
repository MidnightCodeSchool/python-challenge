def test_file_exists():
    global p000_variable_type
    try:
        import p000_variable_type
    except ModuleNotFoundError as e:
        fname = str(e).split(" ")[-1]
        raise FileNotFoundError(
            f"{fname} not found. Are you naming the file correctly?"
        )


def test_an_int():
    assert isinstance(p000_variable_type.an_int, int)


def test_a_float():
    assert isinstance(p000_variable_type.a_float, float)


def test_a_string():
    assert isinstance(p000_variable_type.a_string, str)


def test_a_bool():
    assert isinstance(p000_variable_type.a_bool, bool)


def test_a_list():
    assert isinstance(p000_variable_type.a_list, list)
    assert len(p000_variable_type.a_list) == 3
    assert isinstance(p000_variable_type.a_list[0], int)
    assert isinstance(p000_variable_type.a_list[1], float)
    assert isinstance(p000_variable_type.a_list[2], str)


def test_a_dict():
    assert isinstance(p000_variable_type.a_dict, dict)
    assert len(p000_variable_type.a_dict) == 3


def test_a_tuple():
    assert isinstance(p000_variable_type.a_tuple, tuple)


def test_a_set():
    assert isinstance(p000_variable_type.a_set, set)


def test_a_none():
    assert p000_variable_type.a_none is None
