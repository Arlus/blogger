# Create your views here.

from django.shortcuts import get_object_or_404, render_to_response, render
from blogger.blog.models import Author, Post, Comments, Photos, Categories
from django.template import RequestContext
from blogger.blog.forms import CommentForm
from django.http import HttpResponseRedirect
from django import forms
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def feed(request, post_slug):
	posts = Post.objects.all()
	return render_to_response('blog/feed.html', locals(), context_instance=RequestContext(request))

def index(request, template_name="blog/index.html"):
	page_title = 'BLOG'
	display = Post.objects.all()
	dates = Post.objects.dates('date','month')
	paginator = Paginator(display,2)
	page = request.GET.get('page')
	
	try:
		item = paginator.page(page)
	except TypeError:
		item = paginator.page(1)
	except PageNotAnInteger:
		item = paginator.page(1)
	except EmptyPage:
		item = paginator.page(paginator.num_pages)
	posts = item.object_list
	cats = Categories.objects.all()
	return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def full_post(request, post_slug, template_name="blog/full.html"):
	c = get_object_or_404(Post, slug=post_slug)
	main = c.main_photo
	article = c.body
	categs = Categories.objects.all()
	post_in_picture = Post.objects.get(slug = post_slug)
	commes = Comments.objects.filter(post = post_in_picture)
	paginator = Paginator(commes,1)
	page = request.GET.get('page')
	try:
		item = paginator.page(page)
	except TypeError:
		item = paginator.page(1)
	except PageNotAnInteger:
		item = paginator.page(1)
	except EmptyPage:
		item = paginator.page(paginator.num_pages)
	comm = item.object_list
	snaps = Photos.objects.filter(post = post_in_picture)
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			p = Post.objects.get(slug = post_slug)
			saves = Comments(post = p, name = cd['name'], comment = cd['comment'], email = cd['Email'], website = cd['website'])
			saves.save()
			messages.add_message(request, messages.SUCCESS, 'comment posted')
			return render_to_response(template_name, locals(),context_instance=RequestContext(request))			
	else:			
		form = CommentForm()
	return render_to_response(template_name, locals(),context_instance=RequestContext(request))

def related(request, post_slug, template_name='blog/related.html'):
	base = Post.objects.get(slug=post_slug)
	meta_list = base.meta_keywords.split()
	categs = Categories.objects.all()
	output = []
	other = Post.objects.all()
	for i in other:
		other_list = i.meta_keywords.split()
		test = bool(set(meta_list)&set(other_list))
		test
		if test==True:
			output.append(i)
	if (len(output)==0):
		output.append(base)			
	return render_to_response(template_name, locals(), context_instance=RequestContext(request))
	
def categor(request, categories_slug, template_name='blog/category.html'):
		catr = Categories.objects.get(slug = categories_slug)
		cat_list = Categories.objects.all()
		p = Post.objects.filter(category = catr)
		paginator = Paginator(p,2)
		page = request.GET.get('page')
		try:
			nav = paginator.page(page)
		except TypeError:
			nav = paginator.page(1)
		except PageNotAnInteger:
			nav = paginator.page(1)
		except EmptyPage:
			nav = paginator.page(paginator.num_pages)
		return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def author_posts(request, author_slug, template_name='blog/author_posts.html'):
	gets = Author.objects.get(slug = author_slug)
	post_list = Post.objects.all()
	cat_list = Categories.objects.all()
	wanted = Post.objects.filter(author = gets)
	paginator = Paginator(wanted,2)
	page = request.GET.get('page')
	try:
		nav = paginator.page(page)
	except TypeError:
		nav = paginator.page(1)
	except PageNotAnInteger:
		nav = paginator.page(1)
	except EmptyPage:
		nav = paginator.page(paginator.num_pages)
	return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def archive(request, month, template_name='blog/archives.html'):
	coll = Post.objects.all()
	mon = int(month)
	arch = []
	cats = Categories.objects.all()
	dates = Post.objects.dates('date','month')
	for i in coll:
		tria = i.date.month
		trial = int(tria)
		if (trial == mon):
			arch.append(i)
	return render_to_response(template_name, locals(), context_instance=RequestContext(request))
		
