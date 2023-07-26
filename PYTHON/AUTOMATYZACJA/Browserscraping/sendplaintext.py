import smtplib
import os

sender = 'automateeverythingwithpython@hotmail.com'
receiver = 'app7flask@gmail.com'
password = 'python12345678'

message = """\
Subject: Hello Hello

This is Ardit!
Just wanted to say hi!
"""

server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login(sender, password)
server.sendmail(sender, receiver, message)
server.quit()
