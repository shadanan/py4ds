# Model a Vector using Dataclasses

- Problem: [problem.py](problem.py) _(create this file)_
- Template: [template.py](template.py) _(copy starter code from here)_
- Tests: [test_all.py](test_all.py) _(tests that verify your solution)_
- Solution: [solution.py](solution.py) _(our solution)_

**_Note: The [problem.py](problem.py) doesn't exist yet! After clicking the link above, click "Create File"._**

## Summary

This exercise focuses on implementing a 2D Vector class using Python's `dataclass` feature. You'll learn how to create a clean, efficient class with minimal boilerplate code while adding custom functionality through operator overloading. By implementing methods like `__add__`, `__sub__`, and `__eq__`, you'll enable intuitive mathematical operations between vector instances using standard Python operators (`+`, `-`, `==`). This demonstrates how dataclasses can be extended beyond their basic functionality to create powerful, expressive code patterns common in scientific computing and graphics programming.

## Problem Description

Create a 2D Vector class using Python's dataclass functionality. The Vector should:

1. Store x and y coordinates as integers
2. Support vector addition with the `+` operator
3. Support vector subtraction with the `-` operator
4. Support equality comparison with the `==` operator

For example, if you have two vectors `v1 = Vector(1, 2)` and `v2 = Vector(3, 4)`, then:

- `v1 + v2` should return `Vector(4, 6)`
- `v2 - v1` should return `Vector(2, 2)`
- `Vector(1, 2) == Vector(1, 2)` should return `True`

## Example

```python
from dataclasses import dataclass

# Your Vector implementation here

# Example usage:
v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1 + v2)  # Vector(4, 6)
print(v1 - v2)  # Vector(2, 2)
print(v1 == Vector(3, 4))  # True
```

## Requirements

1. Use Python's `dataclass` decorator
2. Implement `__add__`, `__sub__`, and `__eq__` methods
3. Ensure coordinates are stored as integers
4. Make sure all operations return a new Vector instance
