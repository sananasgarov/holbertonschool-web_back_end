#!/usr/bin/env python3
"""
Filtered logger with PII masking and secure MySQL connection
"""

import logging
import os
import re
from typing import List, Tuple
import mysql.connector
from mysql.connector.connection_cext import CMySQLConnection


PII_FIELDS: Tuple[str, ...] = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """Return the log message with sensitive fields redacted."""
    for field in fields:
        message = re.sub(
            f"{field}=.*?{separator}", f"{field}={redaction}{separator}", message
        )
    return message


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION: str = "***"
    FORMAT: str = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR: str = ";"

    def __init__(self, fields: List[str]):
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format the log record, redacting sensitive information."""
        message = super().format(record)
        return filter_datum(self.fields, self.REDACTION, message, self.SEPARATOR)


def get_logger() -> logging.Logger:
    """Return a logger configured with RedactingFormatter."""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    if not logger.handlers:
        stream_handler = logging.StreamHandler()
        formatter = RedactingFormatter(fields=list(PII_FIELDS))
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

    return logger


def get_db() -> CMySQLConnection:
    """Return a MySQL database connection using environment variables."""
    user = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    database = os.getenv("PERSONAL_DATA_DB_NAME")
    return mysql.connector.connect(
        user=user,
        password=password,
        host=host,
        database=database,
    )


def main() -> None:
    """Fetch all rows from users table and log them with PII redacted."""
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
