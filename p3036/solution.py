def pivot(data: dict[str, list]):
    return [dict(zip(data.keys(), values)) for values in zip(*data.values())]
