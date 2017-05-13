#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as error_msg:
        sys.stderr.write("Exception: {}\n".format(error_msg))
        return False
    return True
