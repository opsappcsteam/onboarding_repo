import unittest

from services.mcns.mcns_config import *

class TestMcnsConfig(unittest.TestCase):
    maxDiff = None

    def test_mcns_configuration_entry_sms(self):
        app_name = 'app-test'
        template_id = 'templateId'
        channel_type = 'sms'
        sender = 'testSender'
        env = 'sit'
        entry = mcns_configuration_entry(app_name, template_id, channel_type, sender, env)
        expected_entry = '''
        {
            "PutRequest": {
                "Item": {
                    "pk": {
                        "S": "app-test#testsender#templateId"
                    },
                    "sk": {
                        "S": "sms"
                    },
                    "appid": {
                        "S": "<placeholder>"
                    },
                    "originationNumber": {
                        "S": "+6580283091"
                    }
                }
            }
        },'''
        self.assertEqual(entry, expected_entry)

        app_name = 'app-test'
        template_id = 'templateId'
        channel_type = 'sms'
        sender = 'nan'
        env = 'sit'
        entry = mcns_configuration_entry(app_name, template_id, channel_type, sender, env)
        expected_entry = '''
        {
            "PutRequest": {
                "Item": {
                    "pk": {
                        "S": "app-test#+6580283091#templateId"
                    },
                    "sk": {
                        "S": "sms"
                    },
                    "appid": {
                        "S": "<placeholder>"
                    },
                    "originationNumber": {
                        "S": "+6580283091"
                    }
                }
            }
        },'''
        self.assertEqual(entry, expected_entry)

        app_name = 'app-test'
        template_id = 'templateId'
        channel_type = 'sms'
        sender = 'testSender'
        env = 'prod'
        entry = mcns_configuration_entry(app_name, template_id, channel_type, sender, env)
        expected_entry = '''
        {
            "PutRequest": {
                "Item": {
                    "pk": {
                        "S": "app-test#testSender#templateId"
                    },
                    "sk": {
                        "S": "sms"
                    },
                    "appid": {
                        "S": "<placeholder>"
                    },
                    "originationNumber": {
                        "S": "73884"
                    }
                }
            }
        },'''
        self.assertEqual(entry, expected_entry)

        app_name = 'app-test'
        template_id = 'templateId'
        channel_type = 'sms'
        sender = 'nan'
        env = 'prod'
        entry = mcns_configuration_entry(app_name, template_id, channel_type, sender, env)
        expected_entry = '''
        {
            "PutRequest": {
                "Item": {
                    "pk": {
                        "S": "app-test#MINDEF#templateId"
                    },
                    "sk": {
                        "S": "sms"
                    },
                    "appid": {
                        "S": "<placeholder>"
                    },
                    "originationNumber": {
                        "S": "73884"
                    }
                }
            }
        },'''
        self.assertEqual(entry, expected_entry)

    def test_mcns_configuration_entry_email(self):
        app_name = 'app-test'
        template_id = 'templateId'
        channel_type = 'email'
        sender = 'testSender'
        env = 'sit'
        entry = mcns_configuration_entry(app_name, template_id, channel_type, sender, env)
        expected_entry = '''
        {
            "PutRequest": {
                "Item": {
                    "pk": {
                        "S": "app-test#testsender@sit.df-mcns.com#templateId"
                    },
                    "sk": {
                        "S": "email"
                    },
                    "appid": {
                        "S": "<placeholder>"
                    }
                }
            }
        },'''
        self.assertEqual(entry, expected_entry)

        app_name = 'app-test'
        template_id = 'templateId'
        channel_type = 'email'
        sender = 'testSender'
        env = 'prod'
        entry = mcns_configuration_entry(app_name, template_id, channel_type, sender, env)
        expected_entry = '''
        {
            "PutRequest": {
                "Item": {
                    "pk": {
                        "S": "app-test#testSender@mcns.defence.gov.sg#templateId"
                    },
                    "sk": {
                        "S": "email"
                    },
                    "appid": {
                        "S": "<placeholder>"
                    }
                }
            }
        },'''
        self.assertEqual(entry, expected_entry)

    def test_mcns_configuration_entry_push(self):
        app_name = 'app-test'
        template_id = 'templateId'
        channel_type = 'push'
        sender = 'testSender'
        env = 'sit'
        entry = mcns_configuration_entry(app_name, template_id, channel_type, sender, env)
        expected_entry = '''
        {
            "PutRequest": {
                "Item": {
                    "pk": {
                        "S": "app-test#testsender#templateId"
                    },
                    "sk": {
                        "S": "push"
                    },
                    "appid": {
                        "S": "<placeholder>"
                    }
                }
            }
        },'''
        self.assertEqual(entry, expected_entry)

        app_name = 'app-test'
        template_id = 'templateId'
        channel_type = 'push'
        sender = 'testSender'
        env = 'prod'
        entry = mcns_configuration_entry(app_name, template_id, channel_type, sender, env)
        expected_entry = '''
        {
            "PutRequest": {
                "Item": {
                    "pk": {
                        "S": "app-test#testSender#templateId"
                    },
                    "sk": {
                        "S": "push"
                    },
                    "appid": {
                        "S": "<placeholder>"
                    }
                }
            }
        },'''
        self.assertEqual(entry, expected_entry)

    def test_mcns_configuration_content(self):
        app_name = 'app-test'
        template_id_array = ['templateId1', 'templateId2'] 
        channel_type_array = ['sms', 'email']
        sender_array = ['testSms', 'testEmail']
        template_array = ['template1', 'template2']
        env  = 'sit'
        content = mcns_configuration_content(app_name, template_id_array, channel_type_array, sender_array, template_array, env)
        expected_content = '''{
    "mcns-configuration-sit": [ 
        {
            "PutRequest": {
                "Item": {
                    "pk": {
                        "S": "app-test#testsms#templateId1"
                    },
                    "sk": {
                        "S": "sms"
                    },
                    "appid": {
                        "S": "<placeholder>"
                    },
                    "originationNumber": {
                        "S": "+6580283091"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "pk": {
                        "S": "app-test#testemail@sit.df-mcns.com#templateId2"
                    },
                    "sk": {
                        "S": "email"
                    },
                    "appid": {
                        "S": "<placeholder>"
                    }
                }
            }
        }
    ]
}'''
        self.assertEqual(content, expected_content)

        app_name = 'app-test'
        template_id_array = ['templateId1', 'templateId2'] 
        channel_type_array = ['sms', 'email']
        sender_array = ['testSms', 'testEmail']
        template_array = ['template1', 'template2']
        env  = 'prod'
        content = mcns_configuration_content(app_name, template_id_array, channel_type_array, sender_array, template_array, env)
        expected_content = '''{
    "mcns-configuration-prod": [ 
        {
            "PutRequest": {
                "Item": {
                    "pk": {
                        "S": "app-test#testSms#templateId1"
                    },
                    "sk": {
                        "S": "sms"
                    },
                    "appid": {
                        "S": "<placeholder>"
                    },
                    "originationNumber": {
                        "S": "73884"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "pk": {
                        "S": "app-test#testEmail@mcns.defence.gov.sg#templateId2"
                    },
                    "sk": {
                        "S": "email"
                    },
                    "appid": {
                        "S": "<placeholder>"
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
        sender_array = ['testSms', 'nan']
        template_array = ['template1', 'nan']
        env  = 'prod'
        content = mcns_configuration_content(app_name, template_id_array, channel_type_array, sender_array, template_array, env)
        expected_content = '''{
    "mcns-configuration-prod": [ 
        {
            "PutRequest": {
                "Item": {
                    "pk": {
                        "S": "app-test#testSms#templateId1"
                    },
                    "sk": {
                        "S": "sms"
                    },
                    "appid": {
                        "S": "<placeholder>"
                    },
                    "originationNumber": {
                        "S": "73884"
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
        sender_array = ['testSms', 'nan']
        template_array = ['nan', 'nan']
        env  = 'prod'
        content = mcns_configuration_content(app_name, template_id_array, channel_type_array, sender_array, template_array, env)
        self.assertIsNone(content)

if __name__ == '__main__':
    unittest.main()
