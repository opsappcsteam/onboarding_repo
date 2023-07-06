from openpyxl import Workbook
import os
import unittest
from services.common.excelsheet import *

class TestExcelsheet(unittest.TestCase):
    def setUp(self):
        workbook = Workbook()
        sheet1 = workbook.active
        sheet1.title = 'Tab1'
        sheet2 = workbook.create_sheet('Guide')
        workbook.save('./excels/testing.xlsx')

    def tearDown(self):
        os.remove('./excels/testing.xlsx')

    def test_excel_path(self):
        path = excel_path()
        expected_path = './excels/testing.xlsx'
        self.assertEqual(path, expected_path)

    def test_excel_name(self):
        name = excel_name()
        expected_name = 'testing'
        self.assertEqual(name, expected_name)

    def test_excel_sheets(self):
        sheets = excel_sheets()
        expected_sheets = ['Tab1']
        self.assertEqual(sheets, expected_sheets)

class test_excelsheet_none(unittest.TestCase):
    def test_excel_path(self):
        path = excel_path()
        self.assertIsNone(path)

if __name__ == '__main__':
    unittest.main()