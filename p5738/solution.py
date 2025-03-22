def pivot(data: list[dict]):
    if not data:
        return {}

    result = {}

    # Initialize the result dictionary with empty lists for each key
    for key in data[0].keys():
        result[key] = []

    # Populate the lists with values from each dictionary
    for item in data:
        for key, value in item.items():
            result[key].append(value)

    return result
