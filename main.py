import smtplib
import datetime as dt
import random

my_email = "testadordeapp0@gmail.com"
password = ""


with open("quotes.txt", "r") as f:
    all_quotes = f.readlines()
    quote = random.choice(all_quotes)


now = dt.datetime.now()
day_of_week = now.weekday()
print(day_of_week)

if day_of_week == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="testadordeapp0@yahoo.com",
            msg=f"Subject:Frase da segunda!\n\n{quote}")
