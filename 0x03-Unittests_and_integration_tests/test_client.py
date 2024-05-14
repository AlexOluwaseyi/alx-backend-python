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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        # Setup the expected return values for the mocked functions
        repos_payload = [
            {'name': 'repo1', 'license': {'key': 'mit'}},
            {'name': 'repo2', 'license': {'key': 'gpl'}}
        ]
        expected_repos = ['repo1', 'repo2']

        # Mock return value for get_json to simulate the API response
        mock_get_json.return_value = repos_payload

        # Use patch as a context manager to mock _public_repos_url property
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = 'https://api.github.com\
                                                 /orgs/google/repos'
            client = GithubOrgClient("google")

            # Call the method under test
            result_repos = client.public_repos()

            # Assert that the result matches expected repos list
            self.assertEqual(result_repos, expected_repos)

            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with('https://api.github\
                                                  .com/orgs/google/repos')


if __name__ == '__main__':
    """Main body for test execution"""
    unittest.main()
