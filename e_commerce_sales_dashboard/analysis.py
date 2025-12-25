import pandas as pd
import matplotlib.pyplot as plt
import glob

"""
Analyse random e-commerce sales.
1) Concat csv files per month into one big dataframe
2) Clean up data
3) Add new columns needed for a) clarity and b) later analysis
4) Analysis: Find best city, hour etc
5) Create some basic charts
"""


files = glob.glob("./sales_data/*.csv")

df = pd.concat(
    (pd.read_csv(f) for f in files),
    ignore_index=True
)

""" move rows so January is top and December is bottom. necessary because files saved in
 alphabetic order, not numeric order, i.e. sales_month_10 comes before sales_month 2.
 Without sorting, months would be 1,10,11,12,2,3,4,...,9 instead of 1,2,3,...,11,12."""
df = df.sort_values("Order Date")
df = df.reset_index(drop=True)  # Reset index numbers (0 to 11999) to match the new order

# add new column "Sales_Volume"
df["Sales_Volume"] = df["Quantity Ordered"] * df["Price Each"]

# add new column month and hour
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Month"] = df["Order Date"].dt.month
df["Hour"] = df["Order Date"].dt.hour

# find best month
results_month = df.groupby('Month')['Sales_Volume'].sum()
print("\n--- Best Month for Sales ---")
print(results_month.sort_values(ascending=False).head(1))

# add new column city
def get_city(address):
    return address.split(',')[1].strip()
df['City'] = df['Purchase Address'].apply(lambda x: get_city(x))

# find city who ordered the most products (quantity, not highest revenue)
ordered_products_per_city = df.groupby("City")["Quantity Ordered"].sum()
print("\n--- City where most products were ordered ---")
print(ordered_products_per_city.sort_values(ascending=False).head(1))

# find best time of day
results_hour = df.groupby('Hour').count()['Order ID']
print("\n--- Busiest Time of Day (Hour) ---")
print(results_hour.sort_values(ascending=False).head(1))


# ---------------- PLOTS ----------------------------------

# figure with custom layout (2 rows, 2 columns)
# top chart spans both columns
fig = plt.figure(figsize=(14, 10))
grid = plt.GridSpec(2, 2, hspace=0.4, wspace=0.3)

# --- Chart 1: Line Graph of Sales over Time (Top, spanning width) ---
ax1 = fig.add_subplot(grid[0, :]) # Row 0, All columns
months = range(1, 13)
ax1.plot(months, results_month, marker='o', color='b')
ax1.set_title('Total Sales by Month')
ax1.set_xticks(months)
ax1.set_xlabel('Month')
ax1.set_ylabel('Sales (USD)')
ax1.grid(True)

# --- Chart 2: Bar Graph of Sales by City (Bottom Left) ---
ax2 = fig.add_subplot(grid[1, 0]) # Row 1, Col 0
cities = [city for city, df in df.groupby('City')]
ax2.bar(cities, ordered_products_per_city, color='g')
ax2.set_title('Quantity Ordered by City')
ax2.set_xticklabels(cities, rotation=45, ha='right', size=8)
ax2.set_ylabel('Quantity Ordered')

# --- Chart 3: Histogram of Order Prices (Bottom Right) ---
ax3 = fig.add_subplot(grid[1, 1]) # Row 1, Col 1
ax3.hist(df['Price Each'], bins=20, color='orange', edgecolor='black')
ax3.set_title('Distribution of Product Prices')
ax3.set_xlabel('Price')
ax3.set_ylabel('Frequency')

plt.suptitle('E-Commerce Sales Dashboard', fontsize=16)
plt.show()
