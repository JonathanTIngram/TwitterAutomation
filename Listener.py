from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return true

    def on_error(self, status):
        print(status)

