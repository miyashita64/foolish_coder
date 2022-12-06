"""
@file   MyCPP14ParserListener.py
@brief  C++のパース時のイベントリスナ
@author miyashita64
"""

from CPP14ParserListener import CPP14ParserListener
from CPP14Parser import CPP14Parser

def pcs(ctx):
    print("[", end="")
    print(type(ctx), end="")
    print(print_children(ctx), end="")
    print("]")

def print_children(ctx):
    if ctx.getChildCount() == 0 and ctx:
        print(f"{ctx.getText()}", end="  ")
        return
    for key in range(ctx.getChildCount()):
        print_children(ctx.getChild(key))

def print_state(ctx, generation_diff = 0):
    target_ctx = get_ancestor(ctx, generation_diff)
    print("===target===============")
    print(target_ctx.getText())
    print(type(target_ctx))
    print("---children---------------")
    print([child.getText() for child in target_ctx.getChildren()])
    print([type(child) for child in target_ctx.getChildren()])
    if target_ctx.parentCtx:
        print("---parent---------------")
        print(target_ctx.parentCtx.getText())
        print(type(target_ctx.parentCtx))
        print("---brothers---------------")
        print([type(bro) for bro in target_ctx.parentCtx.getChildren()])
    print()
    print_ancestor_types(target_ctx, generation_diff)

def print_ancestor_types(ctx, generation_diff=0):
    original_generation = ctx.depth() + generation_diff
    print(f"[{original_generation-ctx.depth()}]{type(ctx)}")
    parent = ctx.parentCtx
    while parent:
        print(f"[{original_generation-parent.depth()}]{type(parent)}")
        parent = parent.parentCtx

def get_ancestor(ctx, generation_diff = 0):
    ancestor = ctx
    target_generation = ancestor.depth() - generation_diff
    while ancestor.depth() > target_generation > 0:
        ancestor = ancestor.parentCtx
    return ancestor

class MyCPP14ParserListener(CPP14ParserListener):
    def __init__(self, target_path):
        self.pre_text = ""
        self.post_text = ""
        self.target_path = target_path

    # 解析開始
    def enterTranslationUnit(self, ctx:CPP14Parser.TranslationUnitContext):
        pass

    # 条件式
    def enterConditionalExpression(self, ctx:CPP14Parser.ConditionalExpressionContext):
        pass

    # 文
    def enterStatement(self, ctx:CPP14Parser.StatementContext):
        # print_state(get_ancestor(ctx, 0))
        pass

    def enterBlockDeclaration(self, ctx:CPP14Parser.BlockDeclarationContext):
        # print_state(get_ancestor(ctx, 0))
        pass

    # リテラル
    def enterLiteral(self, ctx:CPP14Parser.LiteralContext):
        # print_state(ctx, 31)
        # target = get_ancestor(ctx, 19)
        pass

    def enterFunctionDefinition(self, ctx:CPP14Parser.FunctionDefinitionContext):
        print_state(ctx,1)
        pass

    def enterFunctionBody(self, ctx:CPP14Parser.FunctionBodyContext):
        pass

    def enterFunctionSpecifier(self, ctx:CPP14Parser.FunctionSpecifierContext):
        pass