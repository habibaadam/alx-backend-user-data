#!/usr/bin/env python3
"""Contains usage of bcrypt to hash passwords"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    returns a salted, hashed password, which is a byte string
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def is_valid(hashed_password: bytes, password: str) -> bool:
    """checks if a provided password matches with a
    hashed password
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
