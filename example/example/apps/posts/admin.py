from django.contrib import admin

from models import Article, Post
from imperavi.admin import ImperaviAdmin, ImperaviStackedInlineAdmin


class PostInline(ImperaviStackedInlineAdmin):
    model = Post
    extra = 1


class ArticleAdmin(ImperaviAdmin):
    inlines = (PostInline,)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Post)
