import os
import json
import re
from collections import Counter
# from genson import SchemaBuilder

def print_json_schema(file):
  if not os.path.exists(file):
    print("Invalid filename provided")
    return
  try:
    fname = os.path.basename(file)
    fname = re.sub(".json", '', fname)
    with open(file, 'r') as file:
      data = json.load(file)
    keys = set()
    for d in data:
      for key in d:
        keys.add(key)
    keys = list(keys)
    keys.sort()
    print(f"{fname}: {', '.join(keys)}")
        

  except FileNotFoundError:
    # print(f"Error: File not found at '{file}'")
    print("Invalid filename provided")
    exit()
  except json.JSONDecodeError:
    # print(f"Error: Invalid JSON format in '{file}'")
    print("Invalid filename provided")
    exit()

  # builder = SchemaBuilder()
  # builder.add_object(data)
  # json_schema = builder.to_schema()

  # print(json.dumps(json_schema, indent=2))

# def helper_func(data, key_counts):
  # if isinstance(data, dict):
    # for key, value in data.items():
    #   key_counts[key] += 1
      # helper_func(value, key_counts)
  # elif isinstance(data, list):
  # for item in data:
  #   helper_func(item, key_counts)

def helper_func(data, key_counts):
  for d in data:
    for key in d:
      key_counts[key] += 1
  # return key_counts


def analyze_json(fpath):
  if not os.path.exists(fpath):
    print("Invalid filename provided")
    return
  try:
    with open(fpath, 'r') as file:
      data = json.load(file)
    if not data:
      print("empty json")
      return
    # key_counts = {}
    key_counts = Counter()
    helper_func(data, key_counts)
    keys = sorted([[key, value] for key, value in key_counts.items()])
    for key in keys:
      print(f"{key[0]}: {key[1]}")

      
  except FileNotFoundError:
    # print(f"Error: The file {fpath} was not found.")
    print("Invalid filename provided")
  except json.JSONDecodeError:
    # print(f"Error: Could not decode JSON from {fpath}. Check file content.")
    print("Invalid filename provided")
  except Exception as e:
    # print(f"An unexpected error occurred: {e}")
    print("Invalid filename provided")


# list_excel_files("../data")
# print_excel_schema('../data/Employee_Data_4.xlsx')


