#!/usr/bin/env python3
"""
Contains a script that returns a log message obfuscated
"""


import logging
import re
from typing import List
import mysql.connector
from os import environ


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Returns a log message obfuscated
    """
    for f in fields:
        message = re.sub(f'{f}=.*?{separator}',
                         f'{f}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """
        Filter values in incoming log records using filter_datum
        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def get_logger() -> logging.Logger:
    """
    Returns a logging object
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream = logging.StreamHandler()
    stream.setLevel(logging.INFO)
    stream.setFormatter(RedactingFormatter(fields=PII_FIELDS))
    logger.addHandler(stream)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Returns a connector to a database
    """
    username = environ.get('PERSONAL_DATA_DB_USERNAME', 'root')
    password = environ.get('PERSONAL_DATA_DB_PASSWORD', '')
    db_name = environ.get('PERSONAL_DATA_DB_NAME')
    host = environ.get('PERSONAL_DATA_DB_HOST')

    conn = mysql.connector.connection.MySQLConnection(user=username,
                                                      password=password,
                                                      host=host,
                                                      database=db_name)
    return conn
