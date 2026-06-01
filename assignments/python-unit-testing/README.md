# 📘 Assignment: Python Unit Testing & Test-Driven Development

## 🎯 Objective

Master the fundamentals of unit testing with pytest, including writing test cases, using fixtures and mocks, and measuring code coverage. By the end of this assignment, you'll be able to write comprehensive tests for Python modules and apply test-driven development principles to ensure code reliability.

## 📝 Tasks

### 🛠️ Task 1: Write Basic Unit Tests with pytest

#### Description
You're given a `calculator.py` module with basic mathematical functions. Write a suite of unit tests for each function using pytest, covering both normal cases and edge cases.

#### Requirements
Completed program should:

- Create a `test_calculator.py` file that imports the calculator functions
- Write at least 3 test cases per function (happy path, edge case, error case)
- Use pytest assertions (`assert`, `==`, `!=`, etc.)
- Test functions: `add()`, `subtract()`, `multiply()`, `divide()`
- Ensure division by zero raises an appropriate exception

### 🛠️ Task 2: Use Fixtures and Parametrize Tests

#### Description
Refactor your test suite to use pytest fixtures for setup/teardown logic and parametrized tests to reduce code duplication. This teaches you how to write clean, maintainable test code.

#### Requirements
Completed program should:

- Create a fixture that provides sample data (e.g., test numbers or objects)
- Use `@pytest.mark.parametrize` to test multiple inputs in a single test function
- Demonstrate at least one use case of parametrized tests (e.g., testing multiple division operations)
- Remove redundant test setup code by using fixtures instead

### 🛠️ Task 3: Mock External Dependencies & Measure Coverage

#### Description
You're given a `user_service.py` module that calls an external API. Write tests for this module using mocks to avoid making real API calls, then run coverage analysis to identify untested code paths.

#### Requirements
Completed program should:

- Use `unittest.mock.patch()` or `pytest-mock` to mock the API call
- Write tests that verify the service correctly processes API responses
- Run pytest with the `--cov` flag to generate a coverage report
- Achieve at least 85% code coverage for the service module
- Document which code paths are tested and why certain paths were excluded (if any)
