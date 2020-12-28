from rest_framework import generics

from p7.models import populate_user_info_request
from p7.permissions import ProfessionalPermission
from pro.models import Professional
from pro.serializers import CartCreateSerializer
from pro.utils import invoice_id_generator


class CartCreate(generics.CreateAPIView):
    permission_classes = [ProfessionalPermission]
    serializer_class = CartCreateSerializer

    def post(self, request, *args, **kwargs):
        professional = Professional.objects.get(user=request.user)
        populate_user_info_request(request, False, False)
        invoice_id = invoice_id_generator(professional.id)
        request.data.update({'invoice_id': invoice_id, 'professional': professional.id})
        return super(CartCreate, self).post(request, *args, **kwargs)