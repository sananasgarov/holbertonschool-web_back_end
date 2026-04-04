#!/usr/bin/env python3
"""
Main file to test filtered_logger functionality
"""

from filtered_logger import get_db, get_logger

def main() -> None:
    """Fetch all users from the database and log with PII redacted."""
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users;")
    logger = get_logger()

    for row in cursor:
        message = "; ".join(f"{k}={v}" for k, v in row.items()) + ";"
        logger.info(message)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
