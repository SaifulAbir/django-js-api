import requests
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group, User
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_401_UNAUTHORIZED,
    HTTP_200_OK,
    HTTP_404_NOT_FOUND
)
from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
import logging

from account.models import TransactionHistory
from job.models import Company
from job.serializers import CompanySerializer
from p7.models import get_user_address, is_professional, is_company
from p7.utils import *
from pro.models import Professional
from pro.serializers import ProfessionalSerializer
from django.conf import settings


@api_view(["GET"])
@permission_classes(())
def isLoggedIn(request):
    data = []
    if not request.user.is_authenticated:
        return Response(HTTP_401_UNAUTHORIZED)
    elif request.user.is_authenticated:
        professional = Professional.objects.get(user = request.user)
        data.append({'user':{'name':professional.full_name,'email':professional.email,'id':professional.id,'image':professional.image}})
        return JsonResponse(list(data), safe=False)
    return Response(HTTP_200_OK)

@api_view(["POST"])
@permission_classes(())
def send_email_to_admin_contact_us(request):
    data = json.loads(request.body)
    name = data['name']
    email = data['email']
    phone = data['phone']
    subject = data['subject']
    message = data['message']

    if name and email and phone and subject and message:
        status = sendContactUsEmail(name, email, subject, phone, message)
    else:
        return Response(HTTP_404_NOT_FOUND)

    if status:
        return Response(HTTP_200_OK)
    else:
        return Response(HTTP_404_NOT_FOUND)

class GoogleSigninProApi(APIView):
    permission_classes = ()
    authentication_classes = ()
    def post(self, request):
        payload = {'access_token': request.data.get("token")}  # validate the token
        r = requests.get('https://www.googleapis.com/oauth2/v2/userinfo', params=payload)
        data = json.loads(r.text)

        if 'error' in data:
            content = {'message': 'wrong google token / this google token is already expired.'}
            return Response(content)
        pro = Professional.objects.filter(email=data['email']).first()
        # create user if not exist
        try:
            user = User.objects.get(email=data['email'])
            if not is_professional(user):
                raise AuthenticationFailed()
        except User.DoesNotExist:
            user = User()
            user.username = data['email']
            # provider random default password
            user.password = make_password(BaseUserManager().make_random_password())
            user.email = data['email']
            user.is_active = 1
            user.save()
            pro_group = Group.objects.get(name='Professional')
            user.groups.add(pro_group)

            if not pro:
                pro = Professional(
                    full_name=data['name'],
                    email=data['email'],
                    password=user.password,
                    terms_and_condition_status= 1
                )
                pro.user_id = user.id
                pro.created_by = user.id
                pro.created_from = get_user_address(request)
                pro.job_alert_status = True
                pro.save()

        token = RefreshToken.for_user(user)  # generate token without username & password

        data = {}
        data['username'] = user.username
        data['access'] = str(token.access_token)
        data['refresh'] = str(token)

        data['user'] = {
            'id': user.id,
            'email': user.email,
            'type': 'professional'
        }
        data['pro'] = ProfessionalSerializer(pro, many=False).data
        data['token_lifetime'] = settings.SIMPLE_JWT
        return Response(data)

class GoogleSigninCompanyApi(APIView):
    permission_classes = ()
    authentication_classes = ()
    def post(self, request):
        payload = {'access_token': request.data.get("token")}  # validate the token
        r = requests.get('https://www.googleapis.com/oauth2/v2/userinfo', params=payload)
        data = json.loads(r.text)

        if 'error' in data:
            content = {'message': 'wrong google token / this google token is already expired.'}
            return Response(content)
        # create user if not exist
        try:
            user = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            raise AuthenticationFailed()

        if not is_company(user):
            raise AuthenticationFailed()

        token = RefreshToken.for_user(user)  # generate token without username & password
        data = {}
        data['username'] = user.username
        data['access'] = str(token.access_token)
        data['refresh'] = str(token)

        company = Company.objects.get(user_id=user.id)
        data['user'] = {
            'id': user.id,
            'email': user.email,
            'type': 'company'
        }
        data['company'] = CompanySerializer(company, many=False).data
        data['token_lifetime'] = settings.SIMPLE_JWT
        return Response(data)




class IpnAPI(APIView):
    permission_classes = []
    def post(self, request, *args, **kwargs):
        data = request.data
        response = str(request.data)
        logging.warning(logging.INFO, 'ipn response')
        logging.warning(logging.INFO, response)
        # status = data['status']
        # amount = data['amount']
        # store_amount = data['store_amount']
        # tran_date = data['tran_date']
        # tran_histories = TransactionHistory(**data)
        # tran_histories.save()

        return Response(request.data)


@api_view(["GET"])
@permission_classes(())
def ping(request):
    data = {
        'version': settings.APP_VERSION_NUMBER,
    }
    response = Response(data)
    return response