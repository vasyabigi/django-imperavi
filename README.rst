Django Imperavi editor
======================

Installation
------------

#. Install or add ``django-imperavi`` to your python path.

#. Add ``imperavi`` to your ``INSTALLED_APPS`` setting.

#. Add imperavi URL include to your project's ``urls.py`` file::

    url(r'^imperavi/', include('imperavi.urls')),

Usage
-----

The quickest way to add rich text editing capabilities to your admin is to use the included ``ImperaviAdmin`` class. For example::

    from models import Category
    from imperavi.admin import ImperaviAdmin

    class CategotyAdmin(ImperaviAdmin):
        pass

    admin.site.register(Category, CategotyAdmin)

If you want to use it with inline admin models you need to use ``ImperaviStackedInlineAdmin`` class::

    from models import Post
    from imperavi.admin import ImperaviStackedInlineAdmin

    class PostInline(ImperaviStackedInlineAdmin):
        model = Post
        extra = 1

Custom settings
---------------

Add a ``IMPERAVI_CUSTOM_SETTINGS`` variable to your ``settings.py`` with custom config::

    IMPERAVI_CUSTOM_SETTINGS = {
        'lang': 'ua',
        'toolbar': 'mini',
        'resize': true
    }

Full list of settings is `here.
<http://redactorjs.com/docs/settings/>`_

Media URL
---------

You can also customize the URL that django-imperavi will look for the Editor media at by adding ``IMPERAVI_UPLOAD_PATH`` to your ``settings.py`` file like this::

    IMPERAVI_UPLOAD_PATH = 'imperavi-uploads/'

The default value is ``'imperavi/'``.


Unique images per model
-----------------------

If you want to serve unique media content for specific model you can add ``unique_media = True`` to your admin class::

    from models import Category
    from imperavi.admin import ImperaviAdmin

    class CategotyAdmin(ImperaviAdmin):
        unique_media = True

    admin.site.register(Category, CategotyAdmin)
