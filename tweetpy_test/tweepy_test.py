import tweepy
import datetime

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