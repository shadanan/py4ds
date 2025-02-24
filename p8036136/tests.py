import os

if "PY4DS_PYTEST" in os.environ:
    from .solution import load_data
else:
    from .problem import load_data

data1 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data1.dat")


def test_load_data_data1_is_correct_type():
    actual = load_data(data1)
    assert isinstance(actual, list)


def test_load_data_data1_has_correct_sum():
    actual = load_data(data1)
    assert sum(actual) == 1048
