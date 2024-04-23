#!/usr/bin/env python3
"""module contains hashing method"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """hashes a password"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
