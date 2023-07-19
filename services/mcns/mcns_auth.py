import unittest

from services.mcns.mcns_auth import *

class TestMcnsAuth(unittest.TestCase):
    maxDiff = None
    def test_mcns_authorizer_entry_sms(self):
        app_name = 'app-test'
        template_id = 'testTemplateId'
        channel_type = 'sms'
        sender = 'testSender'
        subject = 'testSubject'
        template = 'testTemplate'
        dynamic_value_array = ['value1', 'value2']
        regex_json = '{ \\"test\\": \\"value1\\", \\"test2\\": \\"value2\\" }'
        env = 'sit'
        entry = mcns_authorizer_entry(app_name, template_id, channel_type, sender, subject, template, dynamic_value_array, regex_json, env)
        expected_entry = '''
        {
            "PutRequest": {
                "Item": {
                    "pk": {
                        "S": "app-test#testsender#testTemplateId"
                    },
                    "subject": {
                        "S": "MCNS Notification"
                    },
                    "templateValueSchema": {
                        "S": "{\\"$schema\\":\\"https://json-schema.org/draft/2020-12/schema\\",\\"$id\\":\\"https://dsta.gov.sg/app1.schema.json\\",\\"title\\":\\"app1\\",\\"type\\":\\"object\\",\\"properties\\":{\\"value1\\":{\\"description\\":\\"value1field\\", \\"type\\":\\"string\\"}, \\"value2\\":{\\"description\\":\\"value2field\\", \\"type\\":\\"string\\"}},\\"required\\":[\\"value1\\", \\"value2\\"]}"
                    },
                    "template": {
                        "S": "testTemplate"
                    },
                    "regEx": {
                        "S": "{ \\"test\\": \\"value1\\", \\"test2\\": \\"value2\\" }"
                    },
                    "pkstatus": {
                        "S": "true"
                    }
                }
            }
        },'''
        self.assertEqual(entry, expected_entry)

        app_name = 'app-test'
        template_id = 'testTemplateId'
        channel_type = 'sms'
        sender = 'nan'
        subject = 'testSubject'
        template = 'testTemplate'
        dynamic_value_array = ['value1', 'value2']
        regex_json = '{ \\"test\\": \\"value1\\", \\"test2\\": \\"value2\\" }'
        env = 'prod'
        entry = mcns_authorizer_entry(app_name, template_id, channel_type, sender, subject, template, dynamic_value_array, regex_json, env)
        expected_entry = '''
        {
            "PutRequest": {
                "Item": {
                    "pk": {
                        "S": "app-test#MINDEF#testTemplateId"
                    },
                    "subject": {
                        "S": "MCNS Notification"
                    },
                    "templateValueSchema": {
                        "S": "{\\"$schema\\":\\"https://json-schema.org/draft/2020-12/schema\\",\\"$id\\":\\"https://dsta.gov.sg/app1.schema.json\\",\\"title\\":\\"app1\\",\\"type\\":\\"object\\",\\"properties\\":{\\"value1\\":{\\"description\\":\\"value1field\\", \\"type\\":\\"string\\"}, \\"value2\\":{\\"description\\":\\"value2field\\", \\"type\\":\\"string\\"}},\\"required\\":[\\"value1\\", \\"value2\\"]}"
                    },
                    "template": {
                        "S": "testTemplate"
                    },
                    "regEx": {
                        "S": "{ \\"test\\": \\"value1\\", \\"test2\\": \\"value2\\" }"
                    },
                    "pkstatus": {
                        "S": "true"
                    }
                }
            }
        },'''
        self.assertEqual(entry, expected_entry)

        app_name = 'app-test'
        template_id = 'testTemplateId'
        channel_type = 'sms'
        sender = 'testSender'
        subject = 'testSubject'
        template = 'testTemplate'
        dynamic_value_array = ['value1', 'value2']
        regex_json = '{ \\"test\\": \\"value1\\", \\"test2\\": \\"value2\\" }'
        env = 'prod'
        entry = mcns_authorizer_entry(app_name, template_id, channel_type, sender, subject, template, dynamic_value_array, regex_json, env)
        expected_entry = '''
        {
            "PutRequest": {
                "Item": {
                    "pk": {
                        "S": "app-test#testSender#testTemplateId"
                    },
                    "subject": {
                        "S": "MCNS Notification"
                    },
                    "templateValueSchema": {
                        "S": "{\\"$schema\\":\\"https://json-schema.org/draft/2020-12/schema\\",\\"$id\\":\\"https://dsta.gov.sg/app1.schema.json\\",\\"title\\":\\"app1\\",\\"type\\":\\"object\\",\\"properties\\":{\\"value1\\":{\\"description\\":\\"value1field\\", \\"type\\":\\"string\\"}, \\"value2\\":{\\"description\\":\\"value2field\\", \\"type\\":\\"string\\"}},\\"required\\":[\\"value1\\", \\"value2\\"]}"
                    },
                    "template": {
                        "S": "testTemplate"
                    },
                    "regEx": {
                        "S": "{ \\"test\\": \\"value1\\", \\"test2\\": \\"value2\\" }"
                    },
                    "pkstatus": {
                        "S": "true"
                    }
                }
            }
        },'''
        self.assertEqual(entry, expected_entry)

    def test_mcns_authorizer_entry_email(self):
        app_name = 'app-test'
        template_id = 'testTemplateId'
        channel_type = 'email'
        sender = 'testSender'
        subject = 'testSubject'
        template = 'testTemplate'
        dynamic_value_array = ['value1', 'value2']
        regex_json = '{ \\"test\\": \\"value1\\", \\"test2\\": \\"value2\\" }'
        env = 'sit'
        entry = mcns_authorizer_entry(app_name, template_id, channel_type, sender, subject, template, dynamic_value_array, regex_json, env)
        expected_entry = '''
        {
            "PutRequest": {
                "Item": {
                    "pk": {
                        "S": "app-test#testsender@sit.df-mcns.com#testTemplateId"
                    },
                    "subject": {
                        "S": "testSubject"
                    },
                    "templateValueSchema": {
                        "S": "{\\"$schema\\":\\"https://json-schema.org/draft/2020-12/schema\\",\\"$id\\":\\"https://dsta.gov.sg/app1.schema.json\\",\\"title\\":\\"app1\\",\\"type\\":\\"object\\",\\"properties\\":{\\"value1\\":{\\"description\\":\\"value1field\\", \\"type\\":\\"string\\"}, \\"value2\\":{\\"description\\":\\"value2field\\", \\"type\\":\\"string\\"}},\\"required\\":[\\"value1\\", \\"value2\\"]}"
                    },
                    "template": {
                        "S": "testTemplate"
                    },
                    "regEx": {
                        "S": "{ \\"test\\": \\"value1\\", \\"test2\\": \\"value2\\" }"
                    },
                    "pkstatus": {
                        "S": "true"
                    },
                    "attachmentAllowed": {
                        "S": "true"
                    }
                }
            }
        },'''
        self.assertEqual(entry, expected_entry)

    def test_mcns_authorizer_entry_push(self):
        app_name = 'app-test'
        template_id = 'testTemplateId'
        channel_type = 'push'
        sender = 'testSender'
        subject = 'testSubject'
        template = 'testTemplate'
        dynamic_value_array = ['value1', 'value2']
        regex_json = '{ \\"test\\": \\"value1\\", \\"test2\\": \\"value2\\" }'
        env = 'sit'
        entry = mcns_authorizer_entry(app_name, template_id, channel_type, sender, subject, template, dynamic_value_array, regex_json, env)
        expected_entry = '''
        {
            "PutRequest": {
                "Item": {
                    "pk": {
                        "S": "app-test#testsender#testTemplateId"
                    },
                    "subject": {
                        "S": "testSubject"
                    },
                    "templateValueSchema": {
                        "S": "{\\"$schema\\":\\"https://json-schema.org/draft/2020-12/schema\\",\\"$id\\":\\"https://dsta.gov.sg/app1.schema.json\\",\\"title\\":\\"app1\\",\\"type\\":\\"object\\",\\"properties\\":{\\"value1\\":{\\"description\\":\\"value1field\\", \\"type\\":\\"string\\"}, \\"value2\\":{\\"description\\":\\"value2field\\", \\"type\\":\\"string\\"}},\\"required\\":[\\"value1\\", \\"value2\\"]}"
                    },
                    "template": {
                        "S": "testTemplate"
                    },
                    "regEx": {
                        "S": "{ \\"test\\": \\"value1\\", \\"test2\\": \\"value2\\" }"
                    },
                    "pkstatus": {
                        "S": "true"
                    }
                }
            }
        },'''
        self.assertEqual(entry, expected_entry)

    def test_mcns_authorizer_entry_no_dynamic_value(self):
        app_name = 'app-test'
        template_id = 'testTemplateId'
        channel_type = 'email'
        sender = 'testSender'
        subject = 'testSubject'
        template = 'testTemplate'
        dynamic_value_array = []
        regex_json = '{ \\"test\\": \\"value1\\", \\"test2\\": \\"value2\\" }'
        env = 'sit'
        entry = mcns_authorizer_entry(app_name, template_id, channel_type, sender, subject, template, dynamic_value_array, regex_json, env)
        expected_entry = '''
        {
            "PutRequest": {
                "Item": {
                    "pk": {
                        "S": "app-test#testsender@sit.df-mcns.com#testTemplateId"
                    },
                    "subject": {
                        "S": "testSubject"
                    },
                    "template": {
                        "S": "testTemplate"
                    },
                    "pkstatus": {
                        "S": "true"
                    },
                    "attachmentAllowed": {
                        "S": "true"
                    }
                }
            }
        },'''
        self.assertEqual(entry, expected_entry)

    def test_mcns_authorizer_content(self):
        app_name = 'app-test'
        template_id_array = ['templateId1']
        channel_type_array = ['sms'] 
        sender_array = ['testSender'] 
        subject_array = ['nan'] 
        template_array = ['testTemplate'] 
        dynamic_value_arrays = [['value1']]
        regex_json_array = ['{ \\"value1\\":\\"test1\\" }'] 
        env = 'sit'
        content = mcns_authorizer_content(app_name, template_id_array, channel_type_array, sender_array, subject_array, template_array, dynamic_value_arrays, regex_json_array, env)
        expected_content = '''{
    "mcns-authorizer-sit": [ 
        {
            "PutRequest": {
                "Item": {
                    "pk": {
                        "S": "app-test#testsender#templateId1"
                    },
                    "subject": {
                        "S": "MCNS Notification"
                    },
                    "templateValueSchema": {
                        "S": "{\\"$schema\\":\\"https://json-schema.org/draft/2020-12/schema\\",\\"$id\\":\\"https://dsta.gov.sg/app1.schema.json\\",\\"title\\":\\"app1\\",\\"type\\":\\"object\\",\\"properties\\":{\\"value1\\":{\\"description\\":\\"value1field\\", \\"type\\":\\"string\\"}},\\"required\\":[\\"value1\\"]}"
                    },
                    "template": {
                        "S": "testTemplate"
                    },
                    "regEx": {
                        "S": "{ \\"value1\\":\\"test1\\" }"
                    },
                    "pkstatus": {
                        "S": "true"
                    }
                }
            }
        }
    ]
}'''
        self.assertEqual(content, expected_content)

        app_name = 'app-test'
        template_id_array = ['templateId1', 'nan']
        channel_type_array = ['sms', 'nan'] 
        sender_array = ['testSender', 'nan'] 
        subject_array = ['nan', 'nan'] 
        template_array = ['testTemplate', 'nan'] 
        dynamic_value_arrays = [['value1'], ['nan']]
        regex_json_array = ['{ \\"value1\\":\\"test1\\" }', 'nan'] 
        env = 'sit'
        content = mcns_authorizer_content(app_name, template_id_array, channel_type_array, sender_array, subject_array, template_array, dynamic_value_arrays, regex_json_array, env)
        expected_content = '''{
    "mcns-authorizer-sit": [ 
        {
            "PutRequest": {
                "Item": {
                    "pk": {
                        "S": "app-test#testsender#templateId1"
                    },
                    "subject": {
                        "S": "MCNS Notification"
                    },
                    "templateValueSchema": {
                        "S": "{\\"$schema\\":\\"https://json-schema.org/draft/2020-12/schema\\",\\"$id\\":\\"https://dsta.gov.sg/app1.schema.json\\",\\"title\\":\\"app1\\",\\"type\\":\\"object\\",\\"properties\\":{\\"value1\\":{\\"description\\":\\"value1field\\", \\"type\\":\\"string\\"}},\\"required\\":[\\"value1\\"]}"
                    },
                    "template": {
                        "S": "testTemplate"
                    },
                    "regEx": {
                        "S": "{ \\"value1\\":\\"test1\\" }"
                    },
                    "pkstatus": {
                        "S": "true"
                    }
                }
            }
        }
    ]
}'''
        self.assertEqual(content, expected_content)

        app_name = 'app-test'
        template_id_array = ['templateId1', 'nan']
        channel_type_array = ['sms', 'nan'] 
        sender_array = ['testSender', 'nan'] 
        subject_array = ['nan', 'nan'] 
        template_array = ['nan', 'nan'] 
        dynamic_value_arrays = [['value1'], ['nan']]
        regex_json_array = ['{ \\"value1\\":\\"test1\\" }', 'nan'] 
        env = 'sit'
        content = mcns_authorizer_content(app_name, template_id_array, channel_type_array, sender_array, subject_array, template_array, dynamic_value_arrays, regex_json_array, env)
        self.assertIsNone(content)

if __name__ == '__main__':
    unittest.main()
