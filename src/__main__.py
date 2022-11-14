"""
@file   __main__.py
@brief  FoolishCoderのメインタスク
@author miyashita64
"""

from src.file_reader import FileReader

print("\nFoolish coding...\n")

FileReader.read_latest_build_log()

print("\nComplete!!\n")
