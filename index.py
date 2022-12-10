import tweepy
import openai
import os
import traceback

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

try:
    auth = tweepy.OAuthHandler(
        consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)

    openai.api_key = OPENAI_API_KEY

    api = tweepy.API(auth)

    def handle_tweet(tweet):
        response = openai.Completion.create(
            model="text-davinci-003", prompt=tweet.text)

        api.update_status(response["choices"][0].text, tweet.id)

    stream = tweepy.StreamingClient("Bearer Token")
    stream.add_rules(tweepy.StreamRule("@ChatGPTBot_"))
    stream.on_tweet = handle_tweet
    stream.filter()
except Exception:
    traceback.print_exception()
