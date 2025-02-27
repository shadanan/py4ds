def calculate_statistics(data: list[dict], column: str):
    """Calculate summary statistics for a specified column in a list of dictionaries."""
    values = [item[column] for item in data]

    # Calculate statistics
    count = len(values)
    min_val = min(values)
    max_val = max(values)
    sum_val = sum(values)
    mean = round(sum_val / count, 2)

    # Calculate median
    sorted_values = sorted(values)
    n = len(sorted_values)
    if n % 2 == 0:
        # Even number of values, average the middle two
        median = (sorted_values[n // 2 - 1] + sorted_values[n // 2]) / 2
    else:
        # Odd number of values, take the middle one
        median = sorted_values[n // 2]

    return {
        "count": count,
        "min": min_val,
        "max": max_val,
        "sum": sum_val,
        "mean": mean,
        "median": median,
    }
