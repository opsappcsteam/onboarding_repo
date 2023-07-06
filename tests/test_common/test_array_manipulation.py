import unittest
from services.common.array_manipulation import *

class TestCommonArrayManipulation(unittest.TestCase):
    def test_nan_remover(self):
        array = nan_remover(['nan', 'nan', 'testValue'])
        expected_array = ['testValue']
        self.assertEqual(array, expected_array)

        array = nan_remover(['nan'])
        expected_array = []
        self.assertEqual(array, expected_array)

        array = nan_remover([])
        expected_array = []
        self.assertEqual(array, expected_array)

    def test_template_subject_cleaner(self):
        array = ['$(value1) TEST', '"${value2}" "TEST"', '"$(value3)"']
        service = 'MDS'
        clean_template_array = template_subject_cleaner(array, service)
        expected_clean_template_array = ['${value1} test', '${value2} "TEST"', '${value3}']
        self.assertEqual(clean_template_array, expected_clean_template_array)

        array = ['$(value1) TEST', '"${value2}" "TEST"', '"$(value3)"']
        service = 'MPDS'
        clean_template_array = template_subject_cleaner(array, service)
        expected_clean_template_array = ['${value1} test', '${value2} "TEST"', '${value3}']
        self.assertEqual(clean_template_array, expected_clean_template_array)

        array = ['$(value1) TEST', '"${value2}" "TEST"', '"$(value3)"']
        service = 'MCNS'
        clean_template_array = template_subject_cleaner(array, service)
        expected_clean_template_array = ['${value1} TEST', r'\"${value2}\" \"TEST\"', r'\"${value3}\"']
        self.assertEqual(clean_template_array, expected_clean_template_array)

    def test_dynamic_values_array_generator(self):
        subject_array = ['test']
        template_array = ['test']
        dynamic_values_array = dynamic_values_array_generator(subject_array, template_array)
        expected_dynamic_values_array = [[]]
        self.assertEqual(dynamic_values_array, expected_dynamic_values_array)

        subject_array = ['test']
        template_array = ['${value1}']
        dynamic_values_array = dynamic_values_array_generator(subject_array, template_array)
        expected_dynamic_values_array = [['value1']]
        self.assertEqual(dynamic_values_array, expected_dynamic_values_array)

        subject_array = ['${value1}']
        template_array = ['test']
        dynamic_values_array = dynamic_values_array_generator(subject_array, template_array)
        expected_dynamic_values_array = [['value1']]
        self.assertEqual(dynamic_values_array, expected_dynamic_values_array)

        subject_array = []
        template_array = ['test']
        dynamic_values_array = dynamic_values_array_generator(subject_array, template_array)
        expected_dynamic_values_array = [[]]
        self.assertEqual(dynamic_values_array, expected_dynamic_values_array)

        subject_array = []
        template_array = ['${value1}']
        dynamic_values_array = dynamic_values_array_generator(subject_array, template_array)
        expected_dynamic_values_array = [['value1']]
        self.assertEqual(dynamic_values_array, expected_dynamic_values_array)

        subject_array = ['${value1}']
        template_array = []
        dynamic_values_array = dynamic_values_array_generator(subject_array, template_array)
        expected_dynamic_values_array = [['value1']]
        self.assertEqual(dynamic_values_array, expected_dynamic_values_array)

        subject_array = []
        template_array = []
        dynamic_values_array = dynamic_values_array_generator(subject_array, template_array)
        expected_dynamic_values_array = [[]]
        self.assertEqual(dynamic_values_array, expected_dynamic_values_array)

if __name__ == '__main__':
    unittest.main()