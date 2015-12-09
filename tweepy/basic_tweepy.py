"""
See tutorial: 
- https://python.web.id/blog/cara-menggunakan-tweepy/
- https://python.web.id/blog/filter-timeline-twitter-menggunakan-tweepy/
"""

import tweepy

# Consumer keys and access tokens, used for OAuth
consumer_key = 'JNT2qhC2noSTSya'
consumer_secret = 'YibVMiytGm2qWCun83cYjU4'
access_token = '1746506726-Jx7xPaH63tNC40JC'
access_token_secret = 'LDg6sOkOKlMEO9TSchDDb'

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# Sample method, used to update a status
api.update_status('Test Status using tweepy, hurray!!')
