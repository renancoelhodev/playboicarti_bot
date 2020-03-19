import tweepy
import get_lyrics
import tweet_generator
import time

consumer_key = #consumer_key
consumer_secret = #consumer_secret
access_token = #access_token
access_token_secret = #access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

lyrics = get_lyrics.scrapy()

while True:
    api.update_status(tweet_generator.random_tweet(lyrics))
    time.sleep(3600)
