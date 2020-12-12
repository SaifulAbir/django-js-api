from django.conf import settings

def footer_context(request):
    return {'APP_VERSION_NUMBER': settings.APP_VERSION_NUMBER}