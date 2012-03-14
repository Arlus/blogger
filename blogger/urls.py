from django.conf.urls.defaults import patterns, include, url
from blogger import settings
from blogger.feeds import LatestPostFeed
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from blogger.feeds import LatestPostFeed

feeds = {
	'latest' : LatestPostFeed,
}

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blogger.views.home', name='home'),
    # url(r'^blogger/', include('blogger.foo.urls')),
      (r'^', include('blogger.blog.urls')),
      (r'^captcha/', include('captcha.urls')),
      (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
      (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
