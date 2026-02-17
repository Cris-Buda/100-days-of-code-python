import requests
from datetime import datetime
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
Endpoint = "https://www.alphavantage.co/query"
api_key =
params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": api_key
}

response = requests.get(Endpoint, params=params)
data = response.json()
# print(data)



news_endpoint = "https://newsapi.org/v2/everything"
news_api_key =

now = datetime.day
news_params = {
    "q": COMPANY_NAME,
    "from": STOCK,
    "sortBy": "popularity",
    "apikey": news_api_key
}

account_sid = ""
auth_token = ""

news_response = requests.get(news_endpoint, params=news_params)
news_data = news_response.json()



open_stock_price_yesterday = data["Time Series (Daily)"]["2025-02-14"]["1. open"]
close_stock_price_yesterday = data["Time Series (Daily)"]["2025-02-14"]["4. close"]

close_stock_price_the_day_befere_yesterday = data["Time Series (Daily)"]["2025-02-13"]["1. open"]

print(open_stock_price_yesterday, close_stock_price_yesterday, close_stock_price_the_day_befere_yesterday)

diference = float(open_stock_price_yesterday) - float(close_stock_price_the_day_befere_yesterday)
print(diference)

modificat = False

if diference > 5 or diference < 5:
    print("Get News")
    modificat = True
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"{news_data["articles"][0]["description"]}\n\n\n{news_data["articles"][1]["description"]}\n\n\n{news_data["articles"][2]["description"]}",
        from_="",
        to="",
    )
    print(message.status)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    print(news_data)
    print(f"{news_data["articles"][0]["description"]}\n\n\n{news_data["articles"][1]["description"]}\n\n\n{news_data["articles"][2]["description"]}")

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

