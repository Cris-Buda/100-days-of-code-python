# import smtplib
#
# my_email = "abc@gmail.com"
# password = "abc"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="abc@yahoo.com",
#         msg="Subject:Hello\n\nThis is my email."
#     )

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# if year == 2020:
#     print("Wear a face mask")
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=, month=, day=, hour=)
# print(date_of_birth)

import datetime as dt
import pandas
import random
import smtplib

# now = dt.datetime.now()
# weekday = now.weekday()
#
# with open("quotes.txt") as data_file:
#     data = data_file.readlines()
#
# my_email = "abc@gmail.com"
# password = "abc"
#
# if weekday == 0:
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(
#             from_addr=my_email,
#             to_addrs="abc@yahoo.com",
#             msg=random.choice(data)
#         )

#sau

MY_EMAIL = "abc@gmail.com"
MY_PASSWORD = "abc"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="abc@yahoo.com",
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )