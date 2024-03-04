from forex_python.bitcoin import BtcConverter
from datetime import datetime

# User inputs for Bitcoin purchase date and amount paid
year = int(input("Enter the year you bought Bitcoin: "))
month = int(input("Enter the month you bought Bitcoin (1-12): "))
day = int(input("Enter the day you bought Bitcoin: "))
amount_paid = float(input("Enter the amount paid in dollars: "))

# Current date
current_date = datetime.now().strftime("%Y-%m-%d")

# Bitcoin Converter object
btc_converter = BtcConverter()

# Exchange rate on the purchase date
purchase_rate = btc_converter.get_rate_on_date("USD", current_date, to_currency="BTC")

# Current value of Bitcoin
current_value = amount_paid * btc_converter.get_latest_price("USD")

# Profit or Loss
profit_loss = current_value - amount_paid

# Display the result
print("Bought Bitcoin on {}/{}/{}".format(year, month, day))
print("Amount paid: ${:.2f}".format(amount_paid))
print("Current value: ${:.2f}".format(current_value))
print("Profit/Loss: ${:.2f}".format(profit_loss))
