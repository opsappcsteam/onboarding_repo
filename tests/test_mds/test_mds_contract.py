import unittest
from services.mds.mds_contract import *

class TestMdsContract(unittest.TestCase):
    def test_mds_contract_entry(self):
        table_name = 'it0001_main'
        field_array = ['nric', 'uuid', 'pernr']
        entry = mds_contract_entry(table_name, field_array)
        expected_entry = '''
-   tablename: it0001_main
    columns: [nric, uuid, pernr]
    limit: null
    allow_aggregations: false
'''
        self.assertEqual(entry, expected_entry)

    def test_mds_contract_content(self):
        app_name = 'mds-test' 
        pop_svc_array = ['A', 'H', '0001', '0002'] 
        table_name_array = ['it0001_main'] 
        field_arrays = [['nric', 'uuid', 'pernr']]
        content = mds_contract_content(app_name, pop_svc_array, table_name_array, field_arrays)
        expected_content = '''---
role: [mds-test]
filter: {
    it0001_persg: [A,H], # e.g [A,B,C]
    it0001_werks: ["0001","0002"]  # e.g ["0001","0002","0003"]
}

table:
-   tablename: it0001_main
    columns: [nric, uuid, pernr]
    limit: null
    allow_aggregations: false
'''
        self.assertEqual(content, expected_content)

if __name__ == '__main__':
    unittest.main()