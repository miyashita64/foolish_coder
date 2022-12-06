"""
@file   __main__.py
@brief  FoolishCoderのメインタスク
@author miyashita64
"""

import os

from src.error_analyzer.error_handler import ErrorHandler
from src.parser.parse_controller import ParseController

def main():
    print("\nFoolish coding...\n")

    ErrorHandler.handle()

    test_code_path = "target_project/test/FeeCalculatorTest.cpp"
    testcases = ParseController.parse_testcase(test_code_path)

    print("\nComplete!!\n")

main()