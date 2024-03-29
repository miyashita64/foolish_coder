"""
@file   __main__.py
@brief  FoolishCoderのメインタスク
@author miyashita64
"""

import os
import glob

from src.error_analyzer.error_analyzer import ErrorAnalyzer
from src.error_analyzer.error_handler import ErrorHandler
from src.parser.parse_controller import ParseController
from src.generator.source_code_generator import SourceCodeGenerator
from src.structure.file import File

def main():
    print("\nFoolish coding...\n")

    BUILD_LOG_FILE_NAME = "latest_error.txt"
    BUILD_LOG_DIR_PATH = "logs/errors/"
    TEST_LOG_FILE_NAME = "latest_result.txt"
    TEST_LOG_DIR_PATH = "logs/results/"
    TEST_CODE_DIR_PATH = "target_project/test/"
    SOURCE_CODE_DIR_PATH = "results/"

    # エラー解析
    errors = ErrorAnalyzer.analyze(BUILD_LOG_FILE_NAME, BUILD_LOG_DIR_PATH)
    no_file_error_count = len(errors["no_file_errors"])
    no_class_error_count = len(errors["no_class_errors"])
    no_member_error_count = len(errors["no_member_errors"])
    if no_file_error_count > 0:
        # ファイルが見つからないエラーは、テストケースを通さないため再実行する
        ErrorHandler.handle(errors)
        os.system("make --no-print-directory generate")
        exit(1)
    faild_test_count = ErrorAnalyzer.get_faild_testcase_count(TEST_LOG_FILE_NAME, TEST_LOG_DIR_PATH)
    print()
    print(f"No such {no_file_error_count} files.")
    print(f"No such {no_class_error_count} classes.")
    print(f"No such {no_member_error_count} members.")
    print(f"Faild {faild_test_count} testcases.\n")

    error_classes_names = [error["class_name"] for error in errors["no_class_errors"]] + [error["class_name"] for error in errors["no_member_errors"]]

    # テストコードを1つずつ解析する
    test_file_paths = glob.glob(f"{TEST_CODE_DIR_PATH}*.cpp")
    for test_file_path in test_file_paths:
        # テストケース解析
        testcases = ParseController.parse_testcase(test_file_path)
        source_classes = []
        for class_name in set([testcase["target_class_name"] for testcase in testcases]):
            # エラーが出ているクラスについてのみ扱う
            if class_name not in error_classes_names and faild_test_count == 0:
                print("\nNo error No need Generating.\n")
                exit(1)
            # ソースコード解析
            source_code_path = f"{SOURCE_CODE_DIR_PATH}{class_name}.h"
            source_class_tmps = ParseController.parse_source(source_code_path)
            if len(source_class_tmps) > 0:
                source_classes.append(*source_class_tmps)
        # ソースコード生成
        patched_classes = SourceCodeGenerator.generate(testcases, source_classes)
        for patched_class in patched_classes:
            target_header_file = File(patched_class.header_file_name)
            target_header_file.write(patched_class.get_header_code())
            target_source_file = File(patched_class.source_file_name)
            target_source_file.write(patched_class.get_source_code())

    print("\nCompleted Generating!!\n")

main()