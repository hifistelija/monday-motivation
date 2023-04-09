import random
import smtplib
import datetime as dt
import random

MY_EMAIL = "email@yahoo.com"
PASSWORD = "inserthere"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()

    all_quotes = [quote.strip() for quote in all_quotes]
    file.close()
    quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}."
        )
        connection.close()

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1992, month=10, day=15)
# print(date_of_birth)