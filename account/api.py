from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.response import Response
from account.models import TransactionHistory
from account.utils import subscription_info_save


class IpnAPI(APIView):
    permission_classes = []
    def post(self, request, *args, **kwargs):
        data = request.data
        if data['status'] == 'VALID':
            amount = data['amount']
            bank_tran_id = data['bank_tran_id']
            base_fair = data['base_fair']
            card_brand = data['card_brand']
            card_issuer = data['card_issuer']
            card_issuer_country = data['card_issuer_country']
            card_issuer_country_code = data['card_issuer_country_code']
            card_sub_brand = data['card_sub_brand']
            card_no = data['card_no']
            card_type = data['card_type']
            currency = data['currency']
            currency_amount = data['currency_amount']
            currency_type = data['currency_type']
            currency_rate = data['currency_rate']
            error = data['error']
            risk_level = data['risk_level']
            risk_title = data['risk_title']
            status = data['status']
            store_amount = data['store_amount']
            store_id = data['store_id']
            tran_date = data['tran_date']
            tran_id = data['tran_id']
            val_id = data['val_id']
            value_a = data['value_a']
            value_b = data['value_b']
            value_c = data['value_c']
            value_d = data['value_d']
            verify_sign = data['verify_sign']
            verify_sign_sha2 = data['verify_sign_sha2']
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
            tran_histories.save()
            subscription_info_save(tran_histories)
            return Response(request.data)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)