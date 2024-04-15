#!/usr/bin/env python3
"""Setting up basic authentication for the API"""


from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class to manage the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """public method that returns False - path will be public"""
        return False

    def authorization_header(self, request=None) -> str:
        """public method that returns None - request will be public"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):  # type: ignore
        """public method that returns None - request will be public"""
        return None
