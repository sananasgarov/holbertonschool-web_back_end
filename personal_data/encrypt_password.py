#!/usr/bin/env python3
"""
Encrypt passwords using bcrypt and validate them
"""

import bcrypt

def hash_password(password: str) -> bytes:
    """
    Hash a password with a randomly-generated salt.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The salted, hashed password.
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validate a password against a hashed password.

    Args:
        hashed_password (bytes): The previously hashed password.
        password (str): The password to verify.

    Returns:
        bool: True if password matches the hash, False otherwise.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
