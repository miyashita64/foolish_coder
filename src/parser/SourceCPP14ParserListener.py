"""
@file   SourceCPP14ParserListener.py
@brief  C++ソースコードのパース時のイベントリスナ
@author miyashita64
"""

from src.parser.CPP14ParserListener import CPP14ParserListener
from src.parser.CPP14Parser import CPP14Parser
from src.parser.parser_method import *

import re

class SourceCPP14ParserListener(CPP14ParserListener):
    def __init__(self, target_path):
        self.target_path = target_path
        self.classes = []
        self.access_state = "private"

    # 解析開始時の処理
    def enterTranslationUnit(self, ctx:CPP14Parser.TranslationUnitContext):
        pass

    # 解析終了時の処理
    def exitTranslationUnit(self, ctx:CPP14Parser.TranslationUnitContext):
        pass

    # クラス定義検出時の処理
    def enterClassSpecifier(self, ctx:CPP14Parser.ClassSpecifierContext):
        self.classes.append({
            "class_ctx": ctx,
            "name": "",
            "private": {"variables": [], "functions": []},
            "public": {"variables": [], "functions": []},})
        self.access_state = "private"

    # クラス名検出時の処理
    def enterClassHeadName(self, ctx:CPP14Parser.ClassHeadNameContext):
        self.classes[-1]["name"] = ctx.getText()

    # アクセス指定子検出時の処理
    def enterAccessSpecifier(self, ctx:CPP14Parser.AccessSpecifierContext):
        self.access_state = ctx.getText()

    # メンバ宣言検出時の処理
    def enterMemberdeclaration(self, ctx:CPP14Parser.MemberdeclarationContext):
        # メンバ関数の定義の場合
        if type(ctx.getChild(1)) is CPP14Parser.MemberDeclaratorListContext:
            function_ctx = ctx
            function_head_ctx = descend(function_ctx.getChild(1))
            arg_tmps = descend(function_head_ctx.getChild(1)).getChild(1).getChild(0).getChildren()
            args = [{"type": arg.getChild(0).getText(), "name": arg.getChild(1).getText()} for arg in arg_tmps if type(arg) is CPP14Parser.ParameterDeclarationContext]
            function = {
                "function_ctx": function_ctx,
                "type": function_ctx.getChild(0).getText(),
                "name": function_head_ctx.getChild(0).getText(),
                "args": args
            }
            self.classes[-1][self.access_state]["functions"].append(function)
        # メンバ変数の定義の場合
        else:
            variable = {
                "type": ctx.getChild(0).getText(),
                "name": ctx.getChild(1).getChild(0).getChild(0).getText(),
                "value": ctx.getChild(1).getChild(0).getChild(1).getChild(1).getText(),
            }
            self.classes[-1][self.access_state]["variables"].append(variable)