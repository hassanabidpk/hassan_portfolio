from django.contrib import admin

# Register your models here.
from .models import Post,News,Category,Skill,Project

class CategoryInline(admin.TabularInline):
	model = Post.category.through
	extra = 1

class PostAdmin(admin.ModelAdmin):
	fieldsets = [(None, {'fields': ['post_author','post_title',"post_content","post_photo"]}),
	]

	list_display = ('post_author', 'post_title', 'post_content','post_photo')
	list_editable = ('post_title', 'post_content','post_photo')
	list_filter = ['post_published']
	search_fields = ['post_title', 'post_content']
	inlines = (CategoryInline,)

class ProjectAdmin(admin.ModelAdmin):

	exclude = ('slug',)

class NewsAdmin(admin.ModelAdmin):

	exclude = ('slug',)

class SkillAdmin(admin.ModelAdmin):
	fieldsets = [(None, {'fields': ['title','related_projects',"logo","term"]}),
	]
	list_display = ('title','related_projects','logo','term')
	list_editable = ('title','related_projects','logo','term')
	list_filter = ['title']
	exclude = ('slug',)

class CategoryAdmin(admin.ModelAdmin):

	exclude = ('slug',)

# admin.site.register(Post,PostAdmin)
admin.site.register(Post)
admin.site.register(News, NewsAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Skill,SkillAdmin)
admin.site.register(Project,ProjectAdmin)
