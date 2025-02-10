import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# Load CSV File (Update path if needed)
file_path = "C:\\Users\\NISHANT\\Downloads\\flipkart_sales_analysis\\flipkart_sales_data.csv"
df = pd.read_csv(file_path)

# Convert 'Order Date' to datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'])

# 📊 Total Sales
total_sales = df['Sales'].sum()
print(f"💰 Total Sales: ${total_sales:,.2f}")

# 📅 Sales Trend Over Time
sales_trend = df.groupby('Order Date')['Sales'].sum().reset_index()
fig = px.line(sales_trend, x='Order Date', y='Sales', title="Sales Over Time", markers=True)
fig.show()

# 📦 Category-wise Sales
category_sales = df.groupby('Category')['Sales'].sum().reset_index()
fig = px.bar(category_sales, x='Category', y='Sales', title="Sales by Category", color='Category')
fig.show()

# 🌍 City-wise Sales
city_sales = df.groupby('City')['Sales'].sum().reset_index()
fig = px.pie(city_sales, names='City', values='Sales', title="Sales by City")
fig.show()

# 💳 Sales by Payment Method
payment_sales = df.groupby('Payment Method')['Sales'].sum().reset_index()
fig = px.bar(payment_sales, x='Payment Method', y='Sales', title="Sales by Payment Method", color='Payment Method')
fig.show()
