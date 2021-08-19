import pandas as pd

# import the database
sales_table = pd.read_excel('./excel spreadsheet/sales.xlsx')

# view database
pd.set_option('display.max_columns', None)
print(sales_table)

# revenues
revenues = sales_table[['Store ID']]
