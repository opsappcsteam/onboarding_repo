from openpyxl import Workbook
import os
import unittest
from unittest.mock import patch
from services.myinfo.myinfo_main import *

class TestMyinfoMain(unittest.TestCase):
    def setUp(self):
        workbook = Workbook()
        sheet1 = workbook.active
        sheet1.title = 'MyInfo'
        sheet1.append(['-', '-'])
        sheet1.append([True, '-'])
        sheet1.append([True, '-'])
        sheet1.append([False, '-'])
        sheet1.append([False, '-'])
        sheet1.append([True, '-'])
        sheet1.append([False, '-'])
        sheet1.append([True, '-'])
        sheet1.append([True, '-'])
        sheet1.append([False, '-'])
        sheet1.append([False, '-'])
        sheet1.append([True, '-'])
        sheet1.append([False, '-'])
        sheet1.append([True, '-'])
        sheet1.append([True, '-'])
        sheet1.append([False, '-'])
        sheet1.append([False, '-'])
        sheet1.append([True, '-'])
        sheet1.append([False, '-'])
        sheet1.append(['Redirect URL:', '-', 'https://redirect-uri.com'])
        workbook.save('./excels/myinfo-test.xlsx')

    def tearDown(self):
        os.remove('./excels/myinfo-test.xlsx')
        os.remove('./artifacts/onboarding/myinfo-test-MyInfo_authorizer.json')

    def test_myinfo_main(self):
        with patch('builtins.print') as mock_print:
            excel_path = './excels/myinfo-test.xlsx'
            app_name = 'myinfo-test'
            output = myinfo_main(excel_path, app_name)
            self.assertEqual(mock_print.call_count, 1)
            expected_outputs = ["MyInfo Authorizer: Generated"]
            actual_outputs = [call[0][0] for call in mock_print.call_args_list]
            self.assertListEqual(expected_outputs, actual_outputs)


if __name__ == '__main__':
    unittest.main()