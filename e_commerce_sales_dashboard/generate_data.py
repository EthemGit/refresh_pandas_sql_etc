import pandas as pd
import numpy as np
import os
import random
from datetime import datetime, timedelta

# Create directory
os.makedirs('sales_data', exist_ok=True)

# Configuration
products = {
    'iPhone': 700, 'Google Phone': 600, 'Macbook Pro Laptop': 1700,
    'ThinkPad Laptop': 1000, 'USB-C Charging Cable': 12, 
    'Lightning Charging Cable': 15, 'Wired Headphones': 12,
    'Bose SoundSport Headphones': 100, 'AAA Batteries (4-pack)': 3,
    'AA Batteries (4-pack)': 4
}
cities = ['New York, NY', 'Los Angeles, CA', 'San Francisco, CA', 'Boston, MA', 
          'Atlanta, GA', 'Dallas, TX', 'Seattle, WA', 'Portland, OR', 'Austin, TX']
product_list = list(products.keys())
prices_list = list(products.values())

def generate_month_data(month_num):
    # Generate 1000 rows per month
    n_rows = 1000
    
    # Generate Dates
    year = 2024
    start_date = datetime(year, month_num, 1)
    # Handle lengths of months roughly
    end_date = start_date + timedelta(days=28) 
    
    dates = []
    for _ in range(n_rows):
        random_second = random.randint(0, int((end_date - start_date).total_seconds()))
        date = start_date + timedelta(seconds=random_second)
        dates.append(date.strftime("%m/%d/%Y %H:%M"))

    # Generate Products and Prices
    prods = random.choices(product_list, k=n_rows)
    prices = [products[p] for p in prods]
    
    # Generate Quantities (mostly 1, sometimes 2)
    qtys = np.random.choice([1, 2, 3], size=n_rows, p=[0.9, 0.08, 0.02])
    
    # Generate Cities
    addrs = [f"{random.randint(100, 999)} Main St, {random.choice(cities)} {random.randint(10000, 99999)}" for _ in range(n_rows)]

    df = pd.DataFrame({
        'Order ID': range(1000*month_num, 1000*month_num + n_rows),
        'Product': prods,
        'Quantity Ordered': qtys,
        'Price Each': prices,
        'Order Date': dates,
        'Purchase Address': addrs
    })
    
    return df

# Generate 12 files
months = range(1, 13)
print("Generating files...")
for m in months:
    df = generate_month_data(m)
    filename = f"sales_data/Sales_Month_{m}.csv"
    df.to_csv(filename, index=False)
    print(f"Created {filename}")

print("Done! You now have 12 CSV files in the 'sales_data' folder.")