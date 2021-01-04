from django.conf import settings

def footer_context(request):
    return {'APP_VERSION_NUMBER': settings.APP_VERSION_NUMBER}

def media_context(request):
    return {'MEDIA_BUCKET_URL_PREFIX': settings.MEDIA_BUCKET_URL_PREFIX}

def static_context(request):
    return {'STATIC_CLOUD_FONT_URL_PREFIX': settings.STATIC_URL}
