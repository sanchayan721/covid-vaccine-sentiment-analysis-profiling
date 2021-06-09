import sys
import subprocess
from os import path

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



tweeter_api = getAPI()

