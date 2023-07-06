from openpyxl import *
import os
import unittest
from unittest.mock import patch
from services.sft.sft_main import *

class TestSftMain(unittest.TestCase):
    def setUp(self):
        workbook = Workbook()
        sheet1 = workbook.active
        sheet1.title = 'SFT'
        sheet1.append(['-', '-', '-', '-'])
        sheet1.append(['SNS', '-', 'arn:sns:sns-test', '-'])
        sheet1.append(['HTTP', '-', 'https://callback.com', '-'])
        sheet1.append(['-', '-', '-', '-'])
        sheet1.append([True, 'application/pdf (.pdf)', '-', '-'])
        sheet1.append(['-', '-', '-', '-'])
        sheet1.append(['File Type', 'nan', '-', '-'])
        sheet1.append(['File Type', '(Select)', '-', '-'])
        sheet1.append(['File Type', 'image/jpg (.jpg)', '-', '-'])
        sheet1.append(['File Type', 'image/jpeg (.jpeg)', '-', '-'])
        sheet1.append(['File Type', 'image/jpeg (.jpeg)', '-', '-'])
        workbook.save('./excels/sft-test.xlsx')

    def tearDown(self):
        os.remove('./excels/sft-test.xlsx')
        os.remove('./artifacts/onboarding/sft-test-SFT_authorizer_v1.json')
        os.remove('./artifacts/onboarding/sft-test-SFT_authorizer_v2.json')

    def test_sft_main(self):
        with patch('builtins.print') as mock_print:
            excel_path = './excels/sft-test.xlsx'
            app_name = 'sft-test'
            env = 'sit'
            output = sft_main(excel_path, app_name, env)
            self.assertEqual(mock_print.call_count, 2)
            expected_outputs = ["SFT Authorizer V1: Generated", "SFT Authorizer V2: Generated"]
            actual_outputs = [call[0][0] for call in mock_print.call_args_list]
            self.assertListEqual(expected_outputs, actual_outputs)

if __name__ == '__main__':
    unittest.main()