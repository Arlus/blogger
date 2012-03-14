from blogger.blog.models import Post, Photos, Categories
from blogger import settings

def posts(request):
	return {
		'posts' : Post.objects.all(),
		'request' : request,
		'photos' : Photos.objects.all(),
		'categories' : Categories.objects.all(),
	}
