import md5
import json
import os.path
import imghdr
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import user_passes_test
from django.core.files.storage import default_storage
from django.http import HttpResponse, HttpResponseForbidden
from django.conf import settings

from forms import ImageForm, FileForm

from sorl.thumbnail import get_thumbnail


UPLOAD_PATH = getattr(settings, 'IMPERAVI_UPLOAD_PATH', os.path.join(settings.MEDIA_ROOT, 'imperavi'))


@require_POST
@csrf_exempt
@user_passes_test(lambda user: user.is_staff)
def upload_image(request, upload_path=None):
    form = ImageForm(request.POST, request.FILES)
    if form.is_valid():
        image = form.cleaned_data['file']
        if image.content_type not in ['image/png', 'image/jpg', 'image/jpeg', 'image/pjpeg']:
            return HttpResponse('Bad image format')
        image_name, extension = os.path.splitext(image.name)
        m = md5.new(image_name)
        hashed_name = '{0}{1}'.format(m.hexdigest(), extension)
        image_path = default_storage.save(os.path.join(upload_path or UPLOAD_PATH, hashed_name), image)
        relative_path = os.path.join(settings.MEDIA_URL, os.path.relpath(image_path, settings.MEDIA_ROOT))
        return HttpResponse('<img src="%s">' % relative_path)
    return HttpResponseForbidden()


@user_passes_test(lambda user: user.is_staff)
def uploaded_images_json(request, upload_path=None):
    upload_path = upload_path or UPLOAD_PATH
    results = list()
    for (path, dirs, files) in os.walk(upload_path):
        for image in files:
            image_path = '{0}/{1}'.format(path, image)
            if imghdr.what(image_path):
                thumb = get_thumbnail(image_path, '100x74', crop='center')
                relative_path = os.path.join(settings.MEDIA_URL, os.path.relpath(image_path, settings.MEDIA_ROOT))
                results.append({'thumb': thumb.url, 'image': relative_path})
    return HttpResponse(json.dumps(results))


@require_POST
@csrf_exempt
@user_passes_test(lambda user: user.is_staff)
def upload_file(request, upload_path=None, upload_link=None):
    form = FileForm(request.POST, request.FILES)
    if form.is_valid():
        uploaded_file = form.cleaned_data['file']
        path = os.path.join(upload_path or UPLOAD_PATH, uploaded_file.name)
        real_path = default_storage.save(path, uploaded_file)
        relative_path = os.path.join(settings.MEDIA_URL, os.path.relpath(real_path, settings.MEDIA_ROOT))
        if upload_link:
            return HttpResponse(relative_path)
        return HttpResponse('<a href="%s">%s</a>' % (relative_path, uploaded_file.name))
    return HttpResponseForbidden()
