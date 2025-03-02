import os
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING or "PY4DS_PYTEST" in os.environ:
    from .solution import Salary, read_csv
else:
    from .problem import Salary, read_csv


def test_example_read_csv():
    current_dir = Path(__file__).parent
    test_file = current_dir / "example.csv"

    actual = read_csv(str(test_file))
    expected = [
        Salary("John Smith", "Software Engineer", "Technology", 95000),
        Salary("Emily Johnson", "Marketing Manager", "Advertising", 78500),
    ]

    assert actual == expected


def test_salaries_read_csv():
    rows = read_csv("data/salaries.csv")
    actual = sum(row.salary for row in rows)

    assert actual == 2747500.0
