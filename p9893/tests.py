import os

if "PY4DS_PYTEST" in os.environ:
    from .solution import sum_of_two_values
else:
    from .problem import sum_of_two_values


def test_1_plus_1_is_2():
    assert sum_of_two_values(1, 1) == 2


def test_adding_negative_numbers():
    assert sum_of_two_values(-2, -3) == -5
