#!/usr/bin/env python3
"""
    Replace fields in a message with a redaction string.
"""

import re
import logging
from typing import List


def filter_datum(fields, redaction, message, separator):
    return re.sub('|'.join(f"{field}=.*?{separator}" for field in fields),
                  f"{redaction}{separator}", message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    FORMAT_FIELDS = ('name', 'levelname', 'asctime', 'message')
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """formats a LogRecord.
        """
        original = super().format(record)
        return filter_datum(self.fields, self.REDACTION,
                            original, self.SEPARATOR)


PII_FIELDS = ('name', 'email', 'phone_number', 'ssn', 'password')


def get_logger() -> logging.Logger:
    """Returns a logging.Logger object."""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger
