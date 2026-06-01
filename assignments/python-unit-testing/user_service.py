"""
user_service.py - A service module that fetches user data from an external API.
This module is designed to be tested with mocks to avoid making real API calls.
"""


class UserService:
    """Service for managing user data from an external API."""

    def __init__(self, api_client):
        """Initialize with an API client."""
        self.api_client = api_client

    def get_user(self, user_id):
        """Fetch a user by ID from the API."""
        try:
            response = self.api_client.fetch_user(user_id)
            if response.get('success'):
                return response.get('user')
            else:
                raise ValueError(f"API error: {response.get('error')}")
        except Exception as e:
            raise Exception(f"Failed to fetch user {user_id}: {str(e)}")

    def update_user(self, user_id, data):
        """Update a user's data via the API."""
        try:
            response = self.api_client.update_user(user_id, data)
            if response.get('success'):
                return response.get('user')
            else:
                raise ValueError(f"API error: {response.get('error')}")
        except Exception as e:
            raise Exception(f"Failed to update user {user_id}: {str(e)}")
