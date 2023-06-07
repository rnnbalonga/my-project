import random
import smtplib
import datetime as dt
import pandas as pd
import time
import schedule

my_email = "ruben.lingito@gmail.com"
password = "kizszdeyikbdrhig"

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
                name_email = email_list[i]['email']
                with open(random.choice(email_templates), 'r') as email_file:
                    email_content = email_file.read()
                    final_email = email_content.replace("[NAME]", name)
                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user=my_email, password=password)
                    connection.sendmail(from_addr=my_email, 
                                        to_addrs=name_email, 
                                        msg=f"Subject:HAPPY BIRTHDAY TO YOU!\n\n{final_email}")

                    
schedule.every().day.at("12:00").do(greet)

while True:
    schedule.run_pending()
    time.sleep(1)