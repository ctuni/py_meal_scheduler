# importing module
from pandas import *
import random
import smtplib
import ssl
from email.message import EmailMessage
import os

# reading CSV file
data = read_csv("menu.csv")

# converting column data to list
breakfast = data['Breakfast'].tolist()
lunch = data['Lunch'].tolist()
dinner = data['Dinner'].tolist()

#today's menu on a list
menu = [random.choice(breakfast),random.choice(lunch),random.choice(dinner)]

#email configuration 
email_sender = 'placeholder@gmail.com' #change this for your email
email_password = os.environ.get('MENU_PY_PWD') #create an app password using google account and put it into your /.bashrc (and source!)
email_receiver = 'placeholder@gmail.com' #change this for the email reciever

subject = 'Avui toca de menjar...' #change this for the subject
body = '\n'.join(menu) #change this for the body, I did a very lazy joining using newline

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
