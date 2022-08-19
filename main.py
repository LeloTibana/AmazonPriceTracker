import requests
from bs4 import BeautifulSoup
import smtplib

AMAZON_URL = "https://www.amazon.com/Chefman-4-5-Quart-Air-Fryer/dp/B08GY96RL7/ref=sr_1_3?keywords=air+fryer&qid=1658303573&sr=8-3"
headers = {
    "Accept-Language": "en",
    "User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 14816.99.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
}

response = requests.get(AMAZON_URL, headers=headers)
amazon_page = response.content


soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price = soup.find("span", class_="a-price aok-align-center reinventPricePriceToPayMargin priceToPay").get_text()
# print(price)
price_without_symbol = price.split("$")[1]
# print(price_without_symbol)
price_float = float(price_without_symbol)
# print(price_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)

SENDER = "testmphumelelo@gmail.com"
PASSWORD = "hqithsrwwivyauwu"

TARGET_PRICE = 80

if TARGET_PRICE >= price_float:
    message = f"{title} is now at ${price_float}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(SENDER, PASSWORD)
        connection.sendmail(from_addr=SENDER,
                            to_addrs=SENDER,
                            msg=f"Subject: Amazon Price Alert for Air Fryer!!! \n\n{message}\n{AMAZON_URL}")


