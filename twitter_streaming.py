#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy

#Variables that contains the user credentials to access Twitter API 
access_token = "7514942-YoGmvsAdGeSwAGSOmSCVvYjI5rRVmta1AKG6gpUacT"
access_token_secret = "zDPNl2N5kF0Tzt4FUKlIEMy6cja9Mr8fjYU9M4YR0mztr"
consumer_key = "llZnncF89rgIdcYTiXuy1F3LA"
consumer_secret = "WAW6rUb6ZGN9juBncpWyQDbJk68K1bEpwbxvBxGZqKmgAGKDus"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.secure = True
    auth.set_access_token(access_token, access_token_secret)
   # api = tweepy.API(auth)
    #print(api.me().name)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'big data', 'bigdata'
    stream.filter(track=['python', 'bigdata', 'big data'])