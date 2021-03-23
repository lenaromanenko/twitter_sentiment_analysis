#import time
#import os
#from datetime import datetime
import logging
#import random
import config
from tweepy import OAuthHandler, Cursor, API
from tweepy.streaming import StreamListener
import logging
import pymongo

# Redirect logs to a file
logging.basicConfig(filename='debug.log', 
                    level=logging.WARNING)

# Create a connection to the MongoDB database server
client = pymongo.MongoClient(host='mongodb') # hostname = servicename for docker-compose pipeline

# Create/use a database
db = client.tweets
#equivalent of CREATE DATABASE tweets;

# Define the collection
collection = db.tweet_data
#equivalent of CREATE TABLE tweet_data;

def authenticate():
    """Function for handling Twitter Authentication. Please note
       that this script assumes you have a file called config.py
       which stores the 2 required authentication tokens:

       1. API_KEY
       2. API_SECRET
    
    See course material for instructions on getting your own Twitter credentials.
    """
    auth = OAuthHandler(config.API_KEY, config.API_SECRET)
    return auth

if __name__ == '__main__':
    auth = authenticate()
    api = API(auth)

    cursor = Cursor(
        api.user_timeline,
        id = 'BioNTech_Group',
        tweet_mode = 'extended'
    )

    for status in cursor.items(10000):             
        tweet = {
            'text': status.full_text,
            'username': status.user.screen_name,
            'followers_count': status.user.followers_count
        } 
        collection.insert_one(tweet)
        print(tweet)

