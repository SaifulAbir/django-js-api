import logging

import requests
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.response import Response
from account.models import TransactionHistory
from account.utils import subscription_info_save
from django.conf import settings as current_settings



class IpnAPI(APIView):
    permission_classes = []
    def post(self, request, *args, **kwargs):
        data = request.data
        if data['status'] == 'VALID':
            val_id = data['val_id']
            store_id = data['store_id']
            verify_sign = data['verify_sign']
            verify_sign_sha2 = data['verify_sign_sha2']
            currency_rate = data['currency_rate']
            error = data['error']
            base_fair = data['base_fair']
            card_sub_brand = data['card_sub_brand']
            payload = {'val_id': val_id,'store_id': store_id,
                       'store_passwd': current_settings.PAYMENT_GATEWAY_STORE_PASSWORD}
            resp = requests.get('https://sandbox.sslcommerz.com/validator/api/validationserverAPI.php',
                                params= payload)
            logging.warning(resp)

            if resp['status'] == 'VALID':
                amount = resp['amount']
                bank_tran_id = resp['bank_tran_id']
                card_brand = resp['card_brand']
                card_issuer = resp['card_issuer']
                card_issuer_country = resp['card_issuer_country']
                card_issuer_country_code = resp['card_issuer_country_code']
                card_no = resp['card_no']
                card_type = resp['card_type']
                currency = resp['currency']
                currency_amount = resp['currency_amount']
                currency_type = resp['currency_type']
                risk_level = resp['risk_level']
                risk_title = resp['risk_title']
                status = resp['status']
                store_amount = resp['store_amount']
                tran_date = resp['tran_date']
                tran_id = resp['tran_id']
                emi_installment = resp['emi_installment']
                emi_amount = resp['emi_amount']
                discount_amount = resp['discount_amount']
                discount_percentage = resp['discount_percentage']
                discount_remarks = resp['discount_remarks']
                value_a = resp['value_a']
                value_b = resp['value_b']
                value_c = resp['value_c']
                value_d = resp['value_d']
                tran_histories = TransactionHistory()
                if bank_tran_id:
                    tran_histories.bank_tran_id = bank_tran_id
                else:
                    return Response(status=HTTP_400_BAD_REQUEST)
                if card_brand:
                    tran_histories.card_brand = card_brand
                else:
                    return Response(status=HTTP_400_BAD_REQUEST)
                if card_issuer:
                    tran_histories.card_issuer = card_issuer
                else:
                    return Response(status=HTTP_400_BAD_REQUEST)
                if card_issuer_country:
                    tran_histories.card_issuer_country = card_issuer_country
                else:
                    return Response(status=HTTP_400_BAD_REQUEST)
                if card_issuer_country_code:
                    tran_histories.card_issuer_country_code = card_issuer_country_code
                else:
                    return Response(status=HTTP_400_BAD_REQUEST)
                if currency:
                    tran_histories.currency = currency
                else:
                    return Response(status=HTTP_400_BAD_REQUEST)
                if currency_rate:
                    tran_histories.currency_rate = currency_rate
                else:
                    return Response(status=HTTP_400_BAD_REQUEST)
                if currency_type:
                    tran_histories.currency_type = currency_type
                else:
                    return Response(status=HTTP_400_BAD_REQUEST)
                if status:
                    tran_histories.status = status
                else:
                    return Response(status=HTTP_400_BAD_REQUEST)
                if store_id:
                    tran_histories.store_id = store_id
                else:
                    return Response(status=HTTP_400_BAD_REQUEST)
                if tran_id:
                    tran_histories.tran_id = tran_id
                else:
                    return Response(status=HTTP_400_BAD_REQUEST)
                if val_id:
                    tran_histories.val_id = val_id
                else:
                    return Response(status=HTTP_400_BAD_REQUEST)
                if verify_sign:
                    tran_histories.verify_sign = verify_sign
                else:
                    return Response(status=HTTP_400_BAD_REQUEST)
                if verify_sign_sha2:
                    tran_histories.verify_sign_sha2 = verify_sign_sha2
                else:
                    return Response(status=HTTP_400_BAD_REQUEST)

                tran_histories.amount = amount
                tran_histories.base_fair = base_fair
                tran_histories.card_no = card_no
                tran_histories.card_sub_brand = card_sub_brand
                tran_histories.card_type = card_type
                tran_histories.currency_amount = currency_amount
                tran_histories.error = error
                tran_histories.risk_title = risk_title
                tran_histories.risk_level = risk_level
                tran_histories.store_amount = store_amount
                tran_histories.tran_date = tran_date
                tran_histories.value_a = value_a
                tran_histories.value_b = value_b
                tran_histories.value_c = value_c
                tran_histories.value_d = value_d
                tran_histories.emi_instalment = emi_installment
                tran_histories.emi_amount = emi_amount
                tran_histories.discount_amount = discount_amount
                tran_histories.discount_remarks = discount_remarks
                tran_histories.discount_percentage = discount_percentage
                tran_histories.save()
                subscription_info_save(tran_histories)
                return Response(resp)
            else:
                return Response(status=HTTP_400_BAD_REQUEST)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)