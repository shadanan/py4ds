def filter_salaries(salaries: list[dict]) -> list[dict]:
    return [row for row in salaries if int(row["salary"]) > 100000]
