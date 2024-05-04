import tweepy as twpy
from os import environ
import json as json

api_key = "..."
api_secrets = "..."
access_token = "..."
access_secret = "..."

auth = twpy.OAuthHandler(api_key,api_secrets)
auth.set_access_token(access_token,access_secret)
 
api = twpy.API(auth)
 
try:
    api.verify_credentials()
    print('Successful Authentication')
except:
    print('Failed authentication')

public_tweets = api.home_timeline()

for tweet in public_tweets:
    print(tweet.text)

def authpy(credentials='credentials.json'):
    '''
    Authenticate to Twitter and get API object.
    '''
    creds = read_creds(credentials)
    key, secrets = creds['api_key'], creds['api_secrets']
    tk, tk_secrets = creds['access_token'], creds['access_secret']
 
    # Authenticate to Twitter
    auth = twpy.OAuthHandler(key,secrets)
    auth.set_access_token(tk,tk_secrets)
 
    # Create the API object
    api = twpy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
    return api
 
def read_creds(filename):
    '''
    Read JSON file to load credentials.
    Store API credentials in a safe place.
    If you use Git, make sure to add the file to .gitignore
    '''
    with open(filename) as f:
        credentials = json.load(f)
    return credentials
 
if __name__ == '__main__':
    credentials = 'credentials.json'
    api = authpy(credentials)

def authHeroku(key_var,secret_var,tk_var,tk_s_var):
    '''
    Authenticate to Twitter and get API object.
    '''
    key, secrets = environ[key_var], environ[secret_var]
    tk, tk_secrets = environ[tk_var], environ[tk_s_var]
 
    # Authenticate to Twitter
    auth = twpy.OAuthHandler(key,secrets)
    auth.set_access_token(tk,tk_secrets)
 
    # Create the API object
    api = twpy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
    return api
 
if __name__ == '__main__':
    api = authpy('T_API_KEY','T_API_SECRETS','T_ACCESS_KEY','T_ACCESS_SECRET')
