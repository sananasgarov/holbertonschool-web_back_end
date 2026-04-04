#!/usr/bin/env python3
"""
Main module for reading and filtering users data from MySQL database
"""

from filtered_logger import get_db, get_logger, PII_FIELDS
import logging


def main() -> None:
    """Fetch all users and log each row with PII fields redacted."""
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users;")
    logger = get_logger()

    for row in cursor:
        # Create message string from row dict
        message = "; ".join(f"{k}={v}" for k, v in row.items()) + ";"
        logger.info(message)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
