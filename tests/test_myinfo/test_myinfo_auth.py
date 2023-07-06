import unittest
from services.myinfo.myinfo_auth import *

class TestMyinfoAuth(unittest.TestCase):
    def test_myinfo_authorizer_content(self):
        app_name = 'myinfo-test' 
        attributes_array = ['uinfin', 'name', 'sex'] 
        redirect_uri = 'https://redirect-uri.com' 
        authenticated_flow = 'true'
        output = myinfo_authorizer_content(app_name, attributes_array, redirect_uri, authenticated_flow)
        expected_output = '''[
    {
        "pk": "myinfo-test",
        "attributes": [
            "uinfin",
            "name",
            "sex"
        ],
        "redirect_uri": "https://redirect-uri.com",
        "authenticated_flow": true
    }
]'''
        self.assertEqual(output, expected_output)

        app_name = 'myinfo-test' 
        attributes_array = ['uinfin', 'name', 'sex'] 
        redirect_uri = 'nan' 
        authenticated_flow = 'true'
        output = myinfo_authorizer_content(app_name, attributes_array, redirect_uri, authenticated_flow)
        self.assertIsNone(output)

if __name__ == '__main__':
    unittest.main()