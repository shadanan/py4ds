# Summary Statistics of a Column in List of Dictionaries

- Problem: [problem.py](problem.py) _(create this file)_
- Template: [template.py](template.py) _(copy starter code from here)_
- Tests: [test_all.py](test_all.py) _(tests that verify your solution)_
- Solution: [solution.py](solution.py) _(our solution)_

**_Note: The [problem.py](problem.py) doesn't exist yet! After clicking the link above, click "Create File"._**

Given a list of dictionaries and a column name, implement a function that calculates summary statistics for the specified column.

## Problem Description

In this problem, we'll implement a function similar to the `describe()` method in pandas. When working with DataFrame objects in pandas, the `describe()` method provides summary statistics for numeric columns, including count, mean, standard deviation, min, max, and percentiles. Our function will implement a simplified version of this functionality, but for a list of dictionaries instead of a DataFrame.

This type of statistical summary is a fundamental operation in data analysis, allowing you to quickly understand the distribution and central tendencies of your data. While pandas provides this functionality out of the box for DataFrame objects, implementing it manually helps understand the underlying calculations and provides a solution for when you're working with simple dictionary-based data structures.

Write a function `calculate_statistics(data, column)` that returns a dictionary containing the following statistics:

- `count`: The number of non-None values in the column
- `min`: The minimum value in the column
- `max`: The maximum value in the column
- `sum`: The sum of all values in the column
- `mean`: The mean (average) of all values in the column
- `median`: The median value in the column

### Examples:

```python
# Example with sample salary data
data = [
  {'name': 'John Smith', 'title': 'Software Engineer', 'industry': 'Technology', 'salary': 95000},
  {'name': 'Emily Johnson', 'title': 'Marketing Manager', 'industry': 'Advertising', 'salary': 78500},
  {'name': 'Michael Chen', 'title': 'Financial Analyst', 'industry': 'Finance', 'salary': 82000}
]

calculate_statistics(data, 'salary')
# Returns: {'count': 3, 'min': 78500, 'max': 95000, 'sum': 255500, 'mean': 85166.67, 'median': 82000}

calculate_statistics(data, 'industry')
# Returns: {} (because 'industry' contains non-numeric values)
```

### Another example:

```python
data = [
  {'name': 'Alice', 'age': 25, 'score': 85.0},
  {'name': 'Bob', 'age': 30, 'score': 92.5},
  {'name': 'Charlie', 'age': 22, 'score': 78.3}
]

calculate_statistics(data, 'age')
# Returns: {'count': 3, 'min': 22, 'max': 30, 'sum': 77, 'mean': 25.67, 'median': 25}

calculate_statistics(data, 'score')
# Returns: {'count': 3, 'min': 78.3, 'max': 92.5, 'sum': 255.8, 'mean': 85.27, 'median': 85.0}
```
