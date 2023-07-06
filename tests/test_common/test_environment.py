import unittest
from unittest.mock import patch
from services.common.environment import *

class TestEnvironment(unittest.TestCase):
    @patch('builtins.input', return_value=' sIt ')
    def test_get_environment_sit(self, mock_input):
        result = get_environment()
        self.assertEqual(result, 'sit')

    @patch('builtins.input', return_value=' prOd ')
    def test_get_environment_prod(self, mock_input):
        result = get_environment()
        self.assertEqual(result, 'prod')

    @patch('builtins.input', return_value=' IncOrrEct ')
    def test_get_environment_incorrect(self, mock_input):
        result = get_environment()
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()