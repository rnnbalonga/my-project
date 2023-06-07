import random
import smtplib
import datetime as dt
import pandas as pd

my_email = "ruben.lingito@gmail.com"
password = "sxznwsoaehfcsnpm"



#create a list of dictionaries from email-list file

df = pd.read_csv("email-list.txt")
email_list = df.to_dict('records')
email_templates = ["email-1.txt", "email-2.txt", "email-3.txt"]

#Check today's date

today = dt.datetime.now()
today_month = today.month
today_day = today.day

#Check if there's a matching month in the dictionary
def greet():
    for i in range(0,2):
        if today_month == email_list[i]['month']:
            if today_day == email_list[i]['day']:
                name = email_list[i]['name']
                with open(random.choice(email_templates), 'r') as email_file:
                    email_content = email_file.readlines()
                    email_greeting = email_content[0].replace("[NAME]", name)
                    email_content[0] = email_greeting
                    print(email_content)
                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=password)
                    connection.sendmail(from_addr=my_email, 
                                        to_addrs="fightmaregaming@gmail.com", 
                                        msg=f"Subject:HAPPY BIRTHDAY TO YOU!\n\n{email_content}")
                    
greet()