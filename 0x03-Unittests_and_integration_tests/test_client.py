#!/usr/bin/env python3
"""unit test"""


import unittest
from unittest.mock import patch
from client import GithubOrgClient
get_json = __import__('utils').get_json
from parameterized import parameterized, parameterized_class


class TestGithubOrgClient(unittest.TestCase):
    """"test github client"""
    @parameterized.expand([
        ('google'),
        ('abc')
        ])
    @patch('get_json')
    def test_org(self, url, mock_org):
        """test org"""
        mock_org.return_value = {}
        g = GithubOrgClient(url)
        self.assertEqual(g.org(), {})
        
        
