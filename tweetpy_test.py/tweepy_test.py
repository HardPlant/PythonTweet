import tweepy
import datetime
consumer_key = ""
consume_secret = ""
with open('key.txt') as file:
    consumer_key = file.readline()
    consumer_secret = file.readline()

print(consumer_key)
print(consumer_secret)