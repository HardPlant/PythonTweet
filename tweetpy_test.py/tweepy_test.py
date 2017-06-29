import tweepy
import datetime
consumer_key = ""
consume_secret = ""
access_token = ""
access_token_secret = ""

with open('key.txt') as file:
    consumer_key = file.readline().rstrip()
    consumer_secret = file.readline().rstrip()
    access_token = file.readline().rstrip()
    access_token_secret = file.readline()
print(consumer_key)
print(consumer_secret)
print(access_token)
print(access_token_secret)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#post Tweet
tweet = str(datetime.datetime.now()) + ' Test API'
api.update_status(status=tweet)

print("Successfully Posted.")
print()

#read Timeline
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)