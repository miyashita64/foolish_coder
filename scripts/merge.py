"""
@file   merge.py
@brief  テストの可否を検証しmergeを実行するスクリプト
@author miyashita64
"""

import time
import subprocess
from subprocess import PIPE

def is_test_ok():
    TEST_OK_KEYWORD = "[  PASSED  ]"
    time.sleep(0.3)
    test_result = subprocess.run(["make", "--no-print-directory", "is_test_ok"], stdout=PIPE, stderr=PIPE).stdout.decode('utf-8')
    print("Testing ...")
    print("======================================")
    print(test_result)
    print("======================================")
    return TEST_OK_KEYWORD in test_result

def merge():
    # リファクタリング優先でコンフリクトを解決する
    print("Merging branch named \"refactor\" ... ", end="")
    merge_target = ""
    subprocess.run(["make", "--no-print-directory", "merge_ahead_refactor"])
    print("Succeed!!")
    if is_test_ok():
        merge_target = "refactor"
        print(f"\"{merge_target}\" passed tests!\n")
    # 自動生成優先でコンフリクトを解決する
    else:
        print(f"\"{merge_target}\" faild tests.\n")
        print("Merging branch named \"generate\" ... ", end="")
        subprocess.run(["make", "--no-print-directory", "merge_ahead_generate"])
        print("Succeed!!")
        if is_test_ok():
            merge_target = "generate"
            print(f"\"{merge_target}\" passed tests!\n")
    subprocess.run(["git", "switch", "generate"])
    if merge_target != "":
        print(f"Merging branch named \"{merge_target}\" ... ", end="")
        subprocess.run(["make", "--no-print-directory", f"merge_ahead_{merge_target}_approve"])
        print("Succeed!!")
    else:
        print("!!!!!!!!テストをパスできるブランチがない!!おかしい!!!!!!!!")

if __name__ == "__main__":
    merge()