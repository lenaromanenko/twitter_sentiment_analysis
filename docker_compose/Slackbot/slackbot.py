import os
import time
import slack
from sqlalchemy import create_engine
import logging
import requests
import pandas as pd

WEBHOOK_URL="https://hooks.slack.com/services/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"

time.sleep(15)

pg = create_engine('postgres://lena:1234@postgresdb:5432/tweets', echo=True)

query = """SELECT * FROM tweets"""

time.sleep(15)

while True:
    tweet = pd.read_sql_query(query, con=pg)
    logging.warning('query =  \n {}'.format(tweet))
    text = tweet['text'].iloc[0]
    sentiment =  tweet['sentiment'].iloc[0]
    output = f'Tweet from BioNTech_Group: {text}; \n\n\nThe sentiment score for this tweet is: {sentiment}'
    data = {'text': output}
    requests.post(url=WEBHOOK_URL, json=data)
    time.sleep(120)