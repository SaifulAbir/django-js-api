from django.db.models import Prefetch
from rest_framework.generics import ListAPIView

from p7.pagination import P7Pagination
from p7.permissions import StaffPermission
from pro.models import Professional, ProfessionalSkill, ProfessionalLocationPreference
from pro.serializers import ProfessionalSerializerAdmin


class MlProfessionalList(ListAPIView):
    # required_privilege = 'pro.view_professional'
    permission_classes = []
    serializer_class = ProfessionalSerializerAdmin

    def get_queryset(self):
        queryset = Professional.objects.all(
        ).prefetch_related(
            Prefetch('skills',
                     queryset=ProfessionalSkill.objects.filter(is_archived=False).order_by('skill_name')),
            Prefetch('pro_location_preferences',
                     queryset=ProfessionalLocationPreference.objects.filter(is_archived=False)),
        )
        return queryset