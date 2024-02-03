#!/usr/bin/python3
"""
method that determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    return True if the data is a valid UTF-8 encoding else return false
    """
    try:
        for byte in data:
            # Ensure that only the 8 least significant bits are considered
            byte = byte & 0xFF
            byte_data = bytes([byte])
            byte_data.decode('utf-8', "strict")
        return True
    except UnicodeDecodeError:
        return False
