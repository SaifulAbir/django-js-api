from django.db.models import Prefetch
from rest_framework.generics import ListAPIView

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