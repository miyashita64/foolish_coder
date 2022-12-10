"""
@file   file.py
@brief  ファイルクラス
@author miyashita64
"""

class File:
    def __init__(self, file_name, dir_path="results/"):
        self.name = file_name
        self.path = f"{dir_path}{file_name}"

    def read(self):
        print(f"Loading file {self.path} ... ", end="")
        try:
            target_file = open(self.path, "r")
            text = target_file.read()
            target_file.close()
            print("Succeed!!")
        except:
            text = ""
            print("Failed.")
        return text

    def write(self, text):
        print(f"Writeing file {self.path} ... ", end="")
        try:
            target_file = open(self.path, "w")
            target_file.write(text)
            target_file.close()
            print("Succeed!!")
        except:
            print("Failed.")