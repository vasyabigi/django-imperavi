from django.contrib import admin

from models import Category, Post
from imperavi.admin import ImperaviAdmin, ImperaviStackedInlineAdmin


class PostInline(ImperaviStackedInlineAdmin):

    unique_media = True

    model = Post
    extra = 1


class CategoryAdmin(ImperaviAdmin):

    inlines = (PostInline,)

admin.site.register(Category, CategoryAdmin)


class PostAdmin(ImperaviAdmin):

    unique_media = True

admin.site.register(Post, PostAdmin)
