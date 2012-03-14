
from django.conf.urls.defaults import *

urlpatterns = patterns('blogger.blog.views',
	(r'^$', 'index', {'template_name' : 'blog/index.html'}),
	(r'^article/(?P<post_slug>[-\w]+)/$', 'full_post', {'template_name' : 'blog/full.html'}, 'full_post'),
	(r'^(?P<post_slug>[-\w]+)/related/$', 'related', {'template_name' : 'blog/related.html'}),
	(r'^category/(?P<categories_slug>[-\w]+)/$', 'categor', {'template_name' : 'blog/category.html'}),
	(r'^author/(?P<author_slug>[-\w]+)/$', 'author_posts', {'template_name' : 'blog/author_posts.html'}),
	(r'^(?P<month>\d+)/$', 'archive', {'template_name' : 'blog/archives.html'}),
	
)
