#!/usr/bin/env python3
"""Setting up basic authentication for the API"""


from api.v1.auth.auth import Auth
from flask import request


class BasicAuth(Auth):
    """class for authentication set up"""
