import unittest
from services.sft.sft_service import *

class TestSftService(unittest.TestCase):
    def test_file_type_cleaner(self):
        row_array = ['nan', '(Select)', 'image/jpg (.jpg)', 'image/jpeg (.jpeg)', 'image/jpeg (.jpeg)']
        output = file_type_cleaner(row_array)
        expected_output = ['image/jpeg']
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()