#!/usr/bin/python3
"""
method that determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    return True if the data is a valid UTF-8 encoding else return false
    """
    try:
        bytes(data).decode('utf-8', "strict")
        return True
    except UnicodeDecodeError:
        return False


