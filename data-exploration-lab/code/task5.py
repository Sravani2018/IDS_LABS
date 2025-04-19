import os
import pandas as pd
import sqlite3

import glob
import json


exploration = "exploration"
target_folder = "data"

os.makedirs(exploration, exist_ok=True)
data_path = os.path.join(exploration, "data_dictionary.csv")

def retrieve_type(value):
    if isinstance(value, (int, float)):
        return "Quantitative"
    return "Qualitative"


def get_csv_butes(csv_path):
  attributes = []
  try:
    df = pd.read_csv(csv_path, nrows=1)
    for col in df.columns:
      attributes.append([col, retrieve_type(df[col].iloc[0]), "Marketing", "csv", "campaigns", ""])
  except:
    pass
  return attributes

def get_butes(db_path):
  attributes = []
  try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor.fetchall()]
    
    for table in tables:
      df = pd.read_sql(f"SELECT * FROM {table} LIMIT 1", conn)
      for col in df.columns:
        attributes.append([col, retrieve_type(df[col].iloc[0]), "Sales", "sql", table, ""])
    
    conn.close()
  except:
    pass
  return attributes


def get_xlsx_butes(excel_pattern):
  attributes = []
  try:
    excel_files = glob.glob(excel_pattern)
    for file in excel_files:
      xls = pd.ExcelFile(file)
      fname = os.path.splitext(os.path.basename(file))[0]
      for sheet in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet, nrows=1)
        for col in df.columns:
          attributes.append([col, retrieve_type(df[col].iloc[0]), "HR", "excel", sheet, fname])
  except:
    pass
  return attributes


def get_json_butes(json_path):
    attributes = []
    try:
      with open(json_path, 'r') as file:
        data = json.load(file)
      df = pd.DataFrame(data)
      for col in df.columns:
        attributes.append([col, retrieve_type(df[col].iloc[0]), "Acquisitions", "json", "acquisitions", ""])
    except:
      pass
    return attributes


def main():
  total_butes = []
  total_butes.extend(get_butes(os.path.join(target_folder, "sales.db")))
  total_butes.extend(get_csv_butes(os.path.join(target_folder, "campaigns.csv")))
  total_butes.extend(get_json_butes(os.path.join(target_folder, "acquisitions.json")))
  total_butes.extend(get_xlsx_butes(os.path.join(target_folder, "*.xlsx")))
  
  df = pd.DataFrame(total_butes, columns=["attribute_name", "type", "department", "source_type", "attribute_source", "attribute_sub_source"])
  df.sort_values(by=["attribute_name", "attribute_source", "attribute_sub_source"], inplace=True)
  df.to_csv(data_path, index=False)
  print("Data dictionary created successfully.")

if _name_ == "_main_":
  main()