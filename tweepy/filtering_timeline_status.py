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
consumer_key = 'JNT2qhC2noS'
consumer_secret = 'YibVMiytGm2qWCu'
access_token = '1746506726-Jx7xPaH63tNC40'
access_token_secret = 'LDg6sOkOKlMEO9TSch'

# OAuth process, using the keys and tokens
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)

data_status_asli = open("status_di_filter.txt", "w")
public_tweets = api.home_timeline()
out = ''
status_baik = ["baik", "assalamualaikum", "dateng"]
status_buruk = ["buruk", "asem", "ente", "cekidot"]
for tweet in public_tweets:
    user = tweet.user.name.encode('utf-8')
    status = tweet.text.encode('utf-8')
    cek_status = str(status).lower().split()
    filter_status = ''
    for stat in cek_status:
        if stat in status_baik and stat not in status_buruk:
            filter_status = " --> Ini status baik!"
        elif stat in status_buruk and stat not in status_baik:
            filter_status = " --> Ini status buruk!"
        else:
            pass
    out += str(user) +" : "+str(status) + filter_status + "\n"
data_status_asli.write(out)
data_status_asli.close()
