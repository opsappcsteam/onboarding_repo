#!/bin/bash

# Common
python3 -m tests.test_common.test_file_generation
python3 -m tests.test_common.test_arrays
python3 -m tests.test_common.test_array_manipulation
python3 -m tests.test_common.test_environment
python3 -m tests.test_common.test_excelsheet

# MCNS
python3 -m tests.test_mcns.test_mcns_service
python3 -m tests.test_mcns.test_mcns_auth
python3 -m tests.test_mcns.test_mcns_config
python3 -m tests.test_mcns.test_mcns_main

# MDS
python3 -m tests.test_mds.test_mds_service
python3 -m tests.test_mds.test_mds_contract
python3 -m tests.test_mds.test_mds_template
python3 -m tests.test_mds.test_mds_main
python3 -m tests.test_mds.test_mpds_main

# MyInfo
python3 -m tests.test_myinfo.test_myinfo_service
python3 -m tests.test_myinfo.test_myinfo_auth
python3 -m tests.test_myinfo.test_myinfo_main

# SFT
python3 -m tests.test_sft.test_sft_service
python3 -m tests.test_sft.test_sft_auth
python3 -m tests.test_sft.test_sft_main