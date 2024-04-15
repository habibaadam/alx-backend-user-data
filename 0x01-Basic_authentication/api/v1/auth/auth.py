#!/usr/bin/env python3
"""Setting up basic authentication for the API"""


from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class to manage the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """public method that checks if paths require authentication"""
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """public method that returns None - request will be public"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):  # type: ignore
        """public method that returns None - request will be public"""
        return None
