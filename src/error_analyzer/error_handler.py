"""
@file   error_handler.py
@brief  エラーに対する処理を呼び出すクラス
@author miyashita64
"""

import os

from src.error_analyzer.file_reader import FileReader


class ErrorHandler:
    @staticmethod
    def handle():
        for no_file_name in FileReader.get_error_by_no_such_file():
            path = f"./results/{no_file_name}"
            print(f"Creating file {path} ...", end = "\t")
            f = open(path, 'w')
            f.write('')
            f.close()
            print("Created!!")

        # for no_declared_class_name in FileReader.get_error_by_has_not_been_declared():
        #     path = f"./results/{no_declared_class_name}.h"
        #     print(f"Creating class \"{no_declared_class_name}\" on {path} ....", end = "\t")
        #     code = f"class {no_declared_class_name}"+"{};"
        #     f = open(path, 'w')
        #     f.write(code)
        #     f.close()
        #     print("Created!!")

        for fatal in FileReader.get_error_by_was_not_declared_class_in_this_scope():
            path = f"./results/{fatal['class_name']}.h"
            print(f"Creating class \"{fatal['class_name']}\" on {path} ....", end = "\t")
            code = f"class {fatal['class_name']}"+"{};"
            f = open(path, 'w')
            f.write(code)
            f.close()
            print("Created!!")

        for fatal in FileReader.get_error_by_is_not_a_member_of_class():
            path = f"./results/{fatal['class_name']}.h"
            print(f"Adding member \"{fatal['member_name']}\" on class {fatal['class_name']} ....", end = "\t")
            code = f"class {fatal['class_name']}"+"{\n"
            code += f" public:\n"
            code += f"\tvoid {fatal['member_name']}()"+"{};\n"
            code += "};"
            f = open(path, 'w')
            f.write(code)
            f.close()
            print("Created!!")

        for fatal in FileReader.get_error_by_has_no_member_named():
            path = f"./results/{fatal['class_name']}.h"
            print(f"Adding member \"{fatal['member_name']}\" on class {fatal['class_name']} ....", end = "\t")
            code = f"class {fatal['class_name']}"+"{\n"
            code += f" public:\n"
            code += f"\tvoid {fatal['member_name']}()"+"{};\n"
            code += "};"
            f = open(path, 'w')
            f.write(code)
            f.close()
            print("Created!!")