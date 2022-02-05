import tweepy
from tweepy import user
from credentials import *
import logging
from pymongo import MongoClient

 


client = tweepy.Client(bearer_token=BEARER_TOKEN,consumer_key=API_KEY,consumer_secret=API_KEY_SECRET,
                          access_token=ACCESS_TOKEN,access_token_secret=ACCESS_TOKEN_SECRET)

if client:
    logging.critical("\nAutentication OK")
else:
    logging.critical('\nVerify your credentials')

#conn_string = f"mongodb://{mongotweet}:{27017}"
clientmdb = MongoClient("mongotweet")

try:
    # The ping command is cheap and does not require auth.
    clientmdb.admin.command('hello')
    logging.critical('\n########################################\n\
Connection to Mongodb Server Established\
\n########################################\n')
except:
    logging.critical('\n###################################\nConnection to Mongodb Server Failed\n###################################\n')

#### LOOKUP USERS USING THEIR USERNAME

# for user_fields parameters check here https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/us

biden= client.get_user(username='JoeBiden',user_fields=['name','id','created_at'])
print(biden)

print(f'the user with name {biden.data.name} and ID {biden.data.id} created its twitter account on {biden.data.created_at}')

#### LOOKUP AT USER'S TIMELINE

## biden's timeline
## passing biden id into the function below
# for tweets_fields parameters check herehttps://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet
biden_tweets = client.get_users_tweets(id=biden.data.id, tweet_fields=['id','text','created_at'],max_results=20)
print(biden_tweets.data)
for tweet in biden_tweets.data:
    print(f"the user {biden.data.name} at {tweet.created_at} wrote:{tweet.text}\n")



#### SEARCHING FOR TWEETS #####

# Defining a query search string
query2 = 'Nation+Democracy -is:retweet'


search_tweets = client.search_recent_tweets(query=query2,tweet_fields=['id','text','created_at'], max_results=100)
print(search_tweets)
for tweet in search_tweets.data:
    logging.critical(f'\n\n\nINCOMING TWEET:\n{tweet.text}\n\n\n')

###Creating Database and collection for mongo
db_tweets = clientmdb.tweets
col_tweets= db_tweets.collection_tweets

### Getting more than 100 tweets using Paginator

paginator = tweepy.Paginator(client.search_recent_tweets,tweet_fields=['id','created_at','text'], query=query2).flatten(limit=200)
print(paginator)
for tweet in paginator:
    logging.critical(f'\n\n\nINCOMING TWEET ID {tweet.id}:\n{tweet.text}\n\n\n')
    file = open('fetched_tweets.txt',mode='a',encoding= "utf-8")
    file.write(tweet.text)
    file.close()
    doc_tweet = {"text":tweet.text}
    logging.critical(f"\n---- INSERTING A NEW TWEET DOCUMENT INTO THE 'col_tweets' ----\n")
    col_tweets.insert_one(doc_tweet)
    if col_tweets.find_one(doc_tweet):
        logging.critical(f"\n---- TWEET DOCUMENT SUCCESSFULLY INSERTED ----\n")


    



