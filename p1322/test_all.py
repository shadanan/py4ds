import os

if "PY4DS_PYTEST" in os.environ:
    from .solution import calculate_statistics
else:
    from .problem import calculate_statistics  # type: ignore

SALARY_DATA = [
    {
        "name": "John Smith",
        "title": "Software Engineer",
        "industry": "Technology",
        "salary": 95000,
    },
    {
        "name": "Emily Johnson",
        "title": "Marketing Manager",
        "industry": "Advertising",
        "salary": 78500,
    },
    {
        "name": "Michael Chen",
        "title": "Financial Analyst",
        "industry": "Finance",
        "salary": 82000,
    },
]


def test_calculate_statistics_salary_count():
    result = calculate_statistics(SALARY_DATA, "salary")
    assert result["count"] == 3


def test_calculate_statistics_salary_min_max():
    result = calculate_statistics(SALARY_DATA, "salary")
    assert result["min"] == 78500
    assert result["max"] == 95000


def test_calculate_statistics_salary_sum():
    result = calculate_statistics(SALARY_DATA, "salary")
    assert result["sum"] == 255500


def test_calculate_statistics_salary_mean_median():
    result = calculate_statistics(SALARY_DATA, "salary")
    assert result["mean"] == 85166.67
    assert result["median"] == 82000


def test_calculate_statistics_age_score():
    data = [
        {"name": "Alice", "age": 25, "score": 85.0},
        {"name": "Bob", "age": 30, "score": 92.5},
        {"name": "Charlie", "age": 22, "score": 78.3},
    ]

    # Test age statistics
    age_result = calculate_statistics(data, "age")
    assert age_result["count"] == 3
    assert age_result["min"] == 22
    assert age_result["max"] == 30
    assert age_result["sum"] == 77
    assert age_result["mean"] == 25.67
    assert age_result["median"] == 25

    # Test score statistics
    score_result = calculate_statistics(data, "score")
    assert score_result["count"] == 3
    assert score_result["min"] == 78.3
    assert score_result["max"] == 92.5
    assert score_result["sum"] == 255.8
    assert score_result["mean"] == 85.27
    assert score_result["median"] == 85.0


def test_even_count_median():
    data = [{"a": 1}, {"a": 2}, {"a": 3}, {"a": 4}]
    result = calculate_statistics(data, "a")
    assert result["median"] == 2.5


def test_odd_count_median():
    data = [{"a": 1}, {"a": 3}, {"a": 5}]
    result = calculate_statistics(data, "a")
    assert result["median"] == 3
