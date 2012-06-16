from django.conf.urls import patterns, url

from views import upload_image, uploaded_images_json, upload_file

urlpatterns = patterns('',
    url(r'^upload-image/(?P<upload_path>.*)', upload_image, name="imperavi-upload-image"),
    url(r'^get-json/(?P<upload_path>.*)', uploaded_images_json, name="imperavi-get-json"),
    url(r'^upload-file/(?P<upload_path>.*)', upload_file, name="imperavi-upload-file"),
    url(r'^upload-link-file/(?P<upload_path>.*)', upload_file, {'upload_link': True}, name="imperavi-upload-link-file"),
)
