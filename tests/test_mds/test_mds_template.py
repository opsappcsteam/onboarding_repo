import unittest
from services.mds.mds_template import *

class TestMdsTemplate(unittest.TestCase):
    def test_mds_template_entry(self):
        app_name = 'mds-test' 
        template = 'testTemplate' 
        template_id = 'testTemplateId' 
        dynamic_value_array = ['test'] 
        i = 0
        entry = mds_template_entry(app_name, template, template_id, dynamic_value_array, i)
        expected_entry = '''

# 1
-   pkstatus: true
    dataSource: hasura
    querytemplate: 'testTemplate'
    pk: testTemplateId
    appid: mds-test
    paramValuesSchema:
        test:
            pattern:
            type:
    required:
        - test'''
        self.assertEqual(entry, expected_entry)

    def test_mds_template_content(self):
        app_name = 'mds-test' 
        template_array = ['testTemplate'] 
        template_id_array = ['testTemplateId'] 
        dynamic_value_arrays = [['test']]
        content = mds_template_content(app_name, template_array, template_id_array, dynamic_value_arrays)
        expected_content = '''---

# 1
-   pkstatus: true
    dataSource: hasura
    querytemplate: 'testTemplate'
    pk: testTemplateId
    appid: mds-test
    paramValuesSchema:
        test:
            pattern:
            type:
    required:
        - test'''
        self.assertEqual(content, expected_content)

if __name__ == '__main__':
    unittest.main()