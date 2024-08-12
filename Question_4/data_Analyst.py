import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Dataset.csv')
print(data.isnull().sum())

data.drop_duplicates(inplace=True)
data.ffill(inplace=True)
data.columns = [col.strip() for col in data.columns]

purchase_frequency = data['Customer ID'].value_counts()
sns.histplot(purchase_frequency, kde=False)
plt.title('Purchase Frequency Distribution')
plt.xlabel('Number of Purchases')
plt.ylabel('Number of Customers')
plt.show()

# Analyzing sales by country
sales_by_country = data['Country'].value_counts()
sns.barplot(x=sales_by_country.values, y=sales_by_country.index)
plt.title('Sales by Country')
plt.xlabel('Number of Sales')
plt.ylabel('Country')
plt.show()

# Top selling products || Product Performance Analysis
top_products = data['Description'].value_counts().head(10)
sns.barplot(x=top_products.values, y=top_products.index)
plt.title('Top Selling Products')
plt.xlabel('Number of Sales')
plt.ylabel('Product')
plt.show()

# Convert InvoiceDate to datetime | Sales Trend Analysis
data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])

# Monthly sales trend
monthly_sales = data.resample('ME', on='InvoiceDate')['Invoice'].count()
ax = monthly_sales.plot(kind='line', figsize=(10, 6))
ax.set_xlim(pd.Timestamp('2023-01-01'), pd.Timestamp('2024-01-01'))  # Example: expanding to a full year
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Number of Orders')
plt.show()


# Yearly sales trend
yearly_sales = data.resample('YE', on='InvoiceDate')['Invoice'].count()
yearly_sales.plot(kind='line', figsize=(10, 6))
plt.title('Yearly Sales Trend')
plt.xlabel('Year')
plt.ylabel('Number of Orders')
plt.show()

