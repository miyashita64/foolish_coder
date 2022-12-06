"""
@file   file_reader.py
@brief  ファイル読み込みクラス
@author miyashita64
"""

import glob
import os

BUILD_LOG_PATH = "target_project/logs/*"


class FileReader:
    @staticmethod
    def read_latest_build_log():
        """最新のビルドログを取得する."""
        # 最新のビルドログファイル名を取得する
        build_log_file_names = glob.glob(BUILD_LOG_PATH)
        latest_build_log_file_name = max(build_log_file_names, key=os.path.getctime)
        # ログを読み込む
        latest_build_log_file = open(latest_build_log_file_name, "r")
        latest_build_log = latest_build_log_file.read()
        latest_build_log_file.close()
        return latest_build_log

    @staticmethod
    def get_error_by_no_such_file():
        """未発見エラーを起こしたファイル名のリストを返す."""
        latest_build_log = FileReader.read_latest_build_log()
        errors = latest_build_log.split("No such file")
        if len(errors) <= 1:
            print("no error \"no such file\".")
            return []
        no_file_names = []
        for error in errors:
            if error == errors[-1]:
                break
            no_file_names += [error.split("fatal error: ")[-1].split(":")[0]]
        return no_file_names

    # @staticmethod
    # def get_error_by_has_not_been_declared():
    #     """未定義エラーを起こした名のリストを返す."""
    #     latest_build_log = FileReader.read_latest_build_log()
    #     no_declared_names = []
    #     for row in latest_build_log.split("\n"):
    #         if "error: " in row and "has not been declared" in row:
    #             no_declared_name = row.split("error: ‘")[1].split("’ has not been declared")[0]
    #             no_declared_names.append(no_declared_name)
    #     if no_declared_names == []:
    #         print("no error \"has not been declared\".")
    #     return no_declared_names

    @staticmethod
    def get_error_by_was_not_declared_class_in_this_scope():
        """スコープ内における未定義エラーを起こしたクラス名のリストを返す."""
        latest_build_log = FileReader.read_latest_build_log()
        fatals = []
        pre_row = ""
        for row in latest_build_log.split("\n"):
            if "error: " in row and "was not declared in this scope" in row:
                # 未定義のクラス名を抽出
                no_declared_class = row.split("error: ‘")[1].split("’ was not declared in this scope")[0]
                # 失敗したテストケース名を抽出
                fatal_test_name, fatal_testcase_name, _ = pre_row.split(": In member function ‘virtual void ")[1].split("::")[1].split("_")
                fatals.append({
                    "test_name": fatal_test_name,
                    "testcase_name": fatal_testcase_name,
                    "class_name": no_declared_class,
                })
                # クラスが未定義の場合、インスタンスにも同様のエラーが出るため１つ見つかった時点で終了する
                break
            pre_row = row
        if fatals == []:
            print("no error \"was not declared in this scope\".")
        return fatals

    @staticmethod
    def get_error_by_is_not_a_member_of_class():
        """未定義エラーを起こしたメンバ名とそれを持つクラス名のリストを返す."""
        latest_build_log = FileReader.read_latest_build_log()
        fatals = []
        for row in latest_build_log.split("\n"):
            if "error: " in row and "is not a member of" in row:
                # 未定義のメンバ名を抽出
                no_member = row.split("error: ‘")[1].split("’ is not a member of")[0]
                # 未定義のメンバを持つクラス名を抽出
                target_class = row.split("is not a member of ‘")[1].split("’")[0]
                # 失敗したテストケース名を抽出
                fatal_test_name, fatal_testcase_name, _ = pre_row.split(": In member function ‘virtual void ")[1].split("::")[1].split("_")
                fatals.append({
                    "test_name": fatal_test_name,
                    "testcase_name": fatal_testcase_name,
                    "class_name": target_class,
                    "member_name": no_member,
                })
            pre_row = row
        if fatals == []:
            print("no error \"not a member of Class\".")
        return fatals

    @staticmethod
    def get_error_by_has_no_member_named():
        """未定義エラーを起こしたメンバ名とそれを持つクラス名のリストを返す."""
        latest_build_log = FileReader.read_latest_build_log()
        fatals = []
        pre_row = ""
        for row in latest_build_log.split("\n"):
            if "error: " in row and "has no member named" in row:
                # 未定義のメンバ名を抽出する
                no_member = row.split("has no member named ‘")[1].split("’")[0]
                # 未定義のメンバを持つクラス名を抽出する
                target_class = row.split("error: ‘class ")[1].split("’")[0]
                # 失敗したテストケース名を抽出する
                fatal_test_name, fatal_testcase_name, _ = pre_row.split(": In member function ‘virtual void ")[1].split("::")[1].split("_")
                fatals.append({
                    "test_name": fatal_test_name,
                    "testcase_name": fatal_testcase_name,
                    "class_name": target_class,
                    "member_name": no_member,
                })
            pre_row = row
        if fatals == []:
            print("no error \"has no member named\".")
        return fatals
