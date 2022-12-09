"""
@file   source_code_generator.py
@brief  ソースコード生成クラス
@author miyashita64
"""

import numpy as np
from src.structure.cond_expression import CondExpression
from src.structure.variable import Variable
from src.structure.function import Function
from src.structure.cpp_class import CPPClass

class SourceCodeGenerator:
    @staticmethod
    def generate(testcases):
        # テストケースから中間データを生成する
        return SourceCodeGenerator.demo(testcases)

    @staticmethod
    def demo(testcases):
        # テストケースをクラス・メソッド毎に集約する
        class_infos = {}
        for testcase in testcases:
            class_name = testcase["target_class_name"]
            method_name = testcase["target_method_name"]
            # 未登録のクラスを発見した場合
            if class_name not in class_infos:
                class_infos[class_name] = {"method_infos": {}, "function_members": []}
            # 未登録のメソッドを発見した場合
            if method_name not in class_infos[class_name]["method_infos"]:
                class_infos[class_name]["method_infos"][method_name] = {
                    "type": testcase["expected"]["type"],
                    "args": [Variable("val1", arg) for arg in testcase["arguments"]],
                    "testcases": [testcase],
                }
            else:
                class_infos[class_name]["method_infos"][method_name]["testcases"].append(testcase)

        # 中間データを生成する
        middle_datas = []
        for class_name in class_infos:
            class_info = class_infos[class_name]
            for method_name in class_info["method_infos"]:
                method_info = class_info["method_infos"][method_name]
                # テストケースから同一の入力を省く
                args_list = [testcase["arguments"] for testcase in method_info["testcases"]]
                unique_testcases = [method_info["testcases"][i] for i in range(len(args_list)) if args_list[i] not in args_list[i+1:]]
                # 第1引数でソート
                sorted_testcases = sorted(unique_testcases, key=lambda testcase: max([testcase["arguments"][0]]))
                method_info["testcases"] = sorted_testcases

                # テストケースを同じ期待出力毎に集約する形で、ソースコードを設計する
                cond_expressions = []
                cond_expression = CondExpression(None, None, None)
                for testcase in method_info["testcases"]:
                    # 新しい出力を発見した場合
                    if testcase["expected"]["value"] != cond_expression.value:
                        # 出力がNoneなテストケースは無視する(初回は必ずNone)
                        if cond_expression.value != None:
                            cond_expressions.append(cond_expression)
                        # 条件式をインスタンス化する
                        cond_expression = CondExpression(testcase["expected"]["value"], testcase["arguments"][0], testcase["arguments"][0])
                    else:
                        # 出力が同じな場合、入力の範囲を広げる
                        cond_expression.max = testcase["arguments"][0]
                # 最後ループのCondExpressionを追加する
                cond_expressions.append(cond_expression)
                # 関数の中間データを生成する
                function = Function(method_name, class_name, method_info["type"],  method_info["args"], cond_expressions)
                class_info["function_members"].append(function)
            # CPPクラスの中間データを生成する
            cpp_class = CPPClass(class_name, function_members=class_info["function_members"])
            middle_datas.append(cpp_class)
        return middle_datas
