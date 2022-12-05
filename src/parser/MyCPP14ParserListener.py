from CPP14ParserListener import CPP14ParserListener
from CPP14Parser import CPP14Parser

class MyCPP14ParserListener(CPP14ParserListener):
    def __init__(self):
        self.tree = []

    # Enter a parse tree produced by CPP14Parser#translationUnit.
    def enterTranslationUnit(self, ctx:CPP14Parser.TranslationUnitContext):
        print(ctx.getText())
        pass