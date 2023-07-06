import os
import unittest
from unittest.mock import patch, mock_open
from services.common.file_generation import *

class TestFileGeneration(unittest.TestCase):
    def tearDown(self):
        os.remove('./artifacts/onboarding/app-test-TEST_authorizer.json')

    def test_onboarding_file_generation(self):
        with patch('builtins.print') as mock_print:
            app_name = 'app-test'
            service = 'TEST'
            file_name = 'Authorizer'
            file_content = None
            file_extension = '.json'
            version = ''
            onboarding_file_generation(app_name, service, file_name, file_content, file_extension, version)
            mock_print.assert_called_with('TEST Authorizer: Skipped')

        with patch('builtins.print') as mock_print:
            app_name = 'app-test'
            service = 'TEST'
            file_name = 'Authorizer'
            file_content = 'content'
            file_extension = '.json'
            version = ''
            onboarding_file_generation(app_name, service, file_name, file_content, file_extension, version)
            mock_print.assert_called_with('TEST Authorizer: Generated')

        with patch('builtins.open', mock_open()) as mock_file, patch('os.rename') as mock_rename, patch('builtins.print') as mock_print:
            app_name = 'app-test'
            service = 'TEST'
            file_name = 'Authorizer'
            file_content = 'content'
            file_extension = '.json'
            version = ''
            onboarding_file_generation(app_name, service, file_name, file_content, file_extension, version)
            mock_file.assert_called_once_with('./artifacts/onboarding/app-test-TEST_authorizer.txt', 'w')
            mock_file.return_value.write.assert_called_once_with(file_content)
            mock_rename.assert_called_once_with('./artifacts/onboarding/app-test-TEST_authorizer.txt', './artifacts/onboarding/app-test-TEST_authorizer.json')
            mock_print.assert_called_once_with('TEST Authorizer: Generated')

if __name__ == '__main__':
    unittest.main()