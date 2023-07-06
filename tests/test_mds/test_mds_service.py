import unittest
from services.mds.mds_service import *

class TestMdsService(unittest.TestCase):
    def test_pop_svc_converter(self):
        pop_svc_array = ['Resource\n[A]', 'DSTA\n[H]']
        array = pop_svc_converter(pop_svc_array)
        expected_array = ['A', 'H']
        self.assertEqual(array, expected_array)

    def test_main_name_converter(self):
        table_name_array = ['it_main', 'nric_uuid_main', 'audit_code', 'audit_infotype', 'cd_tos_main', 'cd_test', 'it0001']
        array = main_name_converter(table_name_array)
        expected_array = ['it_main', 'nric_uuid_main', 'audit_code', 'audit_infotype', 'cdtos_main', 'cdtest_main', 'it0001_main']
        self.assertEqual(array, expected_array)

    def test_field_array_splitter(self):
        table_name_column_array = ['it0001', 'nan', 'nan', 'it0002', 'nan']
        field_column_array = ['nric', 'uuid', 'pernr', 'begda', 'endda']
        array = field_array_splitter(table_name_column_array, field_column_array)
        expected_array = [['nric', 'uuid', 'pernr'], ['begda', 'endda']]
        self.assertEqual(array, expected_array)

if __name__ == '__main__':
    unittest.main()