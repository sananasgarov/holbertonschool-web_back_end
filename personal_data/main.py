#!/usr/bin/env python3
"""
Main file to test filtered_logger.py

- Logs a PII message using the RedactingFormatter
- Connects to the secure database and counts users
"""

import logging
from filtered_logger import get_logger, get_db, PII_FIELDS

def test_logger():
    """Test the RedactingFormatter logger"""
    logger = get_logger()
    message = "name=Bob;email=bob@dylan.com;ssn=000-123-0000;password=bobby2019;phone=123456789;"
    logger.info(message)


def test_db():
    """Test the database connection"""
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM users;")
    for row in cursor:
        print("Users count in database:", row[0])
    cursor.close()
    db.close()


if __name__ == "__main__":
    print("Testing logger...")
    test_logger()
    print("\nTesting database connection...")
    test_db()
