#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Test suite for Access Nested Map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ({"a": {"b": {"c": 3}}}, ("a", "b", "c"), 3)
    ])
    def test_access_nested_map(self, nested_map, path, result):
        """testcase for access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """testcase for exception raised in access_nested_map"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Class for get_json test"""
    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False}),
    ])
    def test_get_json(self, url, test_payload):
        """testcase for get_json"""
        with patch('requests.get') as mocked_get:
            mocked_get.return_value.json.return_value = test_payload
            response = get_json(url)

            mocked_get.assert_called_once_with(url)
            self.assertEqual(response, test_payload)


class TestMemoize(unittest.TestCase):
    """
    Class to test Memoize
    """
    def test_memoize(self):
        """
        testcase for memoize
        """
        class TestClass:
            """
            Test class for class TestMemoize test
            """
            def a_method(self):
                """defines a_method"""
                return 42

            @memoize
            def a_property(self):
                """define a_property"""
                return self.a_method()
        with patch.object(TestClass, 'a_method',
                          return_value=42) as mocked_a_method:
            TestClassInstance = TestClass()
            TestClassInstance.a_property
            TestClassInstance.a_property
            mocked_a_method.assert_called_once()


if __name__ == '__main__':
    """Main body for test execution"""
    unittest.main()
