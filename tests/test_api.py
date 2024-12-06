import unittest
from unittest import result
from unittest.mock import patch

import requests
import self

from src.api_class import HhJobService


class TestHhJobService(unittest.TestCase):
    @patch('requests.get')
    def test_get_jobs(self, mock_requests_get):
        mock_response = {'items': [{'name': 'Python Developer', 'alternate_url': 'example.com',
                                    'salary': {'from':100000}, 'description': 'Experience: 3 years'}]}
        mock_requests_get.return_value.json.return_value = mock_response

        hh_api = HhJobService()
        result = hh_api.get_jobs('Python Developer')
"""Проверка что метод возвращает ожидаемый результат"""
        self.assertEqual(result, mock_response)

if __name__ == '__main__':
    unittest.main()