"""
@file   parse_controller.py
@brief  構文解析の仲介クラス
@author miyashita64
"""

from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from src.parser.CPP14Lexer import CPP14Lexer
from src.parser.CPP14Parser import CPP14Parser
from src.parser.TestCaseCPP14ParserListener import TestCaseCPP14ParserListener
from src.parser.SourceCPP14ParserListener import SourceCPP14ParserListener


class ParseController:

    @staticmethod
    def parse_testcase(test_code_file_name, test_code_dir_path):
        """テストコードからテストケースを抽出する."""
        test_code_path = test_code_dir_path + test_code_file_name
        print(f"Parsing test code {test_code_path} ... ", end="")
        try:
            listener = TestCaseCPP14ParserListener(test_code_path)
            parser = CPP14Parser(CommonTokenStream(CPP14Lexer(FileStream(test_code_path, encoding="utf-8"))))
            walker = ParseTreeWalker()
            walker.walk(listener, parser.translationUnit())
            print("Succeed!")
        except:
            print("Failed.")
        return listener.testcases

    @staticmethod
    def parse_source(source_code_file_name, source_code_dir_path):
        """ソースファイルからソース情報を抽出する."""
        source_code_path = source_code_dir_path + source_code_file_name
        print(f"Parsing source code {source_code_path} ... ", end="")
        try:
            listener = SourceCPP14ParserListener(source_code_path)
            parser = CPP14Parser(CommonTokenStream(CPP14Lexer(FileStream(source_code_path, encoding="utf-8"))))
            walker = ParseTreeWalker()
            walker.walk(listener, parser.translationUnit())
            print("Succeed!")
        except:
            print("Failed.")
        return listener.classes