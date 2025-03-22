import os
from typing import TYPE_CHECKING

if TYPE_CHECKING or "PY4DS_PYTEST" in os.environ:
    from .solution import pivot
else:
    from .problem import pivot


def test_empty_data():
    assert pivot([]) == {}


def test_single_entry():
    data = [{"name": "John", "age": 30}]
    expected = {"name": ["John"], "age": [30]}
    assert pivot(data) == expected


def test_multiple_entries():
    data = [
        {"name": "John", "age": 30},
        {"name": "Jane", "age": 25},
        {"name": "Bob", "age": 40},
    ]
    expected = {"name": ["John", "Jane", "Bob"], "age": [30, 25, 40]}
    assert pivot(data) == expected


def test_various_data_types():
    data = [
        {"name": "John", "employed": True, "score": 85.5},
        {"name": "Jane", "employed": False, "score": 92.3},
    ]
    expected = {
        "name": ["John", "Jane"],
        "employed": [True, False],
        "score": [85.5, 92.3],
    }
    assert pivot(data) == expected
