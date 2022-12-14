"""
@file   merge.py
@brief  テストの可否を検証しmergeを実行するスクリプト
@author miyashita64
"""

import subprocess
from subprocess import PIPE

def is_test_ok():
    TEST_OK_KEYWORD = "[  PASSED  ]"
    test_result = subprocess.run(["make", "--no-print-directory", "is_test_ok"], stdout=PIPE, stderr=PIPE).stdout.decode('utf-8')
    return TEST_OK_KEYWORD in test_result

def merge():
    # リファクタリング優先でコンフリクトを解決する
    merge_target = ""
    subprocess.run(["make", "--no-print-directory", "merge_ahead_refactor"])
    if is_test_ok():
        merge_target = "refactor"
    # 自動生成優先でコンフリクトを解決する
    else:
        subprocess.run(["make", "--no-print-directory", "merge_ahead_generate"])
        if is_test_ok():
            merge_target = "generate"
    subprocess.run(["git", "switch", "generate"])
    if merge_target != "":
        subprocess.run(["make", "--no-print-directory", f"merge_ahead_{merge_target}_approve"])

if __name__ == "__main__":
    merge()