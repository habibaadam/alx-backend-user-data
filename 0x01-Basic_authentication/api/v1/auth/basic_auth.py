#!/usr/bin/env python3
"""Setting up basic authentication for the API"""


from api.v1.auth.auth import Auth
from flask import request


class BasicAuth(Auth):
    """class for authentication set up"""

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """extracts the base64 part from the authorization header"""
        if authorization_header is None or type(authorization_header) is not str:
            return None
        if authorization_header[:6] != 'Basic ':
            return None
        return authorization_header[6:]

