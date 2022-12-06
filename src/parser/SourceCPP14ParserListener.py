"""
@file   MyCPP14ParserListener.py
@brief  C++のパース時のイベントリスナ
@author miyashita64
"""

from CPP14ParserListener import CPP14ParserListener
from CPP14Parser import CPP14Parser

def print_state(ctx, generation_diff = 0):
    target_ctx = get_ancestor(ctx, generation_diff)
    print("===============target===============")
    print(target_ctx.getText())
    print(type(target_ctx))
    if hasattr(ctx, "depth"):
        print("---children---------------")
        print([child.getText() for child in target_ctx.getChildren()])
        print([type(child) for child in target_ctx.getChildren()])
        # if target_ctx.parentCtx:
        #     print("---parent---------------")
        #     print(target_ctx.parentCtx.getText())
        #     print(type(target_ctx.parentCtx))
        #     print("---brothers---------------")
        #     print([type(bro) for bro in target_ctx.parentCtx.getChildren()])
    print()
    # print_ancestor_types(target_ctx, generation_diff)

def print_ancestor_types(ctx, generation_diff=0):
    if hasattr(ctx, "depth"):
        original_generation = ctx.depth() + generation_diff
        print(f"[{original_generation-ctx.depth()}]{type(ctx)}")
        parent = ctx.parentCtx
        while parent:
            print(f"[{original_generation-parent.depth()}]{type(parent)}")
            parent = parent.parentCtx
    print()

def get_ancestor(ctx, generation_diff=0):
    ancestor = ctx
    if hasattr(ctx, "depth"):
        target_generation = ancestor.depth() - generation_diff
        while ancestor.depth() > target_generation > 0:
            ancestor = ancestor.parentCtx
    return ancestor

def ascend(ctx):
    # 子が1つしかない間、上位ノードに移る
    current_node = ctx
    while current_node is not None and current_node.getChildCount() == 1:
        current_node = current_node.parentCtx
    return current_node

def descend(ctx):
    # 子が1つしかない間、下位ノードに移る
    current_node = ctx
    while current_node is not None and current_node.getChildCount() == 1:
        current_node = current_node.getChild(0)
    return current_node

def ascend_to_type(ctx, ctx_type):
    # 指定したコンテキストタイプでない間、上位ノードに移る
    current_node = ctx
    while type(current_node) not in ctx_type and current_node is not None:
        current_node = current_node.parentCtx
    return current_node

class MyCPP14ParserListener(CPP14ParserListener):
    def __init__(self, target_path):
        self.pre_text = ""
        self.post_text = ""
        self.target_path = target_path

    # 解析開始
    def enterTranslationUnit(self, ctx:CPP14Parser.TranslationUnitContext):
        pass