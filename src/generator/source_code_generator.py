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
    def generate(testcases, source_classes):
        # テストケースから中間データを生成する
        return SourceCodeGenerator.demo(testcases, source_classes)

    @staticmethod
    def demo(testcases, source_classes):
        # テストケースをクラス・メソッド毎に集約する
        class_infos = {}
        has_args_testcases = [testcase for testcase in testcases if testcase["arguments"] != []]
        for testcase in has_args_testcases:
            class_name = testcase["target_class_name"]
            method_name = testcase["target_method_name"]
            # 未登録のクラスを発見した場合
            if class_name not in class_infos:
                class_infos[class_name] = {"method_infos": {}, "function_members": [], "source": None, }
                # ソースコード情報から同名のクラスを検索する
                source_class_tmps = [src for src in source_classes if src["name"] == class_name]
                if len(source_class_tmps) > 0:
                    class_infos[class_name]["source"] = source_class_tmps[0]
            # 未登録のメソッドを発見した場合
            if method_name not in class_infos[class_name]["method_infos"]:
                # ソースコード情報から同名メソッドを検索する
                source_class = class_infos[class_name]["source"]
                source_method = None
                if source_class is not None:
                    source_method_tmps = [src for src in source_class["public"]["functions"] if src["name"] == method_name]
                    if len(source_method_tmps) > 0:
                        source_method = source_method_tmps[0]
                # ソースコードの情報を優先してメソッドの引数名を決定する
                arg_names = []
                for i in range(len(testcase["arguments"])):
                    name = f"param{i+1}"
                    if source_method is not None and len(source_method["args"]) > i:
                        name = source_method["args"][i]["name"]
                    arg_names.append(name)
                # メソッド情報を作成し、クラス情報に追加する
                class_infos[class_name]["method_infos"][method_name] = {
                    "access": "public",
                    "type": testcase["expected"]["type"],
                    "args": [Variable(arg_names[i], testcase["arguments"][i]) for i in range(len(testcase["arguments"]))],
                    "testcases": [testcase],
                    "source": source_method,
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
