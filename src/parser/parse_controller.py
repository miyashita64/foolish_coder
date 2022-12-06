"""
@file   parse_controller.py
@brief  構文解析の仲介クラス
@author miyashita64
"""

from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from src.parser.CPP14Lexer import CPP14Lexer
from src.parser.CPP14Parser import CPP14Parser
from src.parser.TestCaseCPP14ParserListener import TestCaseCPP14ParserListener


class ParseController:

    @staticmethod
    def parse_testcase(test_code_path):
        listener = TestCaseCPP14ParserListener(test_code_path)
        parser = CPP14Parser(CommonTokenStream(CPP14Lexer(FileStream(test_code_path, encoding="utf-8"))))
        walker = ParseTreeWalker()
        walker.walk(listener, parser.translationUnit())
        return listener.testcases