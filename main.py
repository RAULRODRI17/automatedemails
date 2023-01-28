import yagmail
import pandas
from news import NewsEmail
import datetime
import time


def send_email():
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    news_feed = NewsEmail(interest=row['interest'],
                          from_date=yesterday,
                          to_date=today)
    email = yagmail.SMTP(user="raul.rdzwallace@gmail.com", password="cacgcwwfxkfmsbyf")
    email.send(to=row["email"],
               subject=f"Hi there are your {row['interest']} news for today",
               contents=f"this {row['name']}\n See what's on about {row['interest']} today, {news_feed.get()}")


while True:
    if datetime.datetime.now().hour == 10 and datetime.datetime.now().minute == 45:
        df = pandas.read_excel('people.xlsx')

        for index, row in df.iterrows():
            send_email()
    time.sleep(60)