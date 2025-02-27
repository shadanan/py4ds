import csv
import os

if "PY4DS_PYTEST" in os.environ:
    from .solution import filter_salaries
else:
    from .problem import filter_salaries  # type: ignore

with open("data/salaries.csv", "r") as fp:
    salaries = list(csv.DictReader(fp))


def test_filter_salaries():
    actual = filter_salaries(salaries)
    print(actual)
    expected = [
        {
            "name": "Sarah Williams",
            "title": "HR Director",
            "industry": "Human Resources",
            "salary": "110000",
        },
        {
            "name": "David Rodriguez",
            "title": "Product Manager",
            "industry": "Technology",
            "salary": "115000",
        },
        {
            "name": "Amanda Brown",
            "title": "Research Scientist",
            "industry": "Pharmaceuticals",
            "salary": "105000",
        },
        {
            "name": "Olivia Garcia",
            "title": "Legal Counsel",
            "industry": "Legal",
            "salary": "125000",
        },
        {
            "name": "Daniel Kim",
            "title": "Data Scientist",
            "industry": "Technology",
            "salary": "108000",
        },
        {
            "name": "Christopher Evans",
            "title": "Chief Technology Officer",
            "industry": "Technology",
            "salary": "185000",
        },
        {
            "name": "Matthew Clark",
            "title": "Investment Banker",
            "industry": "Finance",
            "salary": "150000",
        },
        {
            "name": "Michelle Bennett",
            "title": "Pharmacy Manager",
            "industry": "Healthcare",
            "salary": "112000",
        },
    ]
    assert actual == expected
