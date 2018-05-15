#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'lyl'

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC414398709e2601cbc048fb1e8f80d957'
auth_token = '80389c9e124b5de39c64bd2349e2580f'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body="Hello there!",
                              from_="+14155285612",
                              to="+8618360979676"
                          )

print(message.sid)
