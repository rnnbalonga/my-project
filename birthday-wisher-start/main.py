import smtplib

my_email = "ruben.lingito@gmail.com"
password = "sxznwsoaehfcsnpm"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, 
                        to_addrs="rara.huhu@yahoo.com", 
                        msg="Subject: Happy Birthday!\n\nThis is my attempt at sending emails via python")