# Convert a Dictionary of Lists to a List of Dictionaries

- Problem: [problem.py](problem.py) _(create this file)_
- Template: [template.py](template.py) _(copy starter code from here)_
- Tests: [test_all.py](test_all.py) _(tests that verify your solution)_
- Solution: [solution.py](solution.py) _(our solution)_

**_Note: The [problem.py](problem.py) doesn't exist yet! After clicking the link above, click "Create File"._**

## Summary

In this exercise, you'll learn how to transform data from a dictionary of lists to a list of dictionaries. This is a common data manipulation task when working with APIs, CSV files, or preparing data for JSON serialization. You'll practice:

- Working with dictionaries and lists
- Transforming data structures
- Using list comprehensions or loops
- Understanding data orientation (column-based vs row-based formats)

## Problem Description

Write a function called `pivot` that takes a dictionary where each key maps to a list of values, and converts it to a list of dictionaries. Each dictionary in the output list should represent one "row" of data, where keys from the input dictionary become keys in each output dictionary.

All the lists in the input dictionary will have the same length. Each item at index `i` across all the lists in the input dictionary corresponds to a single "row" of data.

## Examples

### Example 1:

```python
input_dict = {
  'name': ['Alice', 'Bob', 'Charlie'],
  'age': [25, 30, 35],
  'city': ['New York', 'Boston', 'Chicago']
}

result = pivot(input_dict)
# Output:
# [
#     {'name': 'Alice', 'age': 25, 'city': 'New York'},
#     {'name': 'Bob', 'age': 30, 'city': 'Boston'},
#     {'name': 'Charlie', 'age': 35, 'city': 'Chicago'}
# ]
```

### Example 2:

```python
input_dict = {
  'product': ['Laptop', 'Phone', 'Tablet', 'Monitor'],
  'price': [1200, 800, 500, 300],
  'stock': [5, 20, 10, 8],
  'rating': [4.5, 4.2, 3.8, 4.0]
}

result = pivot(input_dict)
# Output:
# [
#     {'product': 'Laptop', 'price': 1200, 'stock': 5, 'rating': 4.5},
#     {'product': 'Phone', 'price': 800, 'stock': 20, 'rating': 4.2},
#     {'product': 'Tablet', 'price': 500, 'stock': 10, 'rating': 3.8},
#     {'product': 'Monitor', 'price': 300, 'stock': 8, 'rating': 4.0}
# ]
```

Complete the `pivot` function in the `problem.py` file to solve this problem.

Next up: [Problem p5564 - Vectorize Words in a Sentence](../p5564/index.md)
