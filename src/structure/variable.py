"""
@file   variable.py
@brief  変数クラス
@author miyashita64
"""

class Variable:
    def __init__(self, variable_name, value, data_type = "auto"):
        self.name = variable_name
        self.value = value
        self.type = data_type

    def assign(self, value, is_init=False):
        self.value = value
        code = f"{self.type} " if is_init else ""
        code += f"{self.name} = {value};"
        return code

    def get_arg_code(self, default_value=None):
        code = f"{self.type} {self.name}"
        if default_value != None:
            code += f"={default_value}"
        return code

    def cast(self, value_type = "auto"):
        if value_type == "auto":
            self.auto_cast()
        elif value_type == "int":
            self.int(value)
            self.data_type = "int"
        elif value_type in ["double", "float"]:
            self.float(value)
            self.data_type = "value_type"
        else:
            self.str(value)
            self.data_type = "char*"

    def auto_cast(self):
        target = str(self.value)
        has_only_period = False
        if target.count("-") == 1 and target[0] == "-":
            target = target[1:]
        if target.count(".") == 1:
            has_only_period = True
            target = target.replace(".", "")

        if target.isdecimal():
            if has_only_period:
                self.value = float(self.value)
                self.data_type = "float"
            else:
                self.value = int(self.value)
                self.data_type = "int"
        self.value = str(self.value)
        self.data_type = "char*"