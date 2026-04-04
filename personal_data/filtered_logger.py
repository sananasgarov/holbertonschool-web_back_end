#!/usr/bin/env python3
"""
Database connector
"""

import os
import mysql.connector
from mysql.connector.connection_cext import CMySQLConnection


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
