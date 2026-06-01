"""
conftest.py - Pytest configuration file with shared fixtures.
Define reusable fixtures here that will be available to all test files.
"""

import pytest


@pytest.fixture
def sample_numbers():
    """Provides sample numbers for testing."""
    return {
        "a": 10,
        "b": 5,
        "zero": 0,
        "negative_a": -10,
        "negative_b": -5,
    }


@pytest.fixture
def mock_api_client(mocker):
    """Provides a mock API client for testing services."""
    client = mocker.MagicMock()
    return client
