import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
import seaborn as sns


def sales_trend(db_path, conn):
    
  query = """
    SELECT strftime('%m', datetime(sold_on, 'unixepoch')) AS month, 
    SUM(selling_price) AS total_sales
    FROM Sales
    GROUP BY month
    ORDER BY month;
  """
    
  df = pd.read_sql(query, conn)
    
    
  plt.figure(figsize=(10, 6))
  plt.plot(df['month'], df['total_sales'], marker='o', linestyle='-', color='blue')
    
  plt.title('Sales Trend - Total Sales by Month (Combined Across Years)')
  plt.xlabel('Month')
  plt.ylabel('Total Sales ($)')
  plt.xticks(ticks=[str(i).zfill(2) for i in range(1, 13)], labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45)
  plt.grid(True)
    
  save_path = '../images/sales_trend.png'
  plt.tight_layout()
  plt.savefig(save_path)



def product_performance(db_path, conn):
    
  query = """
    SELECT pd.name, SUM(s.selling_price) AS total_sales
    FROM Sales s
    JOIN Productdetail pd ON s.product_detail_id = pd.id
    GROUP BY pd.name
    ORDER BY total_sales DESC
    LIMIT 10;
  """
    
  df = pd.read_sql(query, conn)
        
  plt.figure(figsize=(10, 6))
  plt.barh(df['name'], df['total_sales'], color='green')
  plt.title('Top 10 Performing Products by Sales')
  plt.xlabel('Total Sales ($)')
  plt.ylabel('Product Name')
  plt.gca().invert_yaxis()  
  plt.tight_layout()
    

  save_path = '../images/product_performance.png'
  plt.savefig(save_path)

def regional_performance(db_path, conn):
  query = """
  SELECT rl.store_name, SUM(s.selling_price) AS total_sales
  FROM Sales s
  JOIN RetailLocation rl ON s.retail_location_id = rl.id
  GROUP BY rl.store_name
  ORDER BY total_sales DESC;
  """
    
  df = pd.read_sql(query, conn)
    
  plt.figure(figsize=(10, 6))
  plt.bar(df['store_name'], df['total_sales'], color='blue')
  plt.title('Total Sales by Retail Location')
  plt.xlabel('Retail Location')
  plt.ylabel('Total Sales ($)')
  plt.xticks(rotation=45, ha='right')
  plt.tight_layout()   

  save_path = '../images/regional_performance.png'
  plt.savefig(save_path)

def salary_distribution(db_path, conn):
  query = """
  SELECT 
    e.name as employee_name,
    s.salary
    FROM Salary s
    JOIN Employees e ON e.id = s.employee_id
    WHERE s.year = (
      SELECT MAX(year) 
      FROM Salary 
      WHERE employee_id = s.employee_id
    )
  """

  salary_data = pd.read_sql(query, conn)
  
  # Convert 'salary' column to numeric, handling errors 
  salary_data['salary'] = pd.to_numeric(salary_data['salary'], errors='coerce')
  
  # Drop rows with invalid salary values (introduced by 'coerce')
  salary_data = salary_data.dropna(subset=['salary'])

  plt.figure(figsize=(12, 6))
    
  sns.histplot(data=salary_data, x='salary', bins=50, edgecolor='black')
  sns.kdeplot(data=salary_data, x='salary', color='red', linewidth=2)

  mean_salary = salary_data['salary'].mean()
  median_salary = salary_data['salary'].median()
    
  plt.axvline(mean_salary, color='red', linestyle='--', label=f'Mean: ${mean_salary:,.0f}')
  plt.axvline(median_salary, color='green', linestyle='--', label=f'Median: ${median_salary:,.0f}')
    
  plt.title('Employee Salary Distribution')
  plt.xlabel('Salary ($)')
  plt.ylabel('Number of Employees')
  plt.legend()
    
  plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${format(int(x), ",")}'))
  plt.tight_layout()

  save_path = '../images/salary_distribution.png'
  plt.tight_layout()
  plt.savefig(save_path)


def campaign_effectiveness(db_path, conn):
    
  query = """
    SELECT pd.name, 
      SUM(c.expenditure) AS total_campaign_spending,
      SUM(s.selling_price) AS total_revenue_generated
    FROM Campaigns c
    JOIN Productdetail pd ON c.target_product_id = pd.id
    JOIN Sales s ON pd.id = s.product_detail_id
    GROUP BY pd.name;
    """
    
  df = pd.read_sql(query, conn)
    
  plt.figure(figsize=(10, 6))
  plt.scatter(df['total_campaign_spending'], df['total_revenue_generated'], color='orange', edgecolor='black')
    
  plt.title('Campaign Effectiveness: Spending vs Revenue')
  plt.xlabel('Total Campaign Spending ($)')
  plt.ylabel('Total Revenue Generated ($)')
  plt.grid(True)
    
  save_path = '../images/campaign_effectiveness.png'
  plt.tight_layout()
  plt.savefig(save_path)
  
def main():

  db_path = '../data/output.db'
  conn = sqlite3.connect(db_path)

  sales_trend(db_path, conn)
  product_performance(db_path, conn)
  regional_performance(db_path, conn)
  salary_distribution(db_path, conn)
  campaign_effectiveness(db_path, conn)


  conn.close()

if __name__ == "__main__":
  main()