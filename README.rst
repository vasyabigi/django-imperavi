Django Imperavi editor
================
**Django admin WYSIWYG Imperavi editor integration.**

Installation
------------

#. Install or add ``django-imperavi`` to your python path.

#. Add ``imperavi`` to your ``INSTALLED_APPS`` setting.

#. Add imperavi URL include to your project's ``urls.py`` file::

    url(r'^imperavi/', include('imperavi.urls')),

Usage
-----

The quickest way to add rich text editing capabilities to your admin is to use the included ``ImperaviAdmin`` class. For example::

    from models import Article
    from imperavi.admin import ImperaviAdmin

    class ArticleAdmin(ImperaviAdmin):
        pass

    admin.site.register(Article, ArticleAdmin)

More information will be soon...
