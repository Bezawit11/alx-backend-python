#!/usr/bin/env python3
"""unit test"""


import unittest
from unittest.mock import patch
from client import GithubOrgClient
get_json = __import__('utils').get_json
from parameterized import parameterized


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
        mock_org.assert_called_once()

    def test_public_repos_url(self):
        """test public repos"""
        with patch('GithubOrgClient.org') as mock:
            c = GithhubOrgClient('url')
            mock.return_value = {"repos_url": "tester"}
            self.assertEqual(c._public_repos_url(), mock.return_value)

    @patch('get_json') 
    def test_public_repos(self):
        """test public repos"""
        with patch('GithubOrgClient._public_repos_url') as mock:
            c = GithhubOrgClient('url')
            mock.return_value = [{"tester1": "result1", "tester2": "result2"}]
            self.assertEqual(c._public_repos(), mock.return_value)
