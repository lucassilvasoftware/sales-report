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
amount_sales = sales_table[['Store ID', 'Amount']].groupby('Store ID').sum()
print(amount_sales)

print('-' * 50)
# average ticket per product
average_ticket = (revenues['Final value'] / amount_sales['Amount']).to_frame
average_ticket = average_ticket.rename(columns={0: 'Ticket Médio'})
print(average_ticket)
