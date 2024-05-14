#!/usr/bin/env python3

"""
Unittests for GitHubOrgClients
"""

import unittest
from unittest.mock import patch, PropertyMock
# from client.GithubOrgClient import org
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """Test suite for GitHubOrgClient"""
    @parameterized.expand([
        ('google',), ('abc',)
    ])
    @patch('client.GithubOrgClient.org')
    def test_org(self, orgs, mock_org):
        """Test case for org method"""
        mock_org.return_value = {'org': orgs, 'status_code': '200'}
        client = GithubOrgClient(orgs)
        client.org(orgs)
        mock_org.assert_called_once()

    def test_public_repos_url(self):
        """test case for _pubblic_repos_url"""
        expected_org_payload = {'repos_url':
                                'https://api.github.com/orgs/google/repos'}
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = expected_org_payload
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url,
                             expected_org_payload['repos_url'])


if __name__ == '__main__':
    """Main body for test execution"""
    unittest.main()
