import win32com.client as win32
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
average_ticket = (revenues['Final value'] / amount_sales['Amount']).to_frame()
print(average_ticket)

# send email with report
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'To address'
mail.Subject = 'Message Subject'
mail.HTMLBody = '<h2>HTML BODY</h2>'

mail.send
