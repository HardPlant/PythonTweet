consumer_key = ""
consume_secret = ""
access_token = ""
access_token_secret = ""

with open('key.txt') as file:
    consumer_key = file.readline().rstrip()
    consumer_secret = file.readline().rstrip()
    access_token = file.readline().rstrip()
    access_token_secret = file.readline()