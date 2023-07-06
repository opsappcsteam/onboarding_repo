from openpyxl import Workbook

import os
import unittest
from unittest.mock import patch

from services.mcns.mcns_main import *

class TestMcnsMain(unittest.TestCase):
    def setUp(self):
        workbook = Workbook()
        sheet1 = workbook.active
        sheet1.title = 'MCNS'
        sheet1.append(['-', '-', '-', '-'])
        sheet1.append(['Template ID', '-', 'testTemplate', '-'])
        sheet1.append(['Channel Type', '-', 'SMS', '-'])
        sheet1.append(['Sender', '-', 'testSender', '-'])
        sheet1.append(['Subject', '-', 'testSubject', '-'])
        sheet1.append(['Template', '-', '${value1} ${value2}', '-'])
        sheet1.append(["Template Values' Regular Expression", '-', '{ "value1":"test1", "value2":"test2" }', '-'])
        workbook.save('./excels/mcns-test.xlsx')

    def tearDown(self):
        os.remove('./excels/mcns-test.xlsx')
        os.remove('./artifacts/onboarding/mcns-test-MCNS_authorizer.json')
        os.remove('./artifacts/onboarding/mcns-test-MCNS_configuration.json')

    def test_mcns_main(self):
        with patch('builtins.print') as mock_print:
            excel_path = './excels/mcns-test.xlsx'
            app_name = 'mcns-test'
            env = 'sit'
            mcns_main(excel_path, app_name, env)
            self.assertEqual(mock_print.call_count, 2)
            expected_outputs = ["MCNS Authorizer: Generated", "MCNS Configuration: Generated"]
            actual_outputs = [call[0][0] for call in mock_print.call_args_list]
            self.assertListEqual(expected_outputs, actual_outputs)

if __name__ == '__main__':
    unittest.main()
