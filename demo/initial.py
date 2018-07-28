import tweepy
import Tkinter

consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret_key'
access_token = 'access_token_key'
access_token_secret = 'access_token_secret'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()

print user.name + "'s profile"


def follow():
    for follower in tweepy.Cursor(api.followers, id=user.id, count=50).items():
        follower.follow()
        print follower.name


def retweetSingle(searchTerm, numberOfTweets):
    for tweet in tweepy.Cursor(api.search, searchTerm).items(numberOfTweets):
        try:
            tweet.retweet()
            print tweet
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break


def bulkRetweet(searchObj):
    for searchItem in searchObj:
        retweetSingle(searchItem["key"], searchItem["noOfTweets"])


searchObj = [
    {"key": "react js", "noOfTweets": 3},
    {"key": "competitive coding", "noOfTweets": 3},
    {"key": "logistics and supply chain", "noOfTweets": 2},
    {"key": "Shipmnts", "noOfTweets": 2}
]


def main():
    bulkRetweet(searchObj)


main()
