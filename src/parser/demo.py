import logging.config
from pprint import pformat

from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from CPP14Lexer import CPP14Lexer
from CPP14Parser import CPP14Parser
# from MyCPP14ParserListener import MyCPP14ParserListener
from TestCaseCPP14ParserListener import MyCPP14ParserListener


class AstProcessor:

    def __init__(self, listener):
        self.listener = listener

    def execute(self, input_source):
        parser = CPP14Parser(CommonTokenStream(CPP14Lexer(FileStream(input_source, encoding="utf-8"))))
        walker = ParseTreeWalker()
        walker.walk(self.listener, parser.translationUnit())
        return self.listener.testcases

if __name__ == "__main__":
    target_path = "FeeCalculatorTest.cpp"
    testcases = AstProcessor(MyCPP14ParserListener(target_path)).execute(target_path)
    print(testcases)