from rest_framework import generics

from p7.models import populate_user_info_request
from p7.permissions import ProfessionalPermission
from pro.serializers import SubscriptionInfoSerializer


class SubscriptionInfoCreate(generics.CreateAPIView):
    permission_classes = [ProfessionalPermission]
    serializer_class = SubscriptionInfoSerializer

    def post(self, request, *args, **kwargs):
        populate_user_info_request(request, False, False)
        return super(SubscriptionInfoCreate, self).post(request, *args, **kwargs)