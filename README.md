# AppCS Onboarding Automation

## Setting up:
-setup.sh yet to be created-

## How it works:
The code will first check for an excelsheet in the './excels/' folder. After finding an existing excelsheet, it would get the full list of the sheet tab names in the excelsheet.

If a service is detected in the list of sheet tab names, the service-related functions will go through information within that specific sheet and extract out all the relevant information that is required for either a service/change request.

If a service is not detected, it would just be skipped.

## Things to note:
### Single excelsheet only:
As the code is checking for the first '.xlsx' file that it encounters, it may not be taking the intended excelsheet to run the automation on.

When you have multiple '.xlsx' files, make sure that only the intended file has the extension of '.xlsx'. The program will also show which file it has captured after you have entered the environment you are planning to onboard to.

### Excelsheet naming convention:
As some PMTs may submit onboarding forms without onboarding to SSO yet, the code takes the name of the excelsheet as the "potential SSO client id" or the existing SSO client id (if they are onboarded already).

This is also to factor in PMTs who are onboarding to Survey without an SSO Client ID and would need to input the "potential SSO Client ID".