#!/usr/bin/python3
import unittest
from scripts import get_latest_date, date_time_from_filename

class updatetodo(unittest.TestCase):
    def get_latest_date():
        assert(updatetodo.get_latest_date([]), None, "Should return None")


if __name__ == "__main__":
    unittest.main()
