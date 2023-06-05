import smtplib
import datetime as dt
import random

my_email = "ruben.lingito@gmail.com"
password = "sxznwsoaehfcsnpm"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, 
#                         to_addrs="fightmaregaming@gmail.com", 
#                         msg="Subject: Happy Birthday!\n\nThis is my attempt at sending emails via python")


now = dt.datetime.now()
day_of_week = now.weekday()


def send_quote():
    if day_of_week == 0:
        with open("quotes.txt") as quote_file:
            quote = quote_file.readlines()
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, 
                                to_addrs="fightmaregaming@gmail.com", 
                                msg=f"Subject: Monday Motivation\n\n{random.choice(quote)}")


send_quote()