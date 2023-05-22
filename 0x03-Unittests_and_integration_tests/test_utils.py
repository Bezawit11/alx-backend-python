#!/usr/bin/env python3
"""unittest"""


import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch
access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json
memoize = __import__('utils').memoize


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
    """test get json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    def test_get_json(self, url, load):
        d = {'return_value.json.return_value': load}
        patcher = patch('requests.get', **d)
        mock_read = patcher.start()
        self.assertEqual(get_json(url), load)
        mock_read.assert_called_once()
        patcher.stop()

class TestMemoize(unittest.TestCase):
    """test memoize"""
    def test_memoize(self):
        """test memoize"""
        class TestClass:
            """"test class"""
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
    
        with patch.object(TestClass, 'a_method') as m:
            t_class = TestClass()
            t_class.a_property()
            t_class.a_property()
            m.assert_called_once()
            self.assertEqual(a_property(), 42)
