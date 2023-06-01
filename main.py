import requests
import datetime
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_Key = "M0B0XK7V9D5OZWZJ"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
st_url = 'https://www.alphavantage.co/query'
parameters = {
    "function" : "TIME_SERIES_DAILY_ADJUSTED",
    "symbol" : STOCK,
    "interval": "60min",
    "apikey": API_Key

}

def ab4_yesterday(day:datetime.date):
    cur_day =day
    while not cur_day.isoweekday():
        cur_day = cur_day -datetime.timedelta(days=1)

r = requests.get(url=st_url, params=parameters)
print(r.status_code)
data = r.json()

today = datetime.date.today()

yesterday = today - datetime.timedelta(days=1)
some_day: datetime.date
x = 1 if (yesterday -datetime.timedelta(days=1)).isoweekday() < 6 else (yesterday -datetime.timedelta(days=1)).isoweekday()-4
day_b4_yesterday = yesterday - datetime.timedelta(days=x)
print(today)
print(day_b4_yesterday)
print(data['Time Series (Daily)'][str(day_b4_yesterday)]['4. close'])
yesterday_closing_price = float(data['Time Series (Daily)'][str(yesterday)]['4. close'])
day_b4_yesterday_closing_price = float(data['Time Series (Daily)'][str(day_b4_yesterday)]['4. close'])
price_change =(yesterday_closing_price - day_b4_yesterday_closing_price)
percent_change = price_change/yesterday_closing_price * 100
if abs(percent_change) > 5:
    print(f"yes{price_change}, {round(percent_change,3)}")






## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
api = "1ed2082a86c74f92ac651dae78aff501"
end_point_url = "https://newsapi.org/v2/everything"
news_parameters = {
    "q": COMPANY_NAME,
    "from": str(yesterday),
    "sortBy": "publishedAt",
    "apiKey": api
    }
news_request= requests.get(url=end_point_url, params=news_parameters)
news_data = news_request.json()
news_dictionary = {}
top3news= []

for i in range(3):
    news_dictionary["title"] = news_data["articles"][i]["title"]
    news_dictionary['description'] = news_data["articles"][i]['description']
    news_dictionary['url'] = news_data["articles"][i]['url']
    top3news.append(news_dictionary)
print(top3news[0]['title'])


## STEP 3: Use https://www.twilio.com
# 


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

