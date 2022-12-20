"""
@file   error_analyzer.py
@brief  ファイル読み込みクラス
@author miyashita64
"""

from src.structure.file import File


class ErrorAnalyzer:
    @staticmethod
    def analyze(log_file_name, log_dir_path):
        """指定されたパスのログを解析する."""
        log_file = File(log_file_name, log_dir_path)
        log_text = log_file.read()
        # 存在しないファイル名のリスト
        no_file_errors = ErrorAnalyzer.get_error_by_no_such_file(log_text)
        no_class_errors = ErrorAnalyzer.get_error_by_was_not_declared_class_in_this_scope(log_text)
        no_member_errors = ErrorAnalyzer.get_error_by_is_not_a_member_of_class(log_text)
        no_member_errors += ErrorAnalyzer.get_error_by_has_no_member_named(log_text)
        return {
            "no_file_errors": no_file_errors,
            "no_class_errors": no_class_errors,
            "no_member_errors": no_member_errors,
        }

    @staticmethod
    def get_faild_testcase_count(log_file_name, log_dir_path):
        """失敗したテストケースの数を取得する."""
        log_file = File(log_file_name, log_dir_path)
        log_text = log_file.read()
        for row in log_text.split("\n"):
            if "FAILED TEST" in row:
                if len(row.split(" ")) >= 1:
                    count = row.split(" ")[1]
                    if count.isdecimal():
                        return int(count)
        return 0

    @staticmethod
    def get_error_by_no_such_file(log_text):
        """未発見エラーを起こしたファイル名のリストを返す."""
        errors = log_text.split("No such file")
        no_file_names = []
        for error in errors:
            if error == errors[-1]:
                break
            no_file_names += [{"file_name": error.split("fatal error: ")[-1].split(":")[0]}]
        return no_file_names

    @staticmethod
    def get_error_by_was_not_declared_class_in_this_scope(log_text):
        """スコープ内における未定義エラーを起こしたクラス名のリストを返す."""
        fatals = []
        pre_row = ""
        for row in log_text.split("\n"):
            if "error: " in row and "was not declared in this scope" in row:
                try:
                    # 未定義のクラス名を抽出
                    no_declared_class = row.split("error: ‘")[1].split("’ was not declared in this scope")[0]
                    # 失敗したテストケース名を抽出
                    fatal_test_name, fatal_testcase_name, *_ = pre_row.split(": In member function ‘virtual void ")[1].split("::")[1].split("_")
                    fatals.append({
                        "test_name": fatal_test_name,
                        "testcase_name": fatal_testcase_name,
                        "class_name": no_declared_class,
                    })
                    # クラスが未定義の場合、インスタンスにも同様のエラーが出るため１つ見つかった時点で終了する
                    break
                except:
                    pass
            pre_row = row
        return fatals

    @staticmethod
    def get_error_by_is_not_a_member_of_class(log_text):
        """未定義エラーを起こしたメンバ名とそれを持つクラス名のリストを返す."""
        fatals = []
        for row in log_text.split("\n"):
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
        return fatals

    @staticmethod
    def get_error_by_has_no_member_named(log_text):
        """未定義エラーを起こしたメンバ名とそれを持つクラス名のリストを返す."""
        fatals = []
        pre_row = ""
        for row in log_text.split("\n"):
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
        return fatals
