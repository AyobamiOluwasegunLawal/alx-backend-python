#!/usr/bin/env python3
from unittest import TestCase
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json

class TestAccessNestedMap(TestCase):
    @parameterized.expand([
        ({'a': 1}, ['a',], 1),
        ({'a': {'b':2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), repr(expected))

@patch('utils.requests.get')
def test_get_json(self, mock_get):
    cases = [
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ]

    for url, payload in cases:
        mock = Mock()
        mock.json.return_value = payload
        mock_get.return_value = mock

        result = get_json(url)

        mock_get.assert_called_once_with(url)
        self.assertEqual(result, payload)

        mock_get.reset_mock()






