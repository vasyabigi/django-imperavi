import json
from django.forms.widgets import Textarea
from django.forms.util import flatatt
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape
from django.utils.encoding import force_unicode
from django.core.urlresolvers import reverse
from django.conf import settings

from imperavi.views import UPLOAD_PATH


IMPERAVI_SETTINGS = getattr(settings, 'IMPERAVI_CUSTOM_SETTINGS', {})

INIT_JS = """<script src="%(static_url)simperavi/redactor/langs/%(lang)s.js"></script>
<script type="text/javascript">
  jQuery(document).ready(function(){
    $("#%(field_id)s").redactor(%(settings)s);
  });
</script>
"""


class ImperaviWidget(Textarea):

    class Media:
        js = ('imperavi/redactor/redactor.min.js',)
        css = {'all': ('imperavi/redactor/css/redactor.css',)}

    def __init__(self, *args, **kwargs):
        self.upload_path = kwargs.pop('upload_path', UPLOAD_PATH)
        self.custom_settings = kwargs.pop('imperavi_settings', {})
        super(ImperaviWidget, self).__init__(*args, **kwargs)

    def get_settings(self):
        imperavi_settings = IMPERAVI_SETTINGS.copy()
        imperavi_settings.update({
            'imageUpload': reverse('imperavi-upload-image', kwargs={'upload_path': self.upload_path}),
            'imageGetJson': reverse('imperavi-get-json', kwargs={'upload_path': self.upload_path}),
            'fileUpload': reverse('imperavi-upload-file', kwargs={'upload_path': self.upload_path}),
            'linkFileUpload': reverse('imperavi-upload-link-file', kwargs={'upload_path': self.upload_path}),
        })
        imperavi_settings.update(self.custom_settings)
        return imperavi_settings

    def render(self, name, value, attrs=None):
        html = super(ImperaviWidget, self).render(name, value, attrs)
        final_attrs = self.build_attrs(attrs, name=name)
        field_id = final_attrs.get('id')
        imperavi_settings = self.get_settings()
        html += INIT_JS % {
            'static_url': settings.STATIC_URL,
            'lang': imperavi_settings['lang'],
            'field_id': field_id,
            'settings': json.dumps(imperavi_settings),
        }
        return mark_safe(html)
