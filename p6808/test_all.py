import os
from typing import TYPE_CHECKING

if TYPE_CHECKING or "PY4DS_PYTEST" in os.environ:
    from .solution import Vector
else:
    from .problem import Vector


def test_vector_creation():
    """Test that vectors can be created with proper attributes."""
    v = Vector(5, 10)
    assert v.x == 5
    assert v.y == 10


def test_vector_addition():
    """Test vector addition."""
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    result = v1 + v2
    assert isinstance(result, Vector)
    assert result.x == 4
    assert result.y == 6


def test_vector_subtraction():
    """Test vector subtraction."""
    v1 = Vector(5, 7)
    v2 = Vector(2, 3)
    result = v1 - v2
    assert isinstance(result, Vector)
    assert result.x == 3
    assert result.y == 4


def test_vector_equality():
    """Test vector equality comparison."""
    v1 = Vector(3, 4)
    v2 = Vector(3, 4)
    v3 = Vector(5, 6)
    assert v1 == v2
    assert v1 != v3


def test_zero_vector():
    """Test with zero vectors."""
    zero = Vector(0, 0)
    v = Vector(5, -3)
    assert v + zero == v
    assert v - zero == v
    assert zero + zero == zero


def test_negative_coordinates():
    """Test vectors with negative coordinates."""
    v1 = Vector(-1, -2)
    v2 = Vector(3, -5)
    result = v1 + v2
    assert result.x == 2
    assert result.y == -7
