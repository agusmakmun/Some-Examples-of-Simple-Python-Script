"""
See tutorial: 
- https://python.web.id/blog/cara-menggunakan-tweepy/
- https://python.web.id/blog/filter-timeline-twitter-menggunakan-tweepy/
"""

import tweepy
import requests
from tweepy.auth import OAuthHandler
requests.packages.urllib3.disable_warnings()
 
# Consumer keys and access tokens, used for OAuth
consumer_key = 'JNT2qhC2noSTSya'
consumer_secret = 'YibVMiytGm2qWCun83cYjH'
access_token = '1746506726-Jx7xPaH63tNC40JO2Q'
access_token_secret = 'LDg6sOkOKlMEO9TSchDDbyZH'

# OAuth process, using the keys and tokens
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

data_status_asli = open("status_asli.txt", "w")
public_tweets = api.home_timeline()
out = ''
for tweet in public_tweets:
    user = tweet.user.name.encode('utf-8')
    status = tweet.text.encode('utf-8')
    out += str(user) +" : "+str(status) + "\n"
data_status_asli.write(out)
data_status_asli.close()
