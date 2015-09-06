from django.contrib import admin

# Register your models here.
from .models import Blog,News,Category,Skill,Project


class BlogAdmin(admin.ModelAdmin):
	fieldsets = [(None, {'fields': ['post_author','post_title',"post_content","post_photo","post_category","post_tags","category"]}),
	]

	list_display = ('post_author', 'post_title', 'post_content','post_photo','post_category','post_tags')
	list_editable = ('post_title', 'post_content','post_photo','post_category','post_tags')
	list_filter = ['post_published']
	search_fields = ['post_title', 'post_content']

class ProjectAdmin(admin.ModelAdmin):

	exclude = ('slug',)

class NewsAdmin(admin.ModelAdmin):

	exclude = ('slug',)

class SkillAdmin(admin.ModelAdmin):

	exclude = ('slug',)

class CategoryAdmin(admin.ModelAdmin):

	exclude = ('slug',)

admin.site.register(Blog,BlogAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Skill,SkillAdmin)
admin.site.register(Project,ProjectAdmin)


