"""
test_calculator.py - Starter template for testing the calculator module.
Complete the tests according to the assignment requirements.
"""

import pytest
from calculator import add, subtract, multiply, divide


# TODO: Task 1 - Write basic unit tests
# Write test functions for add(), subtract(), multiply(), and divide()
# Each function should have at least 3 tests (happy path, edge case, error case)

# Example structure:
# def test_add_positive_numbers():
#     assert add(2, 3) == 5

# def test_add_negative_numbers():
#     assert add(-2, -3) == -5

# def test_divide_by_zero():
#     with pytest.raises(ValueError):
#         divide(10, 0)


# TODO: Task 2 - Use fixtures and parametrize
# Create a fixture for sample data
# Use @pytest.mark.parametrize to test multiple inputs

# Example structure:
# @pytest.fixture
# def sample_numbers():
#     return {"a": 10, "b": 5}

# @pytest.mark.parametrize("a,b,expected", [
#     (10, 5, 15),
#     (0, 0, 0),
#     (-10, 10, 0),
# ])
# def test_add_parametrized(a, b, expected):
#     assert add(a, b) == expected
