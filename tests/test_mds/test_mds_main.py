from openpyxl import Workbook
import os
import unittest
from unittest.mock import patch
from services.mds.mds_main import *

class TestMdsMain(unittest.TestCase):
    def setUp(self):
        workbook = Workbook()
        sheet1 = workbook.active
        sheet1.title = 'MDS'
        sheet1.append(['-', '-', '-', '-'])
        sheet1.append([True, 'Resources\n[A]', True, 'DSTA\n[H]'])
        sheet1.append([True, 'Army\n[0001]', True, 'Navy\n[0002]'])
        sheet1.append(['-', '-', '-', '-'])
        sheet1.append(['-', 'Table Name', '-', 'Field'])
        sheet1.append(['-', 'it0001', '-', 'nric'])
        sheet1.append(['-', 'nan', '-', 'uuid'])
        sheet1.append(['-', 'nan', '-', 'pernr'])
        sheet1.append(['-', '<Add more entries here if necessary>', '-', '-'])
        sheet1.append(['-', '-', '-', '-'])
        sheet1.append(['Template ID', '-', '-', 'testTemplateId'])
        sheet1.append(['Template', '-', '-', 'testTemplate ${test} "TEST"'])
        workbook.save('./excels/mds-test.xlsx')

    def tearDown(self):
        os.remove('./excels/mds-test.xlsx')
        os.remove('./artifacts/onboarding/mds-test-MDS_data_contract.yaml')
        os.remove('./artifacts/onboarding/mds-test-MDS_query_template.yaml')

    def test_mds_main(self):
        with patch('builtins.print') as mock_print:
            excel_path = './excels/mds-test.xlsx'
            app_name = 'mds-test'
            main = mds_main(excel_path, app_name)
            self.assertEqual(mock_print.call_count, 2)
            expected_outputs = ["MDS Data Contract: Generated", "MDS Query Template: Generated"]
            actual_outputs = [call[0][0] for call in mock_print.call_args_list]
            self.assertListEqual(expected_outputs, actual_outputs)

if __name__ == '__main__':
    unittest.main()