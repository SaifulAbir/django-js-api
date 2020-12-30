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
        amount = data['amount']
        bank_tran_id = data['bank_tran_id']
        card_brand = data['card_brand']
        card_issuer = data['card_issuer']
        card_issuer_country = data['card_issuer_country']
        card_issuer_country_code = data['card_issuer_country_code']
        card_no = data['card_no']
        card_type = data['card_type']
        currency = data['currency']
        currency_amount = data['currency_amount']
        currency_type = data['currency_type']
        risk_level = data['risk_level']
        risk_title = data['risk_title']
        status = data['status']
        store_amount = data['store_amount']
        store_id = data['store_id']
        tran_date = data['tran_date']
        tran_id = data['tran_id']
        # tran_histories = TransactionHistory(**data)
        # tran_histories.save()

        return Response(request.data)



<QueryDict: {'amount': ['3.00'], 'bank_tran_id': ['2012301848220s2dvMXwnqmJT3x'],
             'base_fair': ['0.00'], 'card_brand': ['MOBILEBANKING'],
             'card_issuer': ['BKash Mobile Banking'], 'card_issuer_country': ['Bangladesh'],
             'card_issuer_country_code': ['BD'], 'card_no': [''], 'card_sub_brand': ['Classic'],
             'card_type': ['BKASH-BKash'], 'currency': ['BDT'], 'currency_amount': ['3.00'],
             'currency_rate': ['1.0000'], 'currency_type': ['BDT'], 'error': [''],
             'risk_level': ['0'], 'risk_title': ['Safe'], 'status': ['VALID'], 'store_amount': ['2.93'],
             'store_id': ['jobxp5fcdcfa69d176'], 'tran_date': ['2020-12-30 18:47:57'],
             'tran_id': ['82deb504-bc71-4b00-85c4-fbd6277efff4-301220-184433'], 'val_id': ['2012301848226v3nifmc7S7EhOz'], 'value_a': [''], 'value_b': [''], 'value_c': [''], 'value_d': [''], 'verify_sign': ['a40563f69f6570cadb047f03f517ef73'], 'verify_sign_sha2': ['5a34d1b52cc440df9a09f363d85ebdc7a85495ba00e98310726e857bb88ae498'], 'verify_key': ['amount,bank_tran_id,base_fair,card_brand,card_issuer,card_issuer_country,card_issuer_country_code,card_no,card_sub_brand,card_type,currency,currency_amount,currency_rate,currency_type,error,risk_level,risk_title,status,store_amount,store_id,tran_date,tran_id,val_id,value_a,value_b,value_c,value_d']}>
@api_view(["GET"])
@permission_classes(())
def ping(request):
    data = {
        'version': settings.APP_VERSION_NUMBER,
    }
    response = Response(data)
    return response