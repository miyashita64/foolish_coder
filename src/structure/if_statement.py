"""
@file   if_statement.py
@brief  if文クラス
@author miyashita64
"""

class IfStatement:
    def __init__(self, conds):
        self.conds = conds

    def get_code(self, nest:int, arg_name:str, branch:int = 0, is_last = False):
        indent = "\t" * nest
        if_statement_code = indent
        if_statement_code += "if" if branch == 0 else "else if"
        cond_expressions_code = ""
        for cond in self.conds:
            cond_expressions_code += cond.get_code(arg_name)
            if cond is not self.conds[-1]:
                cond_expressions_code += " || "
        if_statement_code += f"({cond_expressions_code})"
        if_statement_code += "{\n"
        if_statement_code += f"{indent}\treturn {self.conds[0].value};\n{indent}"
        if_statement_code += "}\n"
        return if_statement_code