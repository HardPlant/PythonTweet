with open('key.txt','w') as file:
    consumer_key = ''
    consumer_secret = 'Love'
    access_token = 'Story'
    access_token_secret = ''
    #TODO : add Crypto routine
    file.write(consumer_key + '\n')
    file.write(consumer_secret + '\n')
    file.write(access_token + '\n')
    file.write(access_token_secret)