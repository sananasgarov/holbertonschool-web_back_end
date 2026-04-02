#!/usr/bin/env python3
"""
Encrypt passwords using bcrypt
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
    # Generate a random salt
    salt = bcrypt.gensalt()
    # Hash the password with the salt
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed
