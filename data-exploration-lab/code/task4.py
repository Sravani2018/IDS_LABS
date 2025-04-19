import os
import pandas as pd
import re



def print_csv_schema(fpath):
  if not os.path.exists(fpath):
    print("Invalid filename provided")
    return
  try:
    fname = os.path.basename(fpath)
    fname = re.sub(".csv", '', fname)
    sheet = pd.read_csv(fpath)
    cols = list(sheet.keys())
    if not cols:
      print("!!tables are empty!!")
      return
    cols.sort()
    print(f"{fname}: {', '.join(cols)}")
    
  except FileNotFoundError:
    print("Invalid filename provided")
    exit()