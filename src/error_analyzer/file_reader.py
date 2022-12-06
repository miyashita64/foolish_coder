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

    @staticmethod
    def get_error_by_has_not_been_declared():
        """未定義エラーを起こした名のリストを返す."""
        latest_build_log = FileReader.read_latest_build_log()
        no_declared_names = []
        for row in latest_build_log.split("\n"):
            if "error: " in row and "has not been declared" in row:
                no_declared_name = row.split("error: ‘")[1].split("’ has not been declared")[0]
                no_declared_names.append(no_declared_name)
        if no_declared_names == []:
            print("no error \"has not been declared\".")
        return no_declared_names

    @staticmethod
    def get_error_by_was_not_declared_class_in_this_scope():
        """スコープ内における未定義エラーを起こしたクラス名のリストを返す."""
        latest_build_log = FileReader.read_latest_build_log()
        no_declared_classes = []
        for row in latest_build_log.split("\n"):
            if "error: " in row and "was not declared in this scope" in row:
                no_declared_class = row.split("error: ‘")[1].split("’ was not declared in this scope")[0]
                no_declared_classes.append(no_declared_class)
                # クラスが未定義の場合、インスタンスにも同様のエラーが出るため１つ見つかった時点で終了する
                break
        if no_declared_classes == []:
            print("no error \"was not declared in this scope\".")
        return no_declared_classes

    @staticmethod
    def get_error_by_is_not_a_member_of_class():
        """未定義エラーを起こしたメンバ名とそれを持つクラス名のリストを返す."""
        latest_build_log = FileReader.read_latest_build_log()
        no_members = []
        for row in latest_build_log.split("\n"):
            if "error: " in row and "is not a member of" in row:
                no_member = row.split("error: ‘")[1].split("’ is not a member of")[0]
                target_class = row.split("is not a member of ‘")[1].split("’")[0]
                no_members.append([no_member, target_class])
        if no_members == []:
            print("no error \"not a member of Class\".")
        return no_members

    @staticmethod
    def get_error_by_has_no_member_named():
        """未定義エラーを起こしたメンバ名とそれを持つクラス名のリストを返す."""
        latest_build_log = FileReader.read_latest_build_log()
        no_members = []
        for row in latest_build_log.split("\n"):
            if "error: " in row and "has no member named" in row:
                no_member = row.split("has no member named ‘")[1].split("’")[0]
                target_class = row.split("error: ‘class ")[1].split("’")[0]
                no_members.append([no_member, target_class])
        if no_members == []:
            print("no error \"has no member named\".")
        return no_members
