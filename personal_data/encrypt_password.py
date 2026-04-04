#!/usr/bin/env python3
"""
Encrypt password using bcrypt
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt with a generated salt.

    Args:
        password (str): The plain text password to hash.

    Returns:
        bytes: The salted, hashed password.
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates a password against a hashed password.

    Args:
        hashed_password (bytes): The hashed password.
        password (str): The plain text password to check.

    Returns:
        bool: True if the password matches, False otherwise.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
