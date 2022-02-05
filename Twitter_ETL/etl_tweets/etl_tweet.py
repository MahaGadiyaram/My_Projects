from pymongo import MongoClient
from sqlalchemy import create_engine
from time import sleep
from numpy import random
import logging
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer



sleep(20)

### 1. PREPARING THE DATABASES
##############################

## MONGODB 
clientmdb = MongoClient("mongotweet")

# Connecting to the database tweets
db_tweets = clientmdb.tweets

# Connecting to the collection 'collection_tweets'
col_tweets= db_tweets.collection_tweets


## POSTGRES
USERNAME_PG = 'postgres'
PASSWORD_PG = 'postgres'
HOST_PG = 'psqltweet' 
PORT_PG = 5432
DATABASE_NAME_PG = 'sentiment_db'

# Connection string
conn_string_pg = f"postgresql://{USERNAME_PG}:{PASSWORD_PG}@{HOST_PG}:{PORT_PG}/{DATABASE_NAME_PG}" 
pg = create_engine(conn_string_pg)

# Creating a table

pg.execute("""
CREATE TABLE IF NOT EXISTS tweet_table (
    id BIGSERIAL,
    transformed_text VARCHAR(500),
    sentiment NUMERIC
);

""")

def extract():
    """ Gets a random tweet from a mongo database"""
    extracted =[]
    tweet_document_list = list(col_tweets.find())
    for document in tweet_document_list:
        
        try:
            logging.critical(f"\n---RANDOM tweet EXTRACTED---\n{document['tweet']['text']}")
            extracted.append(document['tweet']['text'])
        except:
            pass
    return extracted
    

def transform(tweet):
    """
    This will eventually return the sentiment analysis results.
    You may consider to further clean the text after the sentiment analysis. 
    """
    s  = SentimentIntensityAnalyzer()
    print(f"This is where you insert the sentiment analysis for {tweet}")

    sentiment = s.polarity_scores(tweet)
    print(sentiment)
    score = sentiment['compound']
    logging.critical("\n---TRANSFORMATION COMPLETED---")
    return tweet,score

def load(tweet,sentiment):
    """
    This function writes the transformed tweet and the
    sentiment into a postgres database (table tweet_table).
    """
    try:
        pg.execute(f"""INSERT INTO tweet_table (transformed_text, sentiment)
               VALUES ('{tweet}', '{sentiment}) """)
        logging.critical(f"TWEET AND SENTIMENT {sentiment} LOADED INTO POSTGRES")
    except:
        pass


tweetlist = extract()
for tweet in tweetlist: 
    transformed_tweet,score = transform(tweet)
    load(transformed_tweet,score)


