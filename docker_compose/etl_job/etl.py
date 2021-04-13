import pymongo
import time
from sqlalchemy import create_engine
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

s = SentimentIntensityAnalyzer()

time.sleep(10)  # seconds

#while True:

# Establish a connection to the MongoDB server
client = pymongo.MongoClient("mongodb")

# Select the database you want to use withing the MongoDB server
db = client.tweets

# Select the collection of documents you want to use withing the MongoDB database
collection = db.tweet_data

# As a sanity check, we read a few entries from MongoDB and print them:
entries = collection.find(limit=10000)

# Store the results in Postgres:
pg = create_engine('postgresql://lena:POSTGRES_PASSWORD@postgresdb:5432/tweets', echo=True)

pg.execute('''
   CREATE TABLE IF NOT EXISTS tweets (
   text VARCHAR(1000),
   sentiment NUMERIC
);
''')


   #for e in entries:
   #   print(e)
   #   id = e['id']
   #   text = e['text']
   #   sentiment = s.polarity_scores(e['text'])
   #   score = sentiment['compound']
   #   query = "INSERT INTO tweets VALUES (%s, %s, %s);"
   #   pg.execute(query, (text, score))


   #for e in entries:
   #   sentiment = s.polarity_scores(e['txt'])  # assuming your JSON docs have a text field
   #   print(sentiment)
   
      #replace placeholder from the ETL chapter
    #  score = sentiment['compound']
   #
   #print(e)

entries = collection.find()
for e in entries:
   print(e)
   text = e['text']
   sentiment = s.polarity_scores(e['text'])
   #print(sentiment)

   score = sentiment['compound']
   query = "INSERT INTO tweets VALUES (%s, %s);"
   pg.execute(query, (text, score))
   print(sentiment)

