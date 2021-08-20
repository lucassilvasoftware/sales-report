import pandas as pd

# import the database
sales_table = pd.read_excel('./excel spreadsheet/sales.xlsx')

# view database
pd.set_option('display.max_columns', None)
print(sales_table)

# revenues
revenues = sales_table[['Store ID', 'Final value']].groupby('Store ID').sum()
print(revenues)

# number of products sold per store
amount = sales_table[['Store ID', 'Amount']].groupby('Store ID')
print(amount)

# average ticket per product
average_ticket = revenues['Final value', ] / amount['Amount']
print(average_ticket)
