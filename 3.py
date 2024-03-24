from datetime import datetime

input_date = input("Input: ")
date_format_in = "%Y-%m-%dT%H:%M:%S.%f%z"
date_format_out = "%d-%m-%Y %H:%M:%S %z"
output_date = datetime.strptime(input_date, date_format_in).strftime(date_format_out)

print("Output:", output_date)

