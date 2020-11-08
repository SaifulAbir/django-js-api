import uuid

import requests
from django.core import serializers
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from p7.models import populate_user_info_request
from p7.permissions import ProfessionalPermission
from p7.utils import send_sms
from settings.models import Settings
from .models import CertificateName, Major, Organization, Institute, Nationality, Religion, Professional, \
    EducationLevel, CertifyingOrganization, MembershipOrganization
from .serializers import EmailSubscriptionUpdateSerializer, CertificateNameSerializer, MajorSerializer, \
    OrganizationNameSerializer, InstituteNameSerializer, NationalitySerializer, ReligionSerializer, \
    EducationLevelSerializer, MembershipOrganizationNameSerializer, CertifyingOrganizationNameSerializer, \
    SendAppLinkSerializer


class ReligionList(generics.ListAPIView):
    permission_classes = [ProfessionalPermission]
    queryset = Religion.objects.all()
    serializer_class = ReligionSerializer


class NationalityList(generics.ListAPIView):
    permission_classes = [ProfessionalPermission]
    queryset = Nationality.objects.all()
    serializer_class = NationalitySerializer


class InstituteList(generics.ListAPIView):
    permission_classes = [ProfessionalPermission]
    queryset = Institute.objects.all()
    serializer_class = InstituteNameSerializer


class OrganizationList(generics.ListAPIView):
    permission_classes = [ProfessionalPermission]
    queryset = Organization.objects.all()
    serializer_class = OrganizationNameSerializer


class MembershipOrganizationList(generics.ListAPIView):
    permission_classes = [ProfessionalPermission]
    queryset = MembershipOrganization.objects.all()
    serializer_class = MembershipOrganizationNameSerializer


class CertifyingOrganizationList(generics.ListAPIView):
    permission_classes = [ProfessionalPermission]
    queryset = CertifyingOrganization.objects.all()
    serializer_class = CertifyingOrganizationNameSerializer


class MajorList(generics.ListAPIView):
    permission_classes = [ProfessionalPermission]
    queryset = Major.objects.all()
    serializer_class = MajorSerializer

    def get_queryset(self):
        name = self.request.GET.get('name')
        if name:
            return Major.objects.filter(name__icontains=name).order_by('name')
        else:
            return Major.objects.all().order_by('name')

class EducationLevelList(generics.ListAPIView):
    permission_classes = [ProfessionalPermission]
    queryset = EducationLevel.objects.all()
    serializer_class = EducationLevelSerializer


class CertificateNameList(generics.ListAPIView):
    permission_classes = [ProfessionalPermission]
    queryset = CertificateName.objects.all()
    serializer_class = CertificateNameSerializer


class InstituteSearch(generics.ListAPIView):
    permission_classes = [ProfessionalPermission]
    queryset = CertificateName.objects.all()
    serializer_class = CertificateNameSerializer
    def get_queryset(self):
        name = self.request.GET.get('name')
        if name:
            return Institute.objects.filter(name__icontains=name).order_by('name')

class MembershipOrganizationSearch(generics.ListAPIView):
    permission_classes = [ProfessionalPermission]
    queryset = MembershipOrganization.objects.all()
    serializer_class = MembershipOrganizationNameSerializer
    def get_queryset(self):
        name = self.request.GET.get('name')
        if name:
            return MembershipOrganization.objects.filter(name__icontains=name).order_by('name')

class CertifyingOrganizationSearch(generics.ListAPIView):
    permission_classes = [ProfessionalPermission]
    queryset = CertifyingOrganization.objects.all()
    serializer_class = CertifyingOrganizationNameSerializer
    def get_queryset(self):
        name = self.request.GET.get('name')
        if name:
            return CertifyingOrganization.objects.filter(name__icontains=name).order_by('name')


class EmailSubscriptionUpdateView(generics.UpdateAPIView):
    permission_classes = [ProfessionalPermission]
    serializer_class = EmailSubscriptionUpdateSerializer

    def get_object(self):
        user = self.request.user
        queryset = Professional.objects.filter(
            user_id = user.id
        )
        return get_object_or_404(queryset)

    def put(self, request, *args, **kwargs):
        populate_user_info_request(request, True, False)
        return super(EmailSubscriptionUpdateView, self).put(request, *args, **kwargs)


class SendAppLinkAPI(APIView):
    permission_classes = []

    def post(self, request):
        serializer = SendAppLinkSerializer(data=request.data)
        settingsObj = Settings.objects.all().first()
        sms_text = settingsObj.sms_text
        if serializer.is_valid():
            resp = send_sms(request.data.get("mobile"), sms_text)
            if resp.status_code == 200:
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

