"""
@file   __main__.py
@brief  FoolishCoderのメインタスク
@author miyashita64
"""

import os

from src.file_reader import FileReader

print("\nFoolish coding...\n")

latest_build_log = FileReader.read_latest_build_log()
for no_file_name in FileReader.get_no_such_file_error():
    path = f"./results/{no_file_name}"
    print(f"Create {path} ...", end = "\t")
    f = open(path, 'w')
    f.write('')
    f.close()
    print("Created!!")

print("\nComplete!!\n")
