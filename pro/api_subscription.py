from rest_framework import generics, status
from rest_framework.views import APIView
from sslcommerz_lib import SSLCOMMERZ
from django.conf import settings as current_settings
from p7.models import populate_user_info_request
from p7.permissions import ProfessionalPermission
from pro.models import Professional, Cart
from pro.serializers import CartCreateSerializer, TransactionCreateSerializer
from pro.utils import invoice_id_generator
from rest_framework.response import Response

from settings.models import Settings


class CartCreate(generics.CreateAPIView):
    permission_classes = [ProfessionalPermission]
    serializer_class = CartCreateSerializer

    def post(self, request, *args, **kwargs):
        professional = Professional.objects.get(user=request.user)
        populate_user_info_request(request, False, False)
        invoice_id = invoice_id_generator(professional.id)
        request.data.update({'invoice_id': invoice_id, 'professional': professional.id})
        return super(CartCreate, self).post(request, *args, **kwargs)




class PaymentSession(APIView):
    permission_classes = []
    def post(self, request, *args, **kwargs):
        cart_info = Cart.objects.get(invoice_id = request.data['transaction_id'])
        if not cart_info:
            return Response({'details': 'Invalid Transaction'},
                            status=status.HTTP_400_BAD_REQUEST)
        subscription_fee = 0
        if cart_info.subscription_duration_type == "MONTHLY":
            subscription_fee = Settings.objects.values('standard_member_payable_amount_per_month')[0][
                'standard_member_payable_amount_per_month']

        if cart_info.subscription_duration_type == "YEARLY":
            subscription_fee = Settings.objects.values('standard_member_payable_amount_per_year')[0][
                'standard_member_payable_amount_per_year']
        total_amount = cart_info.subscription_duration * subscription_fee

        settings = {'store_id': current_settings.PAYMENT_GATEWAY_STORE_ID, 'store_pass': current_settings.PAYMENT_GATEWAY_STORE_PASSWORD, 'issandbox': current_settings.IS_SANDBOX}
        sslcommez = SSLCOMMERZ(settings)
        post_body = {}
        post_body['total_amount'] = total_amount
        post_body['currency'] = "BDT"
        post_body['tran_id'] = cart_info.invoice_id
        post_body['success_url'] = "https://jobxprss.com/success"
        post_body['fail_url'] = "https://jobxprss.com/failed"
        post_body['cancel_url'] = "https://jobxprss.com/cancel"
        post_body['emi_option'] = 0
        post_body['cus_name'] = cart_info.professional.full_name
        post_body['cus_email'] = cart_info.professional.email
        post_body['cus_phone'] = cart_info.professional.phone
        post_body['cus_add1'] = cart_info.professional.address
        post_body['cus_city'] = cart_info.professional.current_location
        post_body['cus_country'] = "Bangladesh"
        post_body['shipping_method'] = "NO"
        post_body['multi_card_name'] = ""
        post_body['num_of_item'] = 1
        post_body['product_name'] = "Test"
        post_body['product_category'] = "Test Category"
        post_body['product_profile'] = "general"
        response = sslcommez.createSession(post_body)
        return Response(response['GatewayPageURL'])


class TransactionCreate(generics.CreateAPIView):
    permission_classes = []
    serializer_class = TransactionCreateSerializer

    def post(self, request, *args, **kwargs):
        print(request.data)
        return super(TransactionCreate, self).post(request, *args, **kwargs)