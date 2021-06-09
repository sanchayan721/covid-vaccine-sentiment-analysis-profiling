import sys
import subprocess
import json
from os import path

# Importing Cryptography library
try:
    from cryptography.fernet import Fernet
    print('importing cryptography ...')
    
except ModuleNotFoundError:
    print("Warning: cryptography module not found!")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'cryptography'])
    print("\nimporting cryptography ...")
    from cryptography.fernet import Fernet


def getKeys(console_entry = bool()):

    if not console_entry:
        raw_entry = input("\nAre you authorized to use Sanchayan's Twitter API Tokens? ... [Yes/no] ")
        
        if raw_entry.lower() in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup']:
            console_entry = True
        
        elif raw_entry.lower() in ['no', '0', 'not', 'false', 'none', 'n', 'f']:
            console_entry = False
        
        else:
            print("\nError: Invalid Option! \nPlease try again with correct option.")
            return getKeys()
            

    if console_entry == True and not path.exists("tokens.encrypted"):
        print("\nError: Sanchayan's encrypted token file is missing. \nPlease try with your own API keys.")
        return getKeys(console_entry = False)

    elif console_entry == True and path.exists("tokens.encrypted"):

        decryption_key = input("\nPlease Enter The Decryption Key Provided by Sanchayan: ")
        
        try:
            with open('tokens.encrypted', 'rb') as encrypted_file:

                decrypted_content = Fernet(decryption_key).decrypt(encrypted_file.read())
            
            token = json.loads(decrypted_content)
            
            consumer_key = token.get("API Key")
            consumer_secret = token.get("API Secret")
            access_token = token.get("Access Token")
            access_token_secret = token.get("Access Token Secret")

            return (consumer_key, consumer_secret, access_token, access_token_secret)

        except:
            print("\nError: Wrong decryption key! \nPlease check the key and try again.")
            return getKeys()

    elif console_entry == False:

        print("\nPlease Create a Twitter API token and enter below.\n")
        
        consumer_key = input('Please Enter API Key: ')
        consumer_secret = input('Please Enter API Secret: ')
        access_token = input('Please Enter Access Token: ')
        access_token_secret = input('Please Enter Access Token Secret: ') 

        return (consumer_key, consumer_secret, access_token, access_token_secret)