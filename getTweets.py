import sys
import subprocess
from os import path
import csv


# Importing apiToken module
try:
    import apiToken as token

except ModuleNotFoundError:
    Exception("apiToken module missing from the project.")

# Importing Tweepy library
try:
    print('importing tweepy ...')
    import tweepy
    
except ModuleNotFoundError:
    print("Warning: tweepy module not found!")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tweepy'])
    print("importing tweepy ...")
    import tweepy



def getAPI():
 
    consumer_key, consumer_secret, access_token, access_token_secret = token.getKeys()
    
    if access_token == '' or access_token_secret == '':
        
        try:
            auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
            api = tweepy.API(auth)
            return api
    
        except:
            print("\nError: Invalid API keys! \nPlease check the keys and try again")
            return getAPI()

    else:
        
        try:
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            auth.set_access_token(access_token, access_token_secret)
            api = tweepy.API(auth, wait_on_rate_limit=True)
            return api
        
        except:
            print("\nError: Invalid API keys! \nPlease check the keys and try again")
            return getAPI()


def write_to_csv(new_data, filename='data/raw_test.csv'):
    with open(filename, 'a', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(new_data)
        

tweeter_api = getAPI()
search_words = ["BioNTech", "Moderna", "Covishield", "AstraZeneca", "Sputnik V", "Convidicea", "EpiVacCorona",
            "Johnson & Johnson vaccine", "Sputnik Light", "PakVac", "Ad5-nCoV", "Sinovac vaccine", "Sinopharm vaccine",
            "Pfizer Vaccine", "Comirnaty Vaccine", "Covaxin Vaccine", "Bharat Biotech Vaccine"]


for search_word in search_words:
    
    api_search = search_word + " -filter:retweets"
    tweets = tweepy.Cursor(tweeter_api.search, q=api_search).items(10000)

    for tweet in tweets:
        
        if tweet.text != '':
            tweet_data = [search_word, tweet.text, tweet.user.location, tweet.user.verified, tweet.lang, tweet.user.followers_count]
            try:
                write_to_csv(tweet_data)
            except:
                pass
        
        else:
            pass