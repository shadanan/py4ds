# Read CSV as List of Dictionaries

- Problem: [problem.py](problem.py)
- Tests: [tests.py](tests.py)
- Solution: [solution.py](solution.py)

In pandas, you can read a CSV file using `pd.read_csv` and it will return a pandas DataFrame. Without pandas, we don't have DataFrames, but it is possible to represent tables using native Python types. One way to do this is with a list of dictionaries. In this exercise, we will read a CSV file as a list of dictionaries.

Consider a csv that looks like this:

```csv
name,phone_number
Alice Smith,555-0123
Bob Jones,555-4567
Carol Wu,555-8901
```

This data can be represented as a list of dictionaries, like this:

```python
[
  {"name": "Alice Smith", "phone_number": "555-0123"},
  {"name": "Bob Jones", "phone_number": "555-4567"},
  {"name": "Carol Wu", "phone_number": "555-8901"}
]
```

Write a function called `read_csv` that takes the CSV filename as input and returns the data as a list of dictionaries.

> **_Hint: You can use the `csv` library!_**

There's some test data that you can use in [data/salaries.csv](../data/salaries.csv). Try passing that file to your read_csv function!

Next up: [Problem p7519 - Filter Salaries Greater than 100k](../p7519/index.md)
