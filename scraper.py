import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com/Apple-MacBook-9th-generation-Intel-Core-i9-processor/dp/B07S58MHXF/ref=mp_s_a_1_3?keywords=macbook+pro&qid=1564506496&s=gateway&sr=8-3'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    # convert the price string into a float and select the first 5 characters
    string_price = price[1:6]
    int_price = string_price.replace(',', '')
    converted_price = int(int_price)

    # print(converted_price)
    # print(title.strip())

    if (converted_price < 2000):
        send_mail()
        # print('it works')


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # input your email, password
    server.login('', '')

    subject = 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.com/Apple-MacBook-9th-generation-Intel-Core-i9-processor/dp/B07S58MHXF/ref=mp_s_a_1_3?keywords=macbook+pro&qid=1564506496&s=gateway&sr=8-3'
    msg = f'Subject:{subject}\n\n{body}'

    server.sendmail(
        '',  # the sender's email
        '',  # the receiver's email
        msg
    )

    # print('Hey email has been sent')

    server.quit()


check_price()
