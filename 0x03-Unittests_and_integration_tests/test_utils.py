#!/usr/bin/env python3
""" test file for fonctions already created """
import unittest
import utils
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
