from django.db.models import Prefetch
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework.response import Response
from job.models import JobRecommendation
from job.serializers import JobRecommendationSerializerAdmin
from p7.models import populate_user_info, populate_user_info_request, populate_user_info_querydict
from p7.pagination import P7Pagination
from p7.permissions import StaffPermission
from pro.models import Professional, ProfessionalSkill, ProfessionalLocationPreference
from pro.serializers import ProfessionalSerializerAdmin


class MlProfessionalList(ListAPIView):
    required_privilege = 'pro.view_professional'
    permission_classes = [StaffPermission]
    serializer_class = ProfessionalSerializerAdmin

    def get_queryset(self):
        request = self.request
        job_search_preference = request.GET.get('job_search_preference')
        queryset = Professional.objects.all(
        ).prefetch_related(
            Prefetch('skills',
                     queryset=ProfessionalSkill.objects.filter(is_top_skill=True, is_archived=False).order_by('skill_name')),
            Prefetch('pro_location_preferences',
                     queryset=ProfessionalLocationPreference.objects.filter(is_archived=False)),
        )
        if job_search_preference:
            queryset = queryset.filter(job_search_preference=job_search_preference)
        return queryset


class JobRecommendationBulkCreateView(APIView):
    required_privilege = 'job.add_jobrecommendation'
    permission_classes = [StaffPermission]
    serializer_class = JobRecommendationSerializerAdmin

    def post(self, request, *args, **kwargs):
        serializer = JobRecommendationSerializerAdmin(data=request.data, many=isinstance(request.data, list))
        if serializer.is_valid():
            for job_recomandation in serializer.data:
                populate_user_info_querydict(request, job_recomandation, False, False)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)