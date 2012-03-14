from django.contrib.syndication.feeds import Feed
from blogger.blog.models import Post
from django.contrib.syndication.feeds import Feed
from django.contrib.syndication.feeds import FeedDoesNotExist


class LatestPostFeed(Feed):
	title = "Localhost articles"
	link = "/feeds/"
	description = "Updates on new posts"

	def items(self):
		return Post.objects.all().order_by('-date')[:5]

	def item_link(self):
		return '/feeds/'

