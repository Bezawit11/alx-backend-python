#!/usr/bin/env python3
"""unittest"""


import unittest
from parameterized import parameterized, parameterized_class
access_nested_map = __import__('utils').access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, n, path, expected):
        self.assertEqual(access_nested_map(n, path), expected)
