import sqlite3
import pandas as pd


db_path = "data/output.db"

def total_salary_bill_per_year():
  conn = sqlite3.connect(db_path)
  cursor = conn.cursor()
  query = """
    WITH LatestSalary AS (
      SELECT year, employee_id, MAX(salary) AS salary
      FROM Salary
      GROUP BY year, employee_id
    )
    SELECT year, ROUND(SUM(salary), 2)
    FROM LatestSalary
    GROUP BY year
    ORDER BY year;
  """
  cursor.execute(query)
  results = cursor.fetchall()
  for res in results:
    print(f"{res[0]} {res[1]}")
  conn.close()
    

def total_bonus_by_year():
  conn = sqlite3.connect(db_path)
  cursor = conn.cursor()
  query = """
    SELECT year, SUM(bonus)
    FROM bonus 
    GROUP BY year 
    ORDER BY year;
  """
  cursor.execute(query)
  results = cursor.fetchall()
  
  for res in results:
    print(f"{res[0]} {format(res[1], '.2f')}") 
  conn.close()


def monthly_hiring_stats():
  conn = sqlite3.connect(db_path)
  cursor = conn.cursor()
  
  query = """
    SELECT strftime('%m', date_of_joining) AS month, COUNT(*) 
    FROM Employees 
    GROUP BY month 
    ORDER BY month;
  """
  cursor.execute(query)
  results = cursor.fetchall()
  
  for res in results:
    print(f"{res[0]} {res[1]}")  
  conn.close()


def most_costly_acquisition():
  conn = sqlite3.connect(db_path)
  cursor = conn.cursor()
  query = "SELECT MAX(cost) FROM Acquisitions;"
  cursor.execute(query)
  result = cursor.fetchone()
  print(result[0])
  conn.close()

def most_costly_office_acquisition():
  conn = sqlite3.connect(db_path)
  cursor = conn.cursor()
  query = "SELECT MAX(cost) FROM Acquisitions WHERE type='Office';"
  cursor.execute(query)
  result = cursor.fetchone()
  print(result[0])
  conn.close()


def product_wise_campaign_spending():
  try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = '''
    SELECT target_product_id, SUM(expenditure) AS total_expenditure
    FROM campaigns 
    GROUP BY target_product_id
    ORDER BY total_expenditure DESC;
    '''

    cursor.execute(query)
    results = cursor.fetchall()

    for res in results:
      print(f"{res[0]} {res[1]:.2f}")

  except sqlite3.Error as e:
    print(f"Database error: {e}")
  
  finally:
    if cursor:
      cursor.close()
    if conn:
      conn.close()


def top_5_products_by_sales():
  try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = '''
    SELECT pd.name
    FROM ProductDetail pd
    JOIN Sales s ON pd.id = s.product_detail_id
    GROUP BY pd.id, pd.name
    ORDER BY SUM(s.selling_price) DESC
    LIMIT 5;
    '''

    cursor.execute(query)
    results = cursor.fetchall()

    for res in results:
      print(res[0])

  except sqlite3.Error as e:
    print(f"Database error: {e}")
  
  finally:
    if cursor:
      cursor.close()
    if conn:
      conn.close()


def top_5_retail_stores_by_sales():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query = """
        SELECT rl.store_name
        FROM RetailLocation rl
        JOIN Sales s ON rl.id = s.retail_location_id
        GROUP BY rl.id
        ORDER BY SUM(s.selling_price) DESC
        LIMIT 5;

    """
    cursor.execute(query)
    results = cursor.fetchall()
    for res in results:
        print(res[0])
    conn.close()