"""
@file   error_handler.py
@brief  エラーに対する処理を呼び出すクラス
@author miyashita64
"""

import os


class ErrorHandler:
    @staticmethod
    def handle(errors):
        for no_file_error in errors["no_file_errors"]:
            path = f"./results/{no_file_error['file_name']}"
            print(f"Creating file {path} ...", end = "")
            f = open(path, 'w')
            f.write('')
            f.close()
            print("Created!!")

        # for no_class_error in errors["no_class_errors"]:
        #     path = f"./results/{no_class_error['class_name']}.h"
        #     print(f"Creating class \"{no_class_error['class_name']}\" on {path} ... ", end = "")
        #     code = f"class {no_class_error['class_name']}"+"{};"
        #     f = open(path, 'w')
        #     f.write(code)
        #     f.close()
        #     print("Created!!")

        # for no_member_error in errors["no_member_errors"]:
        #     path = f"./results/{no_member_error['class_name']}.h"
        #     print(f"Adding member \"{no_member_error['member_name']}\" on class {no_member_error['class_name']} ... ", end = "")
        #     code = f"class {no_member_error['class_name']}"+"{\n"
        #     code += f" public:\n"
        #     code += f"\tvoid {no_member_error['member_name']}()"+"{};\n"
        #     code += "};"
        #     f = open(path, 'w')
        #     f.write(code)
        #     f.close()
        #     print("Created!!")
