import os
from typing import TYPE_CHECKING

if TYPE_CHECKING or "PY4DS_PYTEST" in os.environ:
    from .solution import pivot
else:
    from .problem import pivot


def test_empty_dict():
    assert pivot({}) == []


def test_single_key():
    assert pivot({"a": [1, 2, 3]}) == [{"a": 1}, {"a": 2}, {"a": 3}]


def test_multiple_keys():
    input_dict = {
        "name": ["Alice", "Bob", "Charlie"],
        "age": [25, 30, 35],
        "city": ["New York", "Boston", "Chicago"],
    }
    expected = [
        {"name": "Alice", "age": 25, "city": "New York"},
        {"name": "Bob", "age": 30, "city": "Boston"},
        {"name": "Charlie", "age": 35, "city": "Chicago"},
    ]
    assert pivot(input_dict) == expected


def test_different_types():
    input_dict = {
        "str": ["a", "b"],
        "int": [1, 2],
        "bool": [True, False],
        "float": [1.1, 2.2],
    }
    expected = [
        {"str": "a", "int": 1, "bool": True, "float": 1.1},
        {"str": "b", "int": 2, "bool": False, "float": 2.2},
    ]
    assert pivot(input_dict) == expected


def test_single_row():
    input_dict = {"a": [1], "b": [2], "c": [3]}
    expected = [{"a": 1, "b": 2, "c": 3}]
    assert pivot(input_dict) == expected


def test_empty_lists():
    assert pivot({"a": [], "b": []}) == []
