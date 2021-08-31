import pandas as pd
import win32com.client as win32

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
mail.To = '54152996+lucassilvasoftware@users.noreply.github.com'
mail.Subject = 'Sales Report'
mail.HTMLBody = f'''
<p>Below is the sales report for each store.<p>

<p>Revenues:</p>
{revenues.to_html(formatters={'Final Value': 'R${:,.2f}'.format})}

<p>sold amount:</p>
{amount_sales.to_html()}

<p>average ticket of products in each store:</p>
{average_ticket.to_html(formatters={'Average Ticket': 'R${:,.2f}'.format})}

<p>Sales report developed by Lucas Rebouças.</p>
'''

mail.send
print('Email sent')
