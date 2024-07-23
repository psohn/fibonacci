import os
from dotenv import load_dotenv
import tweepy

load_dotenv()


class Twitter:
    def __init__(self):
        self.twitter_api_key = os.getenv("TWITTER_API_KEY")
        self.twitter_api_key_secret = os.getenv("TWITTER_API_SECRET")
        self.twitter_access_token = os.getenv("TWITTER_ACCESS_TOKEN")
        self.twitter_access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
        self.client = self._instantiate_client()

    def _instantiate_client(self):
        client = tweepy.Client(
            consumer_key=self.twitter_api_key,
            consumer_secret=self.twitter_api_key_secret,
            access_token=self.twitter_access_token,
            access_token_secret=self.twitter_access_token_secret,
        )
        return client

    def tweet(self):
        self.client.create_tweet(text="hello world")
