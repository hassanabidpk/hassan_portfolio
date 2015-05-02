from django.contrib import admin

# Register your models here.
from .models import Resume, Views,Blog,News


class ViewsInline(admin.TabularInline):
	model = Views
	extra = 1

class ResumeAdmin(admin.ModelAdmin):
	fieldsets = [(None, {'fields': ['first_name','last_name']}),
	('Date Information',{ 'fields': ['pub_date'], 'classes': ['collapse']}),]
	inlines = [ViewsInline]
	list_display = ('first_name', 'last_name', 'pub_date','was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['first_name', 'last_name']

class BlogAdmin(admin.ModelAdmin):
	fieldsets = [(None, {'fields': ['post_author','post_title',"post_content"]}),
	('Date Information',{ 'fields': ['post_published'], 'classes': ['collapse']}),]

	list_display = ('post_author', 'post_title', 'post_content','post_published','post_modified')
	list_filter = ['post_modified','post_published']
	search_fields = ['post_title', 'post_content']

admin.site.register(Resume,ResumeAdmin)
admin.site.register(Views)
admin.site.register(Blog,BlogAdmin)

