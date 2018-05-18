#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'lyl'


from email.mime.text import MIMEText  # 邮件库
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib  # 发送邮件文件
import json


# 发送邮件
with open('./userData-396852019.json',  encoding='utf-8') as fr:
    email_data = json.load(fr)


msgroot = MIMEMultipart('related')
msgroot['Subject'] = email_data["content_title"]
msgroot['to'] = email_data["to_addr"]
msgroot['Cc'] = email_data["to_addr"]
msgroot['from'] = email_data["from_adder"]

msg = MIMEText(email_data["content_body"], 'plain', 'utf-8')
msg['Subject'] = Header(email_data["content_title"], 'utf-8')

msgroot.attach(msg)

try:
    smtpObj = smtplib.SMTP_SSL(email_data["server_addr"], email_data["port"])
    smtpObj.login(email_data["from_adder"], email_data["password"])
    smtpObj.sendmail(email_data["from_adder"], email_data["to_addr"], msgroot.as_string())
    smtpObj.quit()
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print(e)




