from textblob import TextBlob
import tweepy
import sys

api_key = ""
api_key_secret = ""
access_token = ""
access_token_secret = ""

auth_handler = tweepy.OAuth1UserHandler(consumer_key=api_key,
                                        consumer_secret=api_key_secret,
                                        access_token=access_token,
                                        access_token_secret=access_token_secret)

api = tweepy.API(auth_handler, wait_on_rate_limit=True)

selection = input("What would you like to mimic? ")

search_term = "hey"

tweet_amount = 10

#the number of tweets that we will be carrying over
tweets = tweepy.Cursor(api.search_tweets, q=search_term, lang='en').items(tweet_amount)
for tweet in tweets:
    print(tweet.text)


