#!/usr/bin/env python3
"""Setting up basic authentication for the API"""


from api.v1.auth.auth import Auth
from flask import request
import base64
from typing import TypeVar
from models.user import User


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

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """extracts and returns the user credentials"""
        if decoded_base64_authorization_header is None or \
            type(decoded_base64_authorization_header) is not str or \
                ':' not in decoded_base64_authorization_header:
            return (None, None)
        return tuple(decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """returns user instance based on email and password"""
        if user_email is None or user_pwd is None:
            return None
        if type(user_email) is not str or type(user_pwd) is not str:
            return None
        users = User.search({'email': user_email})
        if not users:
            return None

        for user in users:
            if not user.is_valid_password(user_pwd):
                return None
            return user
