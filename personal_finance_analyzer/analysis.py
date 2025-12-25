import pandas as pd
import matplotlib.pyplot as plt

"""
Basic cleaning up of a messy csv.
Visualizing it using matplotlib in a simple bar chart.
"""

df = pd.read_csv("transactions.csv")

# clean date
df.Date = pd.to_datetime(arg=df.Date, format="mixed")
df.at[5, "Date"] = pd.to_datetime("2024/01/12")
df.Date = df.Date.ffill()

# clean description
df.Description = df["Description"].fillna("Unknown Expense")

# clean category
df.Category = df["Category"].str.strip().str.title()
df.Category = df.Category.fillna("Uncategorized")

# clean amount
df.Amount = df["Amount"].str.strip().str.replace('$', '', regex=False)
df.Amount = pd.to_numeric(arg=df.Amount)
df.Amount = df["Amount"].fillna(0)

# delete income, we only care about expenses
df = df[df['Description'] != 'Paycheck']

category_sums = df.groupby("Category")["Amount"].sum()

plot = category_sums.plot(kind="bar", title="Expenses per Category")
plot.set_xlabel("Category")
plot.set_ylabel("Expense in $")

plt.tight_layout()
plt.show()


print(df)
