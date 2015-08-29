from django.contrib import admin

# Register your models here.
from .models import Blog,News


class BlogAdmin(admin.ModelAdmin):
	fieldsets = [(None, {'fields': ['post_author','post_title',"post_content","post_photo","post_category","post_tags"]}),
	('Date Information',{ 'fields': ['post_published'], 'classes': ['collapse']}),]

	list_display = ('post_author', 'post_title', 'post_content','post_photo','post_category','post_tags','post_published','post_modified')
	list_editable = ('post_title', 'post_content','post_photo','post_category','post_tags')
	list_filter = ['post_modified','post_published']
	search_fields = ['post_title', 'post_content']

admin.site.register(Blog,BlogAdmin)

