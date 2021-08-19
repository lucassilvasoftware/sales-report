import pandas as pd

# import the database
sales_table = pd.read_excel('"./Excel spreadsheets/sales.xlsx')

print(sales_table)
