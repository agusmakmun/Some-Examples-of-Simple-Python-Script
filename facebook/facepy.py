"""
https://www.facebook.com/settings?tab=applications&section=all   --> change to public access.
http://facepy.readthedocs.org/en/latest/usage/graph-api.html     --> docs graph api.
https://developers.facebook.com/tools/explorer/                  --> change to allow some premission.
https://github.com/jgorset/facepy                                --> repository.
http://python.web.id/blog/menggunakan-graph-api-facebook-sangat-mudah-dengan-facepy/
"""

from facepy import GraphAPI
ACCESS_TOKEN = 'tokentokentokentoken'
ID_GROUP_OR_PAGE = '1234567890'
graph = GraphAPI(ACCESS_TOKEN)

graph.post(ID_GROUP_OR_PAGE+'/feed', message='Test My Status on Group/Pages')
graph.post('me/feed', message='Test My Status')
