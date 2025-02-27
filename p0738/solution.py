import csv
from dataclasses import dataclass
from typing import List


@dataclass
class Salary:
    name: str
    title: str
    industry: str
    salary: float

    @classmethod
    def parse(cls, record: dict) -> "Salary":
        """Creates a Salary instance from a dictionary record."""
        return cls(
            name=record["name"],
            title=record["title"],
            industry=record["industry"],
            salary=float(record["salary"]),
        )


def read_csv(filename: str) -> List[Salary]:
    """Reads salary data from a CSV file and returns a list of Salary dataclass instances."""
    salaries = []

    with open(filename, "r", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            salary = Salary.parse(row)
            salaries.append(salary)

    return salaries
