import random
import smtplib
import datetime as dt
import pandas as pd

my_email = "ruben.lingito@gmail.com"
password = "sxznwsoaehfcsnpm"



#create a list of dictionaries from email-list file

df = pd.read_csv("email-list.txt")
email_list = df.to_dict('record')


#If date_today == birthday send email