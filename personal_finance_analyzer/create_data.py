import csv

# The dirty data
data = [
    ["Date", "Description", "Amount", "Category"],
    ["2024-01-01", "Amazon Purchase", "50.00", "Shopping"],
    ["01/02/2024", "Local Grocery Store", " 120.50 ", "Groceries"],
    ["2024-01-05", "Cinema Ticket", "$15.00", "Entertainment"],
    ["Jan 7 2024", "Netflix Subscription", "14.99", "Entertainment"],
    ["2024-01-10", "", "45.00", "groceries"],  # Missing Description, lowercase category
    ["12/01/2024", "Shell Station", "55.20", "Gas"],
    ["2024-01-15", "Gym Membership", "", "Health"], # Missing Amount
    ["2024-01-20", "Paycheck", "2000.00", "Income"],
    ["21/01/2024", "Coffee Shop", "5.50", ""], # Missing Category
    ["2024-01-25", "Phone Bill", "$60.00", "Utilities"],
    ["", "Unknown Expense", "100.00", ""], # Missing Date and Category
    ["2024-01-30", "Target Store", " 80.00 ", "Shopping"]
]

# Write to CSV file
with open('transactions.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("File 'transactions.csv' created successfully!")