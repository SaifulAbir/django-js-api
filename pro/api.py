from django.db.models import Q, Count
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.status import (
    HTTP_200_OK
)
from rest_framework.utils import json
from rest_framework.views import APIView

from job.models import JobRecommendation
from job.serializers import JobSerializer
from p7.permissions import StaffPermission
from p7.socket_client import SocketClient
from pro.serializers import *
from pro.utils import job_alert_save
from resources.strings_pro import *


def logout(request):
    response = HttpResponseRedirect('/')
    response.delete_cookie('access')
    response.delete_cookie('refresh')
    response.delete_cookie('user')
    response.delete_cookie('user_id')
    response.delete_cookie('email')
    response.delete_cookie('user_type')
    response.delete_cookie('name')
    response.delete_cookie('phone')
    response.delete_cookie('professional_id')
    response.delete_cookie('slug')
    response.delete_cookie('image')
    response.delete_cookie('access_lifetime_hr')
    response.delete_cookie('company_name')
    response.delete_cookie('company_picture')
    response.delete_cookie('city')
    response.delete_cookie('refresh_expires_at')
    return response


@api_view(["POST"])
def job_alert(request):
    user_email = json.loads(request.body)
    data = {}
    if user_email['email'] and not request.user.is_authenticated:
        try:
            sub_user = Professional.objects.get(email = user_email['email'], job_alert_status = True)
        except Professional.DoesNotExist:
            sub_user = None
        try:
            not_sub_user = Professional.objects.get(email = user_email['email'])
        except Professional.DoesNotExist:
            not_sub_user = None
        if sub_user:
            data = {
                'status': SUBSCRIBED_TXT,
                'code': HTTP_200_OK,
                "result": {
                    "user": {
                        "email": user_email['email'],
                        "job_alert": sub_user.job_alert_status
                    }
                }
            }
        elif not_sub_user:
            data = {
                'status': NOT_SUBSCRIBED_TXT,
                'code': HTTP_200_OK,
                "result": {
                    "user": {
                        "email": user_email['email'],
                    }
                }
            }
        else:
            data = {
                'status': NOT_USER_TXT,
                'code': HTTP_200_OK,
                "result": {
                    "user": {
                        "email": user_email['email'],
                    }
                }
            }
    if request.user.is_authenticated:
        job_alert_save(user_email['email'])
        try:
            sub_user = Professional.objects.get(email = user_email['email'], job_alert_status = True)
        except Professional.DoesNotExist:
            sub_user = None

        if sub_user:
            data = {
                'status': NOT_SUBSCRIBED_USER_TXT,
                'code': HTTP_200_OK,
                "result": {
                    "user": {
                        "email": user_email['email'],
                        "job_alert": sub_user.job_alert_status
                    }
                }
            }
    return Response(data)


@api_view(["GET"])
@permission_classes(())
def job_alert_notification(request):
    data = {}
    if request.user.is_authenticated:
        try:
            user = Professional.objects.get(user = request.user)
        except Professional.DoesNotExist:
            user = None

        if user.job_alert_status == True:
            data = {
                'status': SUBSCRIBED_TXT,
                'code': HTTP_200_OK,
                "result": {
                    "user": {
                        "email": user.email,
                    }
                }
            }
        else:
            data = {
                'status': NOT_SUBSCRIBED_TXT,
                'code': HTTP_200_OK,
                "result": {
                    "user": {
                        "email": user.email,
                    }
                }
            }

    else:
        data = {
                'status': NOT_USER_TXT,
                'code': HTTP_401_UNAUTHORIZED,
                "result": {
                }
            }
    return Response(data)




def StaticUrl(self):
    data = {
        '1': "http://facebook.com/",
        '2': "http://twitter.com/",
        '3': "http://linkedin.com/",

    }
    return HttpResponse(json.dumps(data), content_type='application/json')


class RecentActivityAPI(APIView):

    def get(self, request):
        user = request.user
        activity = RecentActivity.objects.filter(user = user).order_by('-time')[:20]
        for obj in activity:
            if (timezone.now() - obj.time).days >=1:
                obj.activity_time = '{} days ago'.format((timezone.now() - obj.time).days)
            elif (((timezone.now() - obj.time).seconds)//3600) >=1:
                obj.activity_time = '{} hour ago'.format(((timezone.now() - obj.time).seconds) //3600)
            elif (((timezone.now() - obj.time).seconds)//60) >=1:
                obj.activity_time = '{} min ago'.format(((timezone.now() - obj.time).seconds) //60)
            else:
                obj.activity_time = '{} sec ago'.format(((timezone.now() - obj.time).seconds))
        activity_list =[{
            'description': act.description,
            'time': act.activity_time,
            'type': act.type,
            'releted_job': JobSerializer(act.releted_job).data,
            'updated_section': act.updated_section
        } for act in activity]

        return Response(activity_list)


class EducationObject(APIView):
    def get(self, request, pk):
        education = ProfessionalEducationSerializer(get_object_or_404(ProfessionalEducation, pk=pk)).data
        edu_data = {
            'edu_info': education,
        }
        return Response(edu_data)


class SendRecommendedJobNotification(APIView):
    required_privilege = 'job.change_jobrecommendation'
    permission_classes = [StaffPermission]

    def get(self, request):
        job_recommendation_list = JobRecommendation.objects.filter(is_notified=False).values('professional').annotate(job_count = Count('professional'))
        for job_recommendation in job_recommendation_list:
            SocketClient.send({
                "type": "job_notification",
                "text": "You have " + str(job_recommendation['job_count']) + " job recommendation",
                "from": "",
                "to": str(Professional.objects.get(id=job_recommendation['professional']).user.id)
            })
        job_recommendation_list.update(is_notified = True)
        return Response(job_recommendation_list)


