#DEFAULT SOURCE FROM: https://github.com/pythonanywhere/jab/blob/master/jab/feeds.py
#RESULTS: http://blog.pythonanywhere.com/feed/

from django.conf import settings
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed

from jab.models import Post

# Keep Chrome happy as per http://stackoverflow.com/a/1081023/32846 -- thanks to
# David and Everyblock
class CorrectMimeTypeFeed(Rss201rev2Feed):
    mime_type = 'application/xml'


class LatestEntriesFeed(Feed):
    feed_type = CorrectMimeTypeFeed

    title = settings.BLOG_NAME
    link = "/"
    description = settings.BLOG_DESCRIPTION

    description_template = 'jab/feed_description.html'

    def author_name(self):
        return settings.BLOG_AUTHOR

    def items(self):
        return Post.published_posts().filter(show_in_list_and_rss=True)[:20]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.contents

    def item_author_name(self, item):
        return item.author.username

    def item_pubdate(self, item):
        return item.publication_date
