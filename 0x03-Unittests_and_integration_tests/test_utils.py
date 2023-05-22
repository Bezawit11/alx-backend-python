#!/usr/bin/env python3
"""unittest"""


import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch
access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json


class TestAccessNestedMap(unittest.TestCase):
    """"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, n, path, expected):
        self.assertEqual(access_nested_map(n, path), expected)
    
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(self, n, path):
        with self.assertRaises(KeyError) as context:
            access_nested_map(n, path)

class TestGetJson(unittest.TestCase):
    """"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    @patch('utils.requests')
    def test_get_json(self, url):
        with patch('utils.requests') as mock_requests:
            mock_requests.get.assert_called_once()
