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

    def get_code(self, arg_name):
        cond_expression_code = ""
        if type(min) == str or self.min == self.max:
            cond_expression_code += f"{arg_name} == {self.min}"
        else:
            cond_expression_code += f"({self.min} <= {arg_name} && {arg_name} <= {self.max})"
        return cond_expression_code