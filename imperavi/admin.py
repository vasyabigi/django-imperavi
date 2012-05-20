from django.contrib import admin
from django.db.models import TextField
from django.conf import settings

from widget import ImperaviWidget


class ImperaviAdmin(admin.ModelAdmin):

    formfield_overrides = {
        TextField: {'widget': ImperaviWidget},
    }

    class Media:
        js = (
            '%simperavi/force_jquery.js' % settings.STATIC_URL,
            '%simperavi/redactor/redactor.min.js' % settings.STATIC_URL,
        )
        css = {
            'all': (
                "%simperavi/redactor/css/redactor.css" % settings.STATIC_URL,
            ),
        }


class ImperaviStackedInlineAdmin(admin.StackedInline):

    formfield_overrides = {
        TextField: {'widget': ImperaviWidget},
    }

    class Media:
        js = (
            '%simperavi/force_jquery.js' % settings.STATIC_URL,
            '%simperavi/redactor/redactor.js' % settings.STATIC_URL,
        )
        css = {
            'all': (
                "%simperavi/redactor/css/redactor.css" % settings.STATIC_URL,
            ),
        }
