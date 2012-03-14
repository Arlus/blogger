from django.db import models
import os
#from django.core.urlresolvers import reverse 

def get_image_path(instance, filename):
	return os.path.join('photos', str(instance), filename)

# Create your models here.

class Author(models.Model):
	name = models.CharField(max_length=50)
	slug = models.SlugField(max_length=40, unique=True,help_text='unique value in product page url, created from the name.') 
	def __unicode__(self):
		return self.name
	@models.permalink
	def get_absolute_url(self):
		return ('blog_author', (), {'author_slug' : self.slug})
class Categories(models.Model):
	name = models.CharField(max_length=30)
	description = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField(max_length=40, unique=True,help_text='unique value in product page url, created from the name.')

	def __unicode__(self):
		return self.name
	@models.permalink
	def get_absolute_url(self):
		return ('blog_category', (), {'categories_slug' : self.slug})

	class Meta:
		ordering = ['-date_added']
		verbose_name_plural = 'Categories'
	
class Post(models.Model):
	date = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=70)
	body = models.TextField()
	slug = models.SlugField(max_length=40, unique=True,help_text='unique value in product page url, created from the name.')
	category = models.ForeignKey(Categories)
	author = models.ForeignKey(Author)
	video = models.URLField(blank = True)
	meta_keywords = models.CharField(max_length=255,help_text='Comma-delimited set of SEO keywords for meta tag')
	main_photo = models.ImageField(upload_to = get_image_path)
	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ['-date']

	#@models.permalink
	#def get_absolute_url(self):
		#return ('blog.views.feed', (), {'post_slug':self.slug})
class Comments(models.Model):
	date = models.DateTimeField(auto_now_add=True)
	post = models.ForeignKey(Post)
	comment = models.TextField()
	name = models.CharField(max_length=40)
	email = models.CharField(max_length = 70)
	website = models.URLField(blank = True)
	
	def __unicode__(self):
		return self.comment
	class Meta:
		ordering = ['-date']

class Photos(models.Model):
	image = models.ImageField(upload_to = get_image_path)
	post = models.ForeignKey(Post)
	date = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		verbose_name_plural = 'Photos'

