import requests
import smtplib #server connections
import time
from bs4 import BeautifulSoup

#car seat organizer
URL = 'https://www.amazon.ca/gp/product/B07QRR6737/ref=ox_sc_act_title_1?smid=ACFJC1O0EWRJH&psc=1'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

def checkPrice():
    page = requests.get(URL, headers=headers)

    #scrapes the page and stores all in soup
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    #print(title.strip())

    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[5:10]) #convert price from text to float, so we can compare later
    #print(converted_price)

    if(converted_price < 20):
        sendEmail()

def sendEmail():
    #establish a connection between our connection and gmail's connection
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    #login with your email address and google app password
    #google app password generator -> https://myaccount.google.com/apppasswords
    server.login("YOUREMAILADDRESS", "GOOGLE APP PASSWORD")

    #set up the email
    subject = "Price fell down!"
    body = "Check the Amazon link https://www.amazon.ca/gp/product/B07QRR6737/ref=ox_sc_act_title_1?smid=ACFJC1O0EWRJH&psc=1"
    msg = f"Subject: {subject}\n\n{body}"
    
    #send the mail
    server.sendmail(
        "FROM-EMAIL@gmail.com", #from
        "TO-EMAIL@gmail.com", #to
        msg
    )

    print("Email has been sent")
    server.quit()

#runs once every hour (60x60=3600)
while (True):
    checkPrice()
    time.sleep(3600)





