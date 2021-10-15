#!/usr/bin/env python3

import smtplib
import os

class Email:
  def __init__(self, sent_from=os.environ['GMAIL_USER'], sent_to=os.environ['GMAIL_USER'], subject=None, body=None):
    self.gmail_user = os.environ['GMAIL_USER']
    self.gmail_pass = os.environ['GMAIL_PASS']
    self.sent_from  = sent_from
    self.sent_to    = [sent_to]
    self.subject    = subject
    self.body       = body

  def send(self):
    email_text = """\
From: %s
To: %s
Subject: %s
%s
    """ % (self.sent_from, ", ".join(self.sent_to), self.subject, self.body)
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(self.gmail_user, self.gmail_pass)
    server.sendmail(self.sent_from, self.sent_to, email_text)
