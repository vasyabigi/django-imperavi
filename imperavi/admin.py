from django.contrib import admin
from django.db.models import TextField

from imperavi.widget import ImperaviWidget


class ImperaviAdmin(admin.ModelAdmin):
    unique_media = False
    formfield_overrides = {
        TextField: {'widget': ImperaviWidget},
    }

    class Media:
        js = ('imperavi/jquery.js',)
        css = {'all': ('imperavi/django_admin.css',)}

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(ImperaviAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if getattr(field, 'widget', False) and field.widget.__class__ == ImperaviWidget and self.unique_media:
            field.widget.upload_path += '%s/' % db_field.model.__name__.lower()
        return field


class ImperaviStackedInlineAdmin(admin.StackedInline):
    unique_media = False
    formfield_overrides = {
        TextField: {'widget': ImperaviWidget},
    }

    class Media:
        js = ('imperavi/jquery.js',)
        css = {'all': ('imperavi/django_admin.css',)}

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(ImperaviStackedInlineAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if getattr(field, 'widget', False):
            if field.widget.__class__ == ImperaviWidget and self.unique_media:
                field.widget.upload_path += '%s/' % db_field.model.__name__.lower()
        return field
