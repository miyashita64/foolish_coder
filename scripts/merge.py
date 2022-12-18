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
    print("======================================")
    print(test_result)
    print("======================================")
    return TEST_OK_KEYWORD in test_result

def merge():
    # リファクタリング優先でコンフリクトを解決する
    print("refactorブランチをマージします")
    merge_target = ""
    subprocess.run(["make", "--no-print-directory", "merge_ahead_refactor"])
    print("refactorを優先してマージしました")
    print("==TEST RESULT==")
    print(is_test_ok())
    if is_test_ok():
        merge_target = "refactor"
        print(f"{merge_target}がテストに通りました")
    # 自動生成優先でコンフリクトを解決する
    else:
        print("テストに失敗しました")
        print("generateブランチをマージします")
        subprocess.run(["make", "--no-print-directory", "merge_ahead_generate"])
        print("generateを優先してマージしました")
        print("==TEST RESULT==")
        print(is_test_ok())
        if is_test_ok():
            merge_target = "generate"
            print(f"{merge_target}がテストに通りました")
    subprocess.run(["git", "switch", "generate"])
    if merge_target != "":
        subprocess.run(["make", "--no-print-directory", f"merge_ahead_{merge_target}_approve"])
    else:
        print("どれもテストに通ってない！！おかしい！！")

if __name__ == "__main__":
    merge()