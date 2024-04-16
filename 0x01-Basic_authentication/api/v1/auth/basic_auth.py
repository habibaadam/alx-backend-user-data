#!/usr/bin/env python3
"""Setting up basic authentication for the API"""


from api.v1.auth.auth import Auth
from flask import request
import base64


class BasicAuth(Auth):
    """class for authentication set up"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """extracts the base64 part
        from the authorization header
        """
        if authorization_header is None or \
                type(authorization_header) is not str:
            return None
        if authorization_header[:6] != 'Basic ':
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """returns the decoded part of a base64 string"""
        if base64_authorization_header is None or \
                type(base64_authorization_header) is not str:
            return None
        try:
            decoded_string = base64.b64decode(
                base64_authorization_header).decode('utf-8')
            return decoded_string
        except Exception:
            return
