# Read Salaries CSV as List of Salary Dataclasses

- Problem: [problem.py](problem.py) _(create this file)_
- Template: [template.py](template.py) _(copy starter code from here)_
- Tests: [test_all.py](test_all.py) _(tests that verify your solution)_
- Solution: [solution.py](solution.py) _(our solution)_

**_Note: The [problem.py](problem.py) doesn't exist yet! After clicking the link above, click "Create File"._**

In this exercise, you'll work with a CSV file containing salary information and convert it into a list of dataclass instances.

## Problem Statement

In [Problem p7519 - Filter Salaries Greater than 100k](../p7519/index.md), we filtered a list of dictionaries for salaries greater than $100,000. One of the problems with using a list of dictionaries is that we don't know the **_types_** of the columns. This makes it inconvenient to work with the data. We had to convert the salary to a number before we could compare it to 100,000.

One way to make working with our data easier is to use a dataclass. Using a dataclass, we can specify that the type of the salary column is a float. The types for the columns in some data is called a schema.

Your task is to implement a function that:

1. Reads data from a CSV file containing salary information
2. Creates a dataclass called `Salary` to represent each row
3. Returns a list of `Salary` instances

The `Salary` dataclass should have the following fields:

- `name` (string): The employee's name
- `title` (string): The employee's job title
- `industry` (string): The industry in which the employee works
- `salary` (float): The employee's annual salary

For example, if the CSV file contains:

```csv
name,title,industry,salary
John Smith,Software Engineer,Technology,95000
Emily Johnson,Marketing Manager,Advertising,78500
```

Your function should return a list of `Salary` objects equivalent to:

```python
[
  Salary(name="John Smith", title="Software Engineer", industry="Technology", salary=95000.0),
  Salary(name="Emily Johnson", title="Marketing Manager", industry="Advertising", salary=78500.0)
]
```

## Requirements

- Use Python's `dataclasses` module
- Use the `csv` module for reading the file
- Make sure the salary is converted to a float
- Handle any potential errors gracefully

Next up: [Problem p5564 - Vectorize Words in a Sentence](../p5564/index.md)
