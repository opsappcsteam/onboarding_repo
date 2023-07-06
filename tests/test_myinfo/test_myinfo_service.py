from openpyxl import Workbook
import pandas as pd
import os
import unittest
from services.common.excelsheet import *
from services.myinfo.myinfo_service import *

class TestMyinfoService(unittest.TestCase):
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
        workbook.save('./excels/myinfo-test.xlsx')

    def tearDown(self):
        os.remove('./excels/myinfo-test.xlsx')

    def test_myinfo_array(self):
        sheet_info = pd.read_excel(excel_path(), 'MyInfo')
        output = myinfo_array(sheet_info)
        expected_output = ['True', 'True', 'False', 'False', 'True', 'False']
        self.assertEqual(output, expected_output)

    def test_attributes_converter(self):
        attributes_array = ['False', 'False', 'False', 'True', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'False', 'True', 'False']
        output = attributes_converter(attributes_array)
        expected_output = ['sex', 'childrenbirthrecords.sex']
        self.assertEqual(output, expected_output)

    def test_redirect_uri_converter(self):
        redirect_uri = ['https://redirect-uri.com']
        output = redirect_uri_converter(redirect_uri)
        expected_output = 'https://redirect-uri.com'
        self.assertEqual(output, expected_output)

    def test_authenticated_flow_converter(self):
        authenticated_flow = 'yes'
        output = authenticated_flow_converter(authenticated_flow)
        expected_output = 'true'
        self.assertEqual(output, expected_output)

        authenticated_flow = 'no'
        output = authenticated_flow_converter(authenticated_flow)
        expected_output = 'false'
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()