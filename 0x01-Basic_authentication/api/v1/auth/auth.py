#!/usr/bin/env python3
"""Setting up basic authentication for the API"""


from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class to manage the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """public method that checks if paths require authentication"""
        if not path or not excluded_paths:
            return True

        # Normalize path to ensure consistent trailing slash
        normalized_path = path.rstrip('/') + '/'

        # Check if the path matches any of the excluded paths
        for excluded_path in excluded_paths:
            # Normalize excluded path to ensure consistent trailing slash
            normalized_excluded_path = excluded_path.rstrip('/') + '/'
            if normalized_excluded_path.endswith('*'):
                if normalized_path.startswith(normalized_excluded_path[:-1]):
                    return False
            elif normalized_path == normalized_excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """public method that validates requests"""
        if request is None or request.headers.get('Authorization') is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):  # type: ignore
        """public method that returns None - request will be public"""
        return None
