import smtplib
import datetime as dt

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
            quote_number = 0 
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, 
                                to_addrs="fightmaregaming@gmail.com", 
                                msg=f"Subject: Monday Motivation" {quote[quote_number]})
            quote_number += 1
            print(quote_number)

send_quote()