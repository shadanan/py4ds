# Convert a List of Dictionaries to a Dictionary of Lists

- Problem: [problem.py](problem.py) _(create this file)_
- Template: [template.py](template.py) _(copy starter code from here)_
- Tests: [test_all.py](test_all.py) _(tests that verify your solution)_
- Solution: [solution.py](solution.py) _(our solution)_

**_Note: The [problem.py](problem.py) doesn't exist yet! After clicking the link above, click "Create File"._**

## Summary

In this problem, you'll learn how to transform data structures by converting a list of dictionaries into a dictionary of lists. This is a common data manipulation task in data science and programming that helps reorganize data for easier analysis or processing.

## Problem Description

Write a function called `pivot` that takes a list of dictionaries as input and returns a dictionary of lists. Each key in the output dictionary should correspond to a key that appears in at least one of the input dictionaries. The value for each key should be a list containing the values for that key from each input dictionary, in the same order as the input dictionaries. Assume that every dictionary will contain the same keys.

## Examples

### Example 1:

```python
input_data = [
  {"name": "Alice", "age": 25, "city": "New York"},
  {"name": "Bob", "age": 30, "city": "Chicago"},
  {"name": "Charlie", "age": 35, "city": "Los Angeles"}
]

output = pivot(input_data)
# Output should be:
# {
#     "name": ["Alice", "Bob", "Charlie"],
#     "age": [25, 30, 35],
#     "city": ["New York", "Chicago", "Los Angeles"]
# }
```

### Example 2:

```python
input_data = [
    {"product": "Laptop", "price": 1200, "in_stock": True},
    {"product": "Phone", "price": 800, "in_stock": False},
    {"product": "Tablet", "price": 500, "in_stock": True}
]

output = pivot(input_data)
# Output should be:
# {
#     "product": ["Laptop", "Phone", "Tablet"],
#     "price": [1200, 800, 500],
#     "in_stock": [True, False, True]
# }
```
