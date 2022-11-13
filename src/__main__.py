import sys
import os
 
# sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/bindings/python')
from clang.cindex import Config, Index
 
# Clangの設定
Config.set_library_path(r'../download/')
 
# パース
translation_unit = Index.create().parse('test.cpp')
 
# 出力
def dump(cursor, indent=0):
	text = cursor.kind.name
	print('\t' * indent + text)
	
	for child in cursor.get_children():
		dump(child, indent+1)
 
dump(translation_unit.cursor)