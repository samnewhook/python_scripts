#!/usr/bin/python3
import unittest
from updatetodo import get_latest_date, date_time_from_filename


class updatetodo(unittest.TestCase):
    def test_date_time_from_filename(self):
        self.assertEqual(date_time_from_filename(''), None,
                          "Should return None on no string input")

    def test_get_latest_date(self):
        self.assertEqual(get_latest_date([]), None, "Should return None")


if __name__ == "__main__":
    unittest.main()
