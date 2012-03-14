from django.contrib import admin
from blogger.blog.models import Author, Post, Categories, Photos
from blogger.blog.forms import PostAdminForm


class PhotosInline(admin.TabularInline):
	model = Photos

class PostAdmin(admin.ModelAdmin):
	form = PostAdminForm
	inlines = [PhotosInline,]
	list_display = ('title','slug', 'author', 'meta_keywords')
	list_per_page = 50
	ordering = ['-date']
	search_fields = ['title', 'author', 'meta_keywords']
	prepopulated_fields = {'slug' : ('title',)}

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug' : ('name',)}
	search_fields = ['category']

class AuthorAdmin (admin.ModelAdmin):
	prepopulated_fields = {'slug' : ('name',)}


admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Categories, CategoryAdmin)
admin.site.register(Photos)
