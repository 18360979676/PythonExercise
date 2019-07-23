#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'lyl'

from email.mime.text import MIMEText  # 正文内容格式为文本模式
from email.header import Header
import smtplib  # 发送邮件
import json  # 处理json数据


# 发送邮件
with open('./userData-18360979676.json',  encoding='utf-8') as fr:
    email_data = json.load(fr)

def send_email(email_data):

    msg = MIMEText(email_data["content_body"], 'plain', 'utf-8')
    msg['Subject'] = Header(email_data["content_title"], 'utf-8')
    msg["from"] = email_data["from_adder"]
    msg["to"] = email_data["from_adder"]

    try:
        smtpobj = smtplib.SMTP_SSL(email_data["server_adder"], email_data["port"])
        smtpobj.login(email_data["from_adder"], email_data["password"])
        smtpobj.sendmail(email_data["from_adder"], email_data["to_adder"], msg.as_string())
        smtpobj.quit()
        print("邮件发送成功")
    except smtplib.SMTPException as e:
        print(e)


if __name__ == '__main__':
    send_email(email_data)  # 封装发送短信的函数
