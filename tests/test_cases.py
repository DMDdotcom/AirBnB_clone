#!/usr/bin/python3

import unittest
import datetime
from unittest.mock import patch
import sys
from io import StringIO
import re
import os

class Tests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(2 + 2, 4)

if __name__ == "__main__":
    unittest.main()
