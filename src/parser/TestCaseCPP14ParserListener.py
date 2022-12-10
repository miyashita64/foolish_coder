"""
@file   TestCaseCPP14ParserListener.py
@brief  C++テストケースのパース時のイベントリスナ
@author miyashita64
"""

from src.parser.CPP14ParserListener import CPP14ParserListener
from src.parser.CPP14Parser import CPP14Parser
from src.parser.parser_method import *

import re

class TestCaseCPP14ParserListener(CPP14ParserListener):
    def __init__(self, target_path):
        self.target_path = target_path
        self.assertions = []    # DeclarationStatementContext
        self.testcases = []

    # 解析終了時の処理
    def exitTranslationUnit(self, ctx:CPP14Parser.TranslationUnitContext):
        # 各アサーションについて、テストケースを抽出する
        for assertion in self.assertions:       # DeclarationStatementContext
            # アサーションの種類と引数(targets)を抽出する
            assertion_ctx = descend(descend(assertion).getChild(0))
            assertion_type = assertion_ctx.getChild(0)  # NoPointerDeclaratorContext
            assertion_content = descend(descend(descend(assertion_ctx).getChild(1)).getChild(1))   # ParameterDeclarationListContext
            assertion_targets = [assertion_content.getChild(0), assertion_content.getChild(2)]     # List<ParameterDeclarationContext>

            # アサーションを保持するTESTブロックを抽出する
            test_body = ascend_to_type(assertion.parentCtx, [CPP14Parser.FunctionBodyContext])     # FunctionBodyContext(を探す)
            if test_body is None:
                continue
            test_name, testcase_name = descend(descend(descend(test_body.parentCtx.getChild(0)).getChild(1)).getChild(1)).getText().split(",")

            # 変数表を構築する
            variable_table = {}
            statements = descend(test_body).getChild(1).getChildren()  # StatementSeqContext
            for statement in statements:    # StatementContext
                simple_declaration = descend(statement) # SimpleDeclarationContext
                # 文頭がデータ型かクラス名な文を抽出する
                if type(simple_declaration.getChild(0)) is CPP14Parser.DeclSpecifierSeqContext:
                    # 型(必須)、変数名(必須)、値(任意)を抽出する
                    variable_type_ctx = simple_declaration.getChild(0) # TypeSpecifierContext
                    variable_type = variable_type_ctx.getText()
                    variable_name = simple_declaration.getChild(1).getChild(0).getChild(0).getText()  # DeclaratorContext
                    assignment = simple_declaration.getChild(1).getChild(0).getChild(1) # InitializerContext
                    assignment_value_ctx = None
                    assignment_value = None
                    if assignment is not None:
                        assignment_value_ctx = assignment.getChild(0).getChild(1)   # InitializerClauseContext
                        assignment_value = assignment_value_ctx.getText()   # InitializerClauseContext
                    variable_table[variable_name] = {
                        "type": variable_type,
                        "type_ctx": variable_type_ctx,
                        "value": assignment_value,
                        "value_ctx": assignment_value_ctx,
                    }

            # テストケースを抽出する(テスト対象、入力、期待出力)
            testcase = {
                "test_name": test_name,
                "testcase_name": testcase_name,
                "target_class_name": "",
                "target_method_name": "",
                "arguments": [],
                "expected": None,
            }
            for assertion_target in assertion_targets:
                variable = None
                target_value_ctx = assertion_target
                while target_value_ctx.getText() in variable_table:
                    variable = variable_table[target_value_ctx.getText()]
                    target_value_ctx = variable["value_ctx"]
                # 値と式とで型が異なる階層まで潜る
                value_ctx = descend(target_value_ctx)
                if value_ctx.getChildCount() <= 2:
                    # 値が見つかった場合、それを期待出力とする
                    testcase["expected"] = {
                        "type": variable["type"],
                        "value": cast(target_value_ctx.getText(), variable["type"]),
                    }
                else:
                    # 式が見つかった場合、それをテスト対象の呼び出しとする
                    testcase["arguments"] = [predict_cast(child.getText()) for child in value_ctx.getChild(2).getChild(0).getChildren() if type(child) is CPP14Parser.InitializerClauseContext]
                    if value_ctx.getChildCount() >= 3:
                        instance_name = descend(value_ctx.getChild(0)).getChild(0).getText()
                        if instance_name in variable_table:
                            testcase["target_class_name"] = variable_table[instance_name]["type"]
                        testcase["target_method_name"] = value_ctx.getChild(0).getChild(2).getText()
                    elif value_ctx.getChildCount() >= 1:
                        testcase["target_method_name"] = value_ctx.getChild(0).getChild(0).getText()
            # テストケースを追加する
            self.testcases.append(testcase)

    # 式検出時の処理
    def enterDeclarationStatement(self, ctx:CPP14Parser.DeclarationStatementContext):
        # アサーションを抽出する
        pattern = "EXPECT_EQ"
        if re.match(pattern, ctx.getText()):
            self.assertions.append(ctx)