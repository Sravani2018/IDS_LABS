import os
import pandas as pd
import numpy as np
import json
import sqlite3
import glob
import re
import datetime

# collect data from all the excel files
def list_files(dir_path, engine):
  if not os.path.exists(dir_path):
    print("Invalid input")
    return
  try:
    # print("valid path provided")
    if dir_path.endswith("data"):
      file_paths = glob.glob(f"{dir_path}/*.xlsx")
    # file_names = [os.path.basename(filepath) for filepath in file_paths]
      for file_path in file_paths:
        # print(file_path)
        read_excel(file_path, engine)
    elif dir_path.endswith(".json"):
      analyze_json(dir_path, engine)
    elif dir_path.endswith(".csv"):
      read_csv(dir_path, engine)
    else:
      # print("trying")
      connect_db(dir_path, engine)
      
  except FileNotFoundError:
    print("Invalid filename provided")
    exit()



def data_frames(table_name, table_dict, engine):
  df = pd.DataFrame(table_dict)
  # df = df.applymap(lambda x: pd.to_datetime(x).strftime('%Y-%m-%d') if isinstance(x, str) and is_date(x) else x)
  for col in df.columns:
    if 'date' in col:
    # if pd.api.types.is_datetime64_any_dtype(new_df[col]):
      df[col] = pd.to_datetime(df[col])
      df[col] = df[col].dt.strftime('%Y-%m-%d')
  # print(df.shape)
  # print(df)
  try:
    # existing_df = pd.read_sql_table(table_name, con = engine)
    # if not existing_df.empty:
    #   df = pd.concat([df, existing_df], axis=1, ignore_index=False)
    
    df.to_sql(table_name, con = engine, if_exists='replace', index=False)
  except:
    df.to_sql(table_name, con = engine, if_exists='replace', index=False)
  # print(df.shape)
  



def read_excel(excel_path, engine):
  # print("entred the excel function")
  try:
    dfs = pd.read_excel(excel_path, sheet_name=None)
    sheets = list(dfs.keys())
    # tables.sort()
    excel_data = {}
    for sheet in sheets:
      df = dfs[sheet]
      # df = df.applymap(lambda x: pd.to_datetime(x).strftime('%Y-%m-%d') if isinstance(x, str) and is_date(x) else x)
  
      if sheet.title() in excel_data:
        excel_data[sheet.title()] = pd.concat([excel_data[sheet.title()], df], ignore_index=True)
      else:
        excel_data[sheet.title()] = df
    for sheet, df in excel_data.items():
      data_frames(sheet, df, engine)
  except FileNotFoundError:
    print("FileNotFoundError")
    exit()




def analyze_json(json_path, engine):
  # print("entered the json function")
  try:
    # fname = os.path.basename(json_path)
    # fname = re.sub(".json", '', fname)
    # print(fname)
    
    with open(json_path, 'r') as file:
      data = json.load(file)
    # print(data)
    if not data:
      print("empty json")
      return
    json_table = pd.json_normalize(data)
    data_frames("Acquisitions", json_table, engine)
          
  except FileNotFoundError:
    # print(f"Error: The file {fpath} was not found.")
    print("the FileNotFoundError")
  except json.JSONDecodeError:
    # print(f"Error: Could not decode JSON from {fpath}. Check file content.")
    print("the JSONDecodeError")
  except Exception as e:
    # print(f"An unexpected error occurred: {e}")
    print("the ExceptionError")


def read_csv(fpath, engine):
  # print("entered the csv function")
  try:
    # fname = os.path.basename(fpath)
    # fname = re.sub(".csv", '', fname)
    data = pd.read_csv(fpath)
    data_frames("Campaigns", data, engine)

  except FileNotFoundError:
    print("Invalid filename provided")
    exit()


def connect_db(db_path, engine):
  db_conn = sqlite3.connect(db_path)
  # print("connected to sales successfully")
  try:
    cursor = db_conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table';")
    tables = [row[0] for row in cursor.fetchall()]
    
    for table in tables:
      sql_query = f"SELECT * FROM {table}"
      df = pd.read_sql_query(sql_query, db_conn)

      # df = pd.read_sql_table(table, db_conn, engine)
      data_frames(table, df, engine)
  
  except sqlite3.Error as e:
    print(f"Invalid filename provided")

