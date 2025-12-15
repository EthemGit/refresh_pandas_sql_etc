import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("transactions.csv")

# clean Date
df.Date = pd.to_datetime(df.Date, format="mixed")
df.at[5, "Date"] = pd.to_datetime("01/12/2024")
df.Date = df["Date"].ffill()

# clean amount
df.Amount = pd.to_numeric(
                df.Amount.replace(r"\$", "", regex=True)
            ).fillna(0)

# clean description
df.Description = df.Description.fillna("Unknown Expense")

# clean Category
df.Category = df.Category.fillna("Uncategorized").str.title()

# group by category
category_sums = df.groupby("Category")["Amount"].sum().drop("Income")

# create graphic
ax = category_sums.plot(kind="bar", title="Expenses per Category")
ax.set_xlabel("Category")
ax.set_ylabel("Expense in $")

plt.tight_layout()
# plt.show()

df.to_csv("cleaned_expenses.csv", index=False)