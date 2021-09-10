![git header (3)](https://user-images.githubusercontent.com/54152996/132924461-3322221b-96b3-44ba-90d5-f8afa86d31bb.png)

> Status: Finished ✅

Software designed to read sales tables and email the sales report containing the billing, the quantity of products sold and the average ticket.

## Technologies Used:

<table>
  <tr>
    <td>Technology</td>
    <td>Python</td>
    <td>Pandas</td>
    <td>Outlook</td>
  </tr>
  <tr>
    <td>Version</td>
    <td>3.9.7</td>
    <td>1.3.2</td>
    <td>2019 Version 2108</td>
  </tr>
</table>

## How to run the application:

1. Install all dependencies;
2. Add your sale sheet;

   ![a](https://user-images.githubusercontent.com/54152996/132927610-efa770c2-9b8f-4e45-bc1f-8dffefc5fc11.jpg)

3. Create a free [Twilio](https://www.twilio.com/try-twilio) account; 
4. Get your account_sid, auth_token and your trial phone number;
     ```
    # Your Account SID from twilio.com/console
    account_sid = "W"
    
    # Your Auth Token from twilio.com/console
    auth_token = "X"
    
    # Trial phone number
    from_="Z",
    ```    
5. add your phone number to receive the SMS;
    ```
    if (sales_table['Sales'] > 55000).any():
        seller = sales_table.loc[sales_table['Sales']
                                > 55000, "Seller"].values[0]
        sales = sales_table.loc[sales_table['Sales']
                                > 55000, "Sales"].values[0]
    ```
6. Update the sales target value in code;
    ```
    # Your phone number
    to='Y',
    ```    
7. Run.

## SMS Template:

* The software identifies and shows through SMS the salesperson who reached the goal and also how much he made in sales

![git twilio message sales goal](https://user-images.githubusercontent.com/54152996/129395626-f3c77b74-cac6-444c-99d4-ffc46d5573ef.jpeg)
