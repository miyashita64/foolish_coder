"""
@file   cond_expression.py
@brief  条件式クラス
@author miyashita64
"""

class CondExpression:
    def __init__(self, value, min, max):
        self.value = value
        self.min = min
        self.max = max

    def get_code(self, nest:int, arg_name:str, branch:int = 0, is_last = False):
        indent = "\t" * nest
        cond_expression_code = indent
        cond_expression_code += "if" if branch == 0 else "else if"
        if type(min) == str or self.min == self.max:
            cond_expression_code += f"({arg_name} == {self.min})"
            # if branch == 0 and not is_last:
            #     cond_expression_code += f"({arg_name} <= {self.min})"
            # elif branch > 0 and is_last:
            #     cond_expression_code += f"({self.max} <= {arg_name})"
            # else:
            #     cond_expression_code += f"({arg_name} == {self.min})"
        else:
            cond_expression_code += f"({self.min} <= {arg_name} && {arg_name} <= {self.max})"
        cond_expression_code += "{\n"
        cond_expression_code += f"{indent}\treturn {self.value};\n{indent}"
        cond_expression_code += "}\n"
        return cond_expression_code