import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sales_data = pd.read_csv('sales.csv')
inventory_data = pd.read_csv('inventory.csv')
customer_data = pd.read_csv('customers.csv')
product_data = pd.read_csv('products.csv')

# Check for missing values
print(sales_data.isnull().sum())
print(inventory_data.isnull().sum())
print(customer_data.isnull().sum())
print(product_data.isnull().sum())

# Drop duplicates
sales_data.drop_duplicates(inplace=True)
inventory_data.drop_duplicates(inplace=True)
customer_data.drop_duplicates(inplace=True)
product_data.drop_duplicates(inplace=True)

# Handle missing values (you can drop, fill with mean/median/mode, or interpolate)
sales_data.ffill(inplace=True)
inventory_data.ffill(inplace=True)
customer_data.ffill(inplace=True)
product_data.ffill(inplace=True)

sales_customers = pd.merge(sales_data, customer_data, how='left', on='CustomerID')
sales_customers_products = pd.merge(sales_customers, product_data, how='left', on='ProductID')
full_data = pd.merge(sales_customers_products, inventory_data, how='left', on='ProductID')

# Inventory turnover ratio = Cost of Goods Sold / Average Inventory
inventory_turnover = full_data.groupby('ProductID').apply(
    lambda x: x['StockLevel'].sum() / ((x['ReorderPoint'].sum()) / len(x)),
    include_groups=False  # Add this argument to suppress the warning
)
inventory_turnover = inventory_turnover.sort_values(ascending=False)
print(inventory_turnover.head())

# Plot inventory turnover for top products
inventory_turnover.head(10).plot(kind='bar')
plt.title('Top 10 Products by Inventory Turnover Ratio')
plt.xlabel('Product ID')
plt.ylabel('Inventory Turnover Ratio')
plt.show()

# Products that are frequently out of stock
out_of_stock = full_data[full_data['StockLevel'] == 0]['ProductName'].value_counts()
print(out_of_stock.head())

# Calculate return rate by customer
return_rate = full_data.groupby('CustomerID').apply(
    lambda x: x['StockLevel'].sum() / x['ReorderPoint'].sum(),
    include_groups=False  # Add this argument to suppress the warning
)
return_rate = return_rate.sort_values(ascending=False)
print(return_rate.head())

# Plot return rates
return_rate.plot(kind='hist', bins=20)
plt.title('Customer Return Rate Distribution')
plt.xlabel('Return Rate')
plt.ylabel('Number of Customers')
plt.show()

# Analyzing customer feedback (assuming there's a 'feedback_score' column)
feedback_scores = full_data.groupby('CustomerID')['feedback_score'].mean()
feedback_scores = feedback_scores.sort_values(ascending=False)
print(feedback_scores.head())

# Convert sales_date to datetime
full_data['sales_date'] = pd.to_datetime(full_data['sales_date'])

# Monthly sales trend
monthly_sales = full_data.resample('M', on='sales_date')['total_sales'].sum()
monthly_sales.plot(kind='line', figsize=(10, 6))
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.show()

# Identify peak sales periods
peak_sales = full_data.groupby(full_data['sales_date'].dt.month)['total_sales'].sum()
peak_sales.plot(kind='bar')
plt.title('Sales by Month')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.show()

# Most popular products
popular_products = full_data['product_name'].value_counts().head(10)
popular_products.plot(kind='bar')
plt.title('Top 10 Most Popular Products')
plt.xlabel('Product')
plt.ylabel('Number of Sales')
plt.show()

def automate_analysis():
    pass

import schedule
import time

schedule.every().week.at("01:00").do(automate_analysis)

while True:
    schedule.run_pending()
    time.sleep(1)
