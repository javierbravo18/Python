# Python script to post Bitcoin price updates Tweet.
# Twitter developer account needed. Apply at https://developer.twitter.com/en
# Schedule this script to run periodically to automatically post Bitcoin price updates to your Twitter account.

# tweepy handles Twitter API requests
import tweepy
from tweepy.auth import OAuthHandler
# yfinance handles Yahoo Finance API requests
import yfinance as yf
# random is used to generate random numbers
import random

#When you create an App in Twitter portal, generate the credentials below.
# These credentials are used to access the Twitter account and makre requests on behalf of the Twiiter account.
consumer_key = "<EnterTwitterAPIKey>"
consumer_secret = "<EnterTwitterAPIKeySecret>"
access_token = "<EnterTwitterAccessToken>"
access_secret = "<EnterTwitterAccessSecret>"
# Generates a random number between 1 and 100. To be used for Bot number.
rnum = random.randint(1,100)

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# Requests information about Bitcoin USD from Yahoo Finance API
stock_info = yf.Ticker('BTC-USD').info
# stock_info.keys() for other properties you can explore

# Pulls current price
market_price = stock_info['regularMarketPrice']

# Pulls 52 week high
fifty_two_high = stock_info['fiftyTwoWeekHigh']

# Pulls 52 week low
fifty_two_low = stock_info['fiftyTwoWeekLow']

# Randomly generates a number between 0 and 5, to be used for randomly selecting Tweet.
rnum1 = random.randint(0,5)

# Depending on rnum1 generated, picks a message for the Twitter post
if rnum1 == 0:

    twitterpost = f"#BTC is currently sitting at ${market_price}. With a 52-week range of ${fifty_two_low} - {fifty_two_high}. Posted by Javier's Bot {rnum}."

elif rnum1 == 1:

    twitterpost = f"Don't know how much gold is worth, but Bitcoin is worth ${market_price}. Gold s*cks. -Middle Schooler Bot {rnum}."

elif rnum1 == 2:

    twitterpost = f"The father of all crytpto, #BTC is currently priced at ${market_price}. Say hello to my little gains! -Tony Botana {rnum}."

elif rnum1 == 3:

    twitterpost = f"#Bitcoin is currently worth ${market_price}. Dammit, should've bougth in early but I'm a bot. #BTC -Posted by Greedy Bot {rnum}."

elif rnum1 == 4:

	twitterpost = f"#BTC is currently sitting at ${market_price}. With a 52-week range of ${fifty_two_low} - {fifty_two_high}. Posted by Your's Truly, Bot {rnum}."

elif rnum1 == 5:

	twitterpost = f"You mean to tell me that one #Bitcoin costs ${market_price}. That's like a million grams of &*%$3#$%!!!! -Crackhead Bot Joe Momma {rnum}."

elif rnum1 == 6:

	twitterpost = f"Is my only purpose in life telling you people the price of #Bitcoin? Well it's ${market_price}. ***Error: Sad Bot {rnum} ended his own program***"


else:

    twitterpost = f"Some weird error happened, and Javi's bots are not feeling too hot... But here's the price of #Bitcoin ${market_price}. Posted by Javier's Messed UP Bot {rnum}."

# Creates Twitter API request to post a new Tweet and passes the selected message.
api.update_status(twitterpost)
