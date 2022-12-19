"""
@file   function.py
@brief  関数クラス
@author miyashita64
"""

from src.structure.variable import Variable
from src.structure.cond_expression import CondExpression
from src.structure.if_statement import IfStatement

class Function:
    def __init__(self, function_name, owner = "", return_type = "void", arguments = [], statements = []):
        self.name = function_name
        self.owner = owner
        self.type = return_type
        self.arguments = arguments
        self.statements = statements

    def get_header_code(self, nest = 0):
        indent = "\t" * nest
        code = f"{indent}{self.type} {self.name}({self.get_args_code()})"
        return code

    def get_source_code(self, nest = 0):
        indent = "\t" * nest
        code = f"{indent}{self.type} {self.owner}::{self.name}({self.get_args_code()})"
        code += "{\n"
        branch = 0
        for statement in self.statements:
            if type(statement) is IfStatement:
                if statement is self.statements[-1]:
                    code += statement.get_code(nest+1, self.arguments[0].name, branch, is_last = True)
                else:
                    code += statement.get_code(nest+1, self.arguments[0].name, branch)
                branch += 1
        code += indent + "}\n"
        return code

    def get_args_code(self):
        code = ""
        for arg in self.arguments:
            code += f"{arg.get_arg_code()}, "
        return code[:-2]
