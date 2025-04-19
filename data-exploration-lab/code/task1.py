import os
import sqlite3
import pandas as pd


# conn = sqlite3.connect(db_path)
# print("Connected to the database successfully")


def print_db_schema(db_file):
  if not os.path.exists(db_file):
    print(f"Invalid filename provided")
    return
  
  else:
    try:
      conn = sqlite3.connect(db_file)
      cursor = conn.cursor()
      cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table';")
      tables = sorted([row[0] for row in cursor.fetchall()])
      if not tables:
        return
      for table in tables:
        schema = f"{table}:"
        cursor.execute(f"PRAGMA table_info({table});")
        columns = cursor.fetchall()
        column_list = sorted([f" {column[1]}" for column in columns])
        print(schema + ','.join(column_list))
      conn.close()
  
    except sqlite3.Error as e:
      print(f"Invalid filename provided")