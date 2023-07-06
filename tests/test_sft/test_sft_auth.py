import unittest
from services.sft.sft_auth import *

class TestSftAuth(unittest.TestCase):
    maxDiff = None
    def test_sft_authorizer_entry(self):
        app_name = 'sft-test'
        sns_callback = ['arn:sns:test']
        http_callback = ['https://callback.com'] 
        file_type = 'image/jpeg'
        output = sft_authorizer_entry(app_name, sns_callback, http_callback, file_type)
        expected_output = '''
        {
            "PutRequest": {
                "Item": {
                    "pk": {
                        "S": "sft-test#image/jpeg"
                    },
                    "pkstatus": {
                        "S": "true"
                    },
                    "httpCallback": {
                        "S": "https://callback.com"
                    },
                    "callback": {
                        "S": "arn:sns:test"
                    }
                }
            }
        },'''
        self.assertEqual(output, expected_output)

    def test_sft_authorizer_content(self):
        app_name = 'sft-test'
        sns_callback = ['arn:sns:test']
        http_callback = ['https://callback.com'] 
        file_type_array = ['image/jpeg', 'image/tiff']
        env = 'prod'
        output = sft_authorizer_content(app_name, sns_callback, http_callback, file_type_array, env)
        expected_output = '''{
    "sft-authorizer-prod": [ 
        {
            "PutRequest": {
                "Item": {
                    "pk": {
                        "S": "sft-test#image/jpeg"
                    },
                    "pkstatus": {
                        "S": "true"
                    },
                    "httpCallback": {
                        "S": "https://callback.com"
                    },
                    "callback": {
                        "S": "arn:sns:test"
                    }
                }
            }
        },
        {
            "PutRequest": {
                "Item": {
                    "pk": {
                        "S": "sft-test#image/tiff"
                    },
                    "pkstatus": {
                        "S": "true"
                    },
                    "httpCallback": {
                        "S": "https://callback.com"
                    },
                    "callback": {
                        "S": "arn:sns:test"
                    }
                }
            }
        }
    ]
}'''
        self.assertEqual(output, expected_output)

        app_name = 'sft-test'
        sns_callback = ['arn:sns:test']
        http_callback = ['https://callback.com'] 
        file_type_array = ['image/jpeg']
        env = 'prod'
        output = sft_authorizer_content(app_name, sns_callback, http_callback, file_type_array, env)
        expected_output = '''{
    "sft-authorizer-prod": [ 
        {
            "PutRequest": {
                "Item": {
                    "pk": {
                        "S": "sft-test#image/jpeg"
                    },
                    "pkstatus": {
                        "S": "true"
                    },
                    "httpCallback": {
                        "S": "https://callback.com"
                    },
                    "callback": {
                        "S": "arn:sns:test"
                    }
                }
            }
        }
    ]
}'''
        self.assertEqual(output, expected_output)

        app_name = 'sft-test'
        sns_callback = ['arn:sns:test']
        http_callback = ['https://callback.com'] 
        file_type_array = []
        env = 'prod'
        output = sft_authorizer_content(app_name, sns_callback, http_callback, file_type_array, env)
        self.assertIsNone(output)

if __name__ == '__main__':
    unittest.main()