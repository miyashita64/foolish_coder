"""
@file   class.py
@brief  クラスクラス
@author miyashita64
"""

from src.structure.variable import Variable
from src.structure.function import Function

class CPPClass:
    def __init__(self, class_name, file_name = "", arguments = [], variable_members = [], function_members = []):
        self.name = class_name
        self.file_name = f"{class_name}.h" if file_name == "" else file_name
        self.arguments = arguments
        self.variables = variable_members
        self.functions = function_members

    def get_code(self, nest = 0):
        indent = "\t" * nest
        code = f"{indent}class {self.name}"
        code += "{\n"
        if self.functions != []:
            code += f"{indent} public:\n"
        for function in self.functions:
            code += f"{function.get_code(nest+1)}\n"
        if self.variables != []:
            code += f"{indent} private:\n"
        for variable in self.variables:
            code += f"{indent}\t{variable.get_arg_code()};\n"
        code += indent + "};\n"
        return code