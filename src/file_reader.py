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
        # 最新のビルドログファイル名を取得する.
        build_log_file_names = glob.glob(BUILD_LOG_PATH)
        latest_log_file_name = max(build_log_file_names, key=os.path.getctime)
        # ログを読み込む
        latest_log_file = open(latest_log_file_name, "r")
        latest_log = latest_log_file.read()
        latest_log_file.close()
        return latest_log
