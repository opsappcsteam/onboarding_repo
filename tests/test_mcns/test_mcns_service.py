import unittest

from services.mcns.mcns_service import *

class TestMcnsService(unittest.TestCase):
    def test_uuid_generator(self):
        template_id_array = ['email1', 'sms1', 'push1']
        template_id_list = uuid_generator(template_id_array)
        expected_template_id_list = ['email1', 'sms1', 'push1']
        self.assertEqual(template_id_list, expected_template_id_list)

        template_id_array = ['nan', 'nan']
        expected_output = ['<channel_type>00000000000000000000000000000001', '<channel_type>00000000000000000000000000000001']
        uuid.uuid4 = lambda: uuid.UUID('00000000-0000-0000-0000-000000000001')
        self.assertEqual(uuid_generator(template_id_array), expected_output)

    def test_channel_type_converter(self):
        channel_type_array = ['Email', 'SMS', 'Push']
        converted_channel_type_array = channel_type_converter(channel_type_array)
        expected_converted_channel_type_array = ['email', 'sms', 'push']
        self.assertEqual(converted_channel_type_array, expected_converted_channel_type_array)

    def test_template_id_converter(self):
        template_id_array = ['<channel_type>123456789', '<channel_type>987654321', '<channel_type>000000000']
        channel_type_array = ['email', 'sms', 'push']
        converted_template_id_array = template_id_converter(template_id_array, channel_type_array)
        expected_converted_template_id_array = ['email123456789', 'sms987654321', 'push000000000']
        self.assertEqual(converted_template_id_array, expected_converted_template_id_array)

    def test_regex_json_converter(self):
        regex_json_array = ['"', '\\', '   ', '\n']
        array = regex_json_converter(regex_json_array)
        expected_array = ['\\"', '\\\\\\\\', '', ' ']
        self.assertEqual(array, expected_array)

        regex_json_array = ['''{
    "test": "value1",
    "test2": "value2"
}''']
        array = regex_json_converter(regex_json_array)
        expected_array = ['{ \\"test\\": \\"value1\\", \\"test2\\": \\"value2\\" }']
        self.assertEqual(array, expected_array)

if __name__ == '__main__':
    unittest.main()