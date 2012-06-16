import json
from django.forms.widgets import Textarea
from django.forms.util import flatatt
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape
from django.utils.encoding import force_unicode
from django.core.urlresolvers import reverse
from django.conf import settings

from views import UPLOAD_PATH


IMPERAVI_SETTINGS = getattr(settings, 'IMPERAVI_CUSTOM_SETTINGS', {})


class ImperaviWidget(Textarea):

    def __init__(self, *args, **kwargs):
        self.upload_path = kwargs.pop('upload_path', UPLOAD_PATH)
        self.imperavi_settings = IMPERAVI_SETTINGS
        super(ImperaviWidget, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        field_id = final_attrs.get('id')
        self.imperavi_settings.update({
            'imageUpload': reverse('imperavi-upload-image', kwargs={'upload_path': self.upload_path}),
            'imageGetJson': reverse('imperavi-get-json', kwargs={'upload_path': self.upload_path}),
            'fileUpload': reverse('imperavi-upload-file', kwargs={'upload_path': self.upload_path}),
            'linkFileUpload': reverse('imperavi-upload-link-file', kwargs={'upload_path': self.upload_path}),
        })
        imperavi_settings = json.dumps(self.imperavi_settings)
        return mark_safe(u"""
            <div style="width: 800px;">
                <textarea%(attrs)s>%(value)s</textarea>
            </div>
            <script>
                $(document).ready(
                    function() {
                        $("#%(id)s").parent().siblings('label').css('float', 'none');
                        $("#%(id)s").height(300);
                        $("#%(id)s").redactor(%(imperavi_settings)s);
                    }
                );
            </script>
            """ % {
                'attrs': flatatt(final_attrs),
                'value': conditional_escape(force_unicode(value)),
                'id': field_id,
                'imperavi_settings': imperavi_settings,
            }
        )
