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
    def get_no_such_file_error():
        """ファイルが見つからない場合のエラーを取得する."""
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