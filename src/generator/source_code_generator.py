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
        conds = SourceCodeGenerator.demo(testcases)
        if len(conds) == 0:
            return None
        # 仮に全てのテストケースは1つのメンバ関数に対するものとする
        class_name = testcases[0]["target_class_name"]
        function_name = testcases[0]["target_method_name"]
        function_type = testcases[0]["expected"]["type"]
        function_arguments = [Variable("val1", arg) for arg in testcases[0]["arguments"]]
        function_statements = conds
        # コードデータを作成する
        function = Function(function_name, class_name, function_type, function_arguments, function_statements)
        target_class = CPPClass(class_name, function_members=[function])
        return target_class

    @staticmethod
    def demo(testcases):
        # テストケースから同一の入力を省く
        args_list = [testcase["arguments"] for testcase in testcases]
        unique_testcases = [testcases[i] for i in range(len(args_list)) if args_list[i] not in args_list[i+1:]]
        # 第1引数でソート
        sorted_testcases = sorted(unique_testcases, key=lambda testcase: max([testcase["arguments"][0]]))
        # 各出力における引数の範囲を探索する
        cond_expressions = []
        cond_expression = CondExpression(None, None, None)
        for testcase in sorted_testcases:
            # 新しい出力を発見した場合
            if testcase["expected"]["value"] != cond_expression.value:
                # 出力がNoneなテストケースは無視する
                if cond_expression.value != None:
                    cond_expressions.append(cond_expression)
                # 条件式をインスタンス化する
                cond_expression = CondExpression(testcase["expected"]["value"], testcase["arguments"][0], testcase["arguments"][0])
            else:
                # 出力が同じな場合、入力の範囲を広げる
                cond_expression.max = testcase["arguments"][0]
        return cond_expressions