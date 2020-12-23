import requests
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth.hashers import check_password

from job.models import Company
from job.serializers import CompanySerializer
from p7.models import is_professional, is_company
from pro.models import Professional, ProfessionalSkill
from pro.serializers import ProfessionalSerializer, INACTIVE_USER
from django.conf import settings
from resources.strings_pro import INCORRECT_PASSWORD, NO_SUCH_USER, INACTIVE_COMPANY, INCORRECT_PASSWORD_COMPANY, \
    NO_SUCH_COMPANY


@api_view(["POST"])
@permission_classes(())
def professional_signin(request):
    email = request.data['email']
    password = request.data['password']

    try:
        user = User.objects.get(email=email)
        if not user.is_active :
            raise AuthenticationFailed(INACTIVE_USER)
        elif not check_password(password, user.password) :
            raise AuthenticationFailed(INCORRECT_PASSWORD)
        elif not is_professional(user):
            raise AuthenticationFailed()
    except User.DoesNotExist:
        raise AuthenticationFailed(NO_SUCH_USER)

    if 'device_id' in request.data and request.data['device_id']:
        RefreshToken.lifetime = settings.DEVICE_REFRESH_TOKEN_LIFETIME
        AccessToken.lifetime = settings.DEVICE_ACCESS_TOKEN_LIFETIME
    else:
        RefreshToken.lifetime = settings.WEB_REFRESH_TOKEN_LIFETIME
        AccessToken.lifetime = settings.WEB_ACCESS_TOKEN_LIFETIME

    token=RefreshToken.for_user(user)
    data= {}
    data['username'] = user.username
    data['access'] = str(token.access_token)
    data['refresh'] = str(token)

    pro = Professional.objects.get(user_id = user.id)
    top_skill_count = ProfessionalSkill.objects.filter(professional=pro, is_archived=False, is_top_skill=True).count()

    data['user'] = {
        'id': user.id,
        'email': email,
        'type': 'professional'
    }
    data['pro'] = ProfessionalSerializer(pro, many=False).data
    data['pro'].update({'top_skill_count': top_skill_count})
    data['token_lifetime'] = settings.SIMPLE_JWT
    return Response(data)


@api_view(["POST"])
@permission_classes(())
def company_signin(request):
    email = request.data['email']
    password = request.data['password']

    try:
        user = User.objects.get(email=email)
        if not user.is_active :
            raise AuthenticationFailed(INACTIVE_COMPANY)
        elif not check_password(password, user.password) :
            raise AuthenticationFailed(INCORRECT_PASSWORD_COMPANY)
        elif not is_company(user):
            raise AuthenticationFailed()
    except User.DoesNotExist:
        raise AuthenticationFailed(NO_SUCH_COMPANY)

    if 'device_id' in request.data and request.data['device_id']:
        RefreshToken.lifetime = settings.DEVICE_REFRESH_TOKEN_LIFETIME
        AccessToken.lifetime = settings.DEVICE_ACCESS_TOKEN_LIFETIME
    else:
        RefreshToken.lifetime = settings.WEB_REFRESH_TOKEN_LIFETIME
        AccessToken.lifetime = settings.WEB_ACCESS_TOKEN_LIFETIME

    token = RefreshToken.for_user(user)
    data = {}
    data['username'] = user.username
    data['access'] = str(token.access_token)
    data['refresh'] = str(token)

    company = Company.objects.get(user_id=user.id)
    data['user'] = {
        'id': user.id,
        'email': email,
        'type': 'company'
    }
    data['company'] = CompanySerializer(company, many=False).data
    data['token_lifetime'] = settings.SIMPLE_JWT
    return Response(data)


@api_view(["GET"])
@permission_classes(())
def verify_user(request):
    if request.user.is_anonymous:
        raise AuthenticationFailed()
    data = {
        'id': request.user.id,
        'email': request.user.email,
        'type': 'professional' if is_professional(request.user) else 'company'
    }
    response = Response(data)
    return response

@api_view(["POST"])
@permission_classes(())
def resolve_captcha(request):
    return Response({"Status": "OK"})