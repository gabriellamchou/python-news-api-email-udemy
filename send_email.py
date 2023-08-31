import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    sender = "gabriel.lamela.ch@gmail.com"
    receiver = "gabriel.lamela.ch@gmail.com"

    password = os.getenv("PASSWORD")
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)
