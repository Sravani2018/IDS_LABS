import os
import glob
# import sqlite3
import pandas as pd
import re

def print_excel_schema(file):
  if not os.path.exists(file):
    print("Invalid filename provided")
    return
  try:
    dfs = pd.read_excel(file, sheet_name=None)
    tables = list(dfs.keys())
    if not tables:
      print("!!tables are empty!!")
      return
    tables.sort()
    for table in tables:
      cols = [col for col in dfs[table].columns]
      cols.sort()
      print(f"{table}: {', '.join(cols)}")
  
  except FileNotFoundError:
    print("Invalid filename provided")
    exit()


def list_excel_files(dir_path):
  if not os.path.exists(dir_path):
    print("Invalid filename provided")
    return
  try:
    filenames = [os.path.basename(x) for x in glob.glob(f"{dir_path}/*.xlsx")]
    # filenames = [re.sub("data/", '', file) for file in files]
    filenames.sort()
    for filename in filenames:
      print(filename)
    # for file in files:
    #   print_excel_schema(file)
    return filenames
  except FileNotFoundError:
    print("Invalid filename provided")
    exit()


# list_excel_files("../data")
# print_excel_schema('../data/Employee_Data_4.xlsx')


