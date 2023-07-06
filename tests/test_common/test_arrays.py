from openpyxl import Workbook
import pandas as pd
import os
import unittest
from services.common.excelsheet import *
from services.common.arrays import *

class TestArrays(unittest.TestCase):
    def setUp(self):
        workbook = Workbook()
        sheet1 = workbook.active
        sheet1.title = 'Tab1'
        sheet1.append(['-', '-', '-', '-'])
        sheet1.append(['-', 'Row', 'value1', '-'])
        sheet1.append(['-', 'Row', 'value2', '-'])
        sheet1.append(['-', 'Row', 'value3', '-'])
        sheet1.append(['-', '-', '-', '-'])
        sheet1.append(['-', 'Table Name', '-', 'Field'])
        sheet1.append(['-', 'it0001', '-', 'nric'])
        sheet1.append(['-', '-', '-', 'uuid'])
        sheet1.append(['-', '-', '-', 'pernr'])
        sheet1.append(['-', '<Add more entries here if necessary>', '-', '-'])
        workbook.save('./excels/testing.xlsx')

    def tearDown(self):
        os.remove('./excels/testing.xlsx')

    def test_row_array(self):
        sheet_info = pd.read_excel(excel_path(), 'Tab1')
        array = row_array(sheet_info, 'Row', 1)
        expected_array = ['value1', 'value2', 'value3']
        self.assertEqual(array, expected_array)

        sheet_info = pd.read_excel(excel_path(), 'Tab1')
        array = row_array(sheet_info, 'Incorrect', 1)
        expected_array = []
        self.assertEqual(array, expected_array)

    def test_column_array(self):
        sheet_info = pd.read_excel(excel_path(), 'Tab1')
        array = column_array(sheet_info, 'Field')
        expected_array = ['nric', 'uuid', 'pernr']
        self.assertEqual(array, expected_array)

        sheet_info = pd.read_excel(excel_path(), 'Tab1')
        array = column_array(sheet_info, 'Incorrect')
        expected_array = []
        self.assertEqual(array, expected_array)

if __name__ == '__main__':
    unittest.main()