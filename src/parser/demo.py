import logging.config
from pprint import pformat

from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from CPP14Lexer import CPP14Lexer
from CPP14Parser import CPP14Parser
from CPP14ParserListener import CPP14ParserListener



class AstProcessor:

    def __init__(self, listener):
        self.listener = listener

    def execute(self, input_source):
        parser = CPP14Parser(CommonTokenStream(CPP14Lexer(FileStream(input_source, encoding="utf-8"))))
        walker = ParseTreeWalker()
        walker.walk(self.listener, parser.translationUnit())

if __name__ == "__main__":
    AstProcessor(CPP14ParserListener()).execute("target.cpp")