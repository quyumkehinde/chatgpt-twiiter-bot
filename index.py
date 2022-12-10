import tweepy
import openai
import os

# Authenticate to Twitter
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

openai.api_key = OPENAI_API_KEY

api = tweepy.API(auth)


def handle_tweet(tweet):
    response = openai.Completion.create(
        model="text-davinci-003", prompt=tweet.text)

    api.update_status(response, tweet.id)


stream = tweepy.StreamingClient("Bearer Token")
stream.on_tweet = handle_tweet
stream.filter(track=["@ChatGPTBot_"])


# TODO: add logging implementation