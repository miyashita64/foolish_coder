"""
@file   __main__.py
@brief  FoolishCoderのメインタスク
@author miyashita64
"""

import os

from src.error_analyzer.error_analyzer import ErrorAnalyzer
from src.error_analyzer.error_handler import ErrorHandler
from src.parser.parse_controller import ParseController
from src.generator.source_code_generator import SourceCodeGenerator
from src.structure.file import File

def main():
    print("\nFoolish coding...\n")

    BUILD_LOG_FILE_NAME = "latest_error.txt"
    BUILD_LOG_DIR_PATH = "target_project/logs/"
    TEST_CODE_FILE_NAME = "FeeCalculatorTest.cpp"
    TEST_CODE_DIR_PATH = "target_project/test/"

    # エラー解析
    errors = ErrorAnalyzer.analyze(BUILD_LOG_FILE_NAME, BUILD_LOG_DIR_PATH)
    no_file_error_count = len(errors["no_file_errors"])
    no_class_error_count = len(errors["no_class_errors"])
    no_member_error_count = len(errors["no_member_errors"])
    print()
    print(f"No such {no_file_error_count} files.")
    print(f"No such {no_class_error_count} classes.")
    print(f"No such {no_member_error_count} memvers.\n")

    if no_file_error_count > 0:
        # ファイルが見つからないエラーは、テストケースを通さないため再実行する
        ErrorHandler.handle(errors)
        os.system("make run")
        exit()
    # テストケース解析
    testcases = ParseController.parse_testcase(TEST_CODE_FILE_NAME, TEST_CODE_DIR_PATH)
    # ソースコード解析
    # 自動生成
    patched_class = SourceCodeGenerator.generate(testcases)
    target_file = File(patched_class.file_name)
    target_file.write(patched_class.get_code())

    print("\nCompleted!!\n")

main()