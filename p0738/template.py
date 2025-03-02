from dataclasses import dataclass
from typing import List


@dataclass
class Salary: ...


def read_csv(filename: str) -> List[Salary]: ...
