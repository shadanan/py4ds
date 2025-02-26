import csv


def read_csv(filename: str) -> list[dict]:
    with open(filename, "r") as fp:
        reader = csv.DictReader(fp)
        data = list(reader)
    return data
