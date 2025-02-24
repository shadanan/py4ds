def load_data(filename: str) -> list[int]:
    with open(filename, "r") as fp:
        return [int(line) for line in fp.read().splitlines()]
