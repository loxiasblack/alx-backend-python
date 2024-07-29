#!/usr/bin/env python3
""" test file for fonctions already created """
import unittest
import utils
from utils import memoize
from parameterized import parameterized
from unittest.mock import patch, Mock
import requests


class TestAccessNestedMap(unittest.TestCase):
    """ the class access Nested map """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ test the function with different input """
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """test the type of the error raised"""
        self.assertRaises(KeyError)


class TestGetJson(unittest.TestCase):
    """ new class TestGeJson """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        mock_get.return_value.json.return_value = test_payload
        data = utils.get_json(test_url)
        self.assertEqual(data, test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """ class that test memoize decorator"""

    def test_memoize(self):
        """ test memoize method check if the proprety when called twice
        the method called once"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        new_obj = TestClass()
        with patch.object(new_obj, 'a_method', return_value=42) as mock_method:
            result1 = new_obj.a_property
            result1 = new_obj.a_property
            self.assertEqual(result1, 42)
            mock_method.assert_called_once()
