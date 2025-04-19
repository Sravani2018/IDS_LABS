import sqlite3
import pandas as pd

import task6 as six

from sqlalchemy import create_engine, inspect

from sqlalchemy import text


def main():
  engine = create_engine('sqlite:///../data/output.db', echo=False)
  # conn = sqlite3.connect('../data/output.db')
  # print("Opened SQLite database successfully.")
  with engine.begin() as conn:
    six.list_files("../data", conn)
    six.list_files("../data/acquisitions.json", conn)
    six.list_files("../data/campaigns.csv", conn)
    six.list_files("../data/sales.db", conn)
    # inspector = inspect(conn)
    # table_names = inspector.get_table_names()
    # print(table_names)
    # for table_name in table_names:
    #   df = pd.read_sql_table(table_name, conn)
    #   print(f"Table: {table_name}")
    #   print(df)
    #   print("-" * 20)

    
if __name__ == "__main__":
    main()