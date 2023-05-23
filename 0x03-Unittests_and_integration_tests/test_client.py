#!/usr/bin/env python3
"""unit test"""


import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class


class TestGithubOrgClient(unittest.TestCase):
    """"test github client"""
    @parameterized.expand([
        ('google'),
        ('abc')
        ])
    @patch('org')
    def test_org(self, url):
        """test org"""
        g = GithubOrgClient(url)
