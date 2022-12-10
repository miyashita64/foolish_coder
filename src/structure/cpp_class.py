"""
@file   class.py
@brief  クラスクラス
@author miyashita64
"""

from src.structure.variable import Variable
from src.structure.function import Function

class CPPClass:
    def __init__(self, class_name, header_file_name = "", source_file_name = "", arguments = [], variable_members = [], function_members = []):
        self.name = class_name
        self.header_file_name = f"{class_name}.h" if header_file_name == "" else header_file_name
        self.source_file_name = f"{class_name}.cpp" if source_file_name == "" else source_file_name
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

    def get_header_code(self, nest = 0):
        indent = "\t" * nest
        guard_name = self.get_guard_name()
        code = f"#ifndef {guard_name}\n"
        code += f"#define {guard_name}\n\n"
        code += f"{indent}class {self.name}"
        code += "{\n"
        if self.functions != []:
            code += f"{indent} public:\n"
        for function in self.functions:
            code += f"{function.get_header_code(nest+1)};\n"
        if self.variables != []:
            code += f"{indent} private:\n"
        for variable in self.variables:
            code += f"{indent}\t{variable.get_arg_code()};\n"
        code += indent + "};\n\n"
        code += "#endif"
        return code
    
    def get_source_code(self, nest = 0):
        indent = "\t" * nest
        code = f"#include \"{self.header_file_name}\"\n\n"
        for function in self.functions:
            code += f"{function.get_source_code(nest)}\n"
        return code

    def get_guard_name(self):
        name = self.name
        result = name[0]
        for char in name[1:]:
            if char.isupper():
                result += "_"
            result += char.upper()
        result += "_H"
        return result