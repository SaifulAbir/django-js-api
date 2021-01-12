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
        logging.warning('calling ipn response')
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
            resp = requests.get(current_settings.PAYMENT_VALIDATE_URL, params= payload)
            logging.warning(resp)
            resp_data = resp.json()
            logging.warning('starting')
            logging.warning(resp_data)
            logging.warning(resp_data['status'])
            if resp_data['status'] == 'VALID':
                amount = resp_data['amount']
                bank_tran_id = resp_data['bank_tran_id']
                card_brand = resp_data['card_brand']
                card_issuer = resp_data['card_issuer']
                card_issuer_country = resp_data['card_issuer_country']
                card_issuer_country_code = resp_data['card_issuer_country_code']
                card_no = resp_data['card_no']
                card_type = resp_data['card_type']
                currency = resp_data['currency']
                currency_amount = resp_data['currency_amount']
                currency_type = resp_data['currency_type']
                risk_level = resp_data['risk_level']
                risk_title = resp_data['risk_title']
                status = resp_data['status']
                store_amount = resp_data['store_amount']
                tran_date = resp_data['tran_date']
                tran_id = resp_data['tran_id']
                emi_instalment = resp_data['emi_instalment']
                emi_amount = resp_data['emi_amount']
                discount_amount = resp_data['discount_amount']
                discount_percentage = resp_data['discount_percentage']
                discount_remarks = resp_data['discount_remarks']
                value_a = resp_data['value_a']
                value_b = resp_data['value_b']
                value_c = resp_data['value_c']
                value_d = resp_data['value_d']
                tran_histories = TransactionHistory()
                if bank_tran_id:
                    tran_histories.bank_tran_id = bank_tran_id
                else:
                    logging.warning('Status Not Validated14')
                    return Response({'details': 'Status Not Valid.1'},
                                    status=HTTP_400_BAD_REQUEST)
                if card_brand:
                    tran_histories.card_brand = card_brand
                else:
                    logging.warning('Status Not Validated13')
                    return Response({'details': 'Status Not Valid.2'},
                                    status=HTTP_400_BAD_REQUEST)
                if card_issuer:
                    tran_histories.card_issuer = card_issuer
                else:
                    logging.warning('Status Not Validated12')
                    return Response({'details': 'Status Not Valid.3'},
                                    status=HTTP_400_BAD_REQUEST)
                if card_issuer_country:
                    tran_histories.card_issuer_country = card_issuer_country
                else:
                    logging.warning('Status Not Validated11')
                    return Response({'details': 'Status Not Valid.4'},
                                    status=HTTP_400_BAD_REQUEST)
                if card_issuer_country_code:
                    tran_histories.card_issuer_country_code = card_issuer_country_code
                else:
                    logging.warning('Status Not Validated10')
                    return Response({'details': 'Status Not Valid.5'},
                                    status=HTTP_400_BAD_REQUEST)
                if currency:
                    tran_histories.currency = currency
                else:
                    logging.warning('Status Not Validated9')
                    return Response({'details': 'Status Not Valid.6'},
                                    status=HTTP_400_BAD_REQUEST)
                if currency_rate:
                    tran_histories.currency_rate = currency_rate
                else:
                    logging.warning('Status Not Validated8')
                    return Response({'details': 'Status Not Valid.7'},
                                    status=HTTP_400_BAD_REQUEST)
                if currency_type:
                    tran_histories.currency_type = currency_type
                else:
                    logging.warning('Status Not Validated7')
                    return Response({'details': 'Status Not Valid.8'},
                                    status=HTTP_400_BAD_REQUEST)
                if status:
                    tran_histories.status = status
                else:
                    logging.warning('Status Not Validated6')
                    return Response({'details': 'Status Not Valid.9'},
                                    status=HTTP_400_BAD_REQUEST)
                if store_id:
                    tran_histories.store_id = store_id
                else:
                    logging.warning('Status Not Validated5')
                    return Response({'details': 'Status Not Valid.10'},
                                    status=HTTP_400_BAD_REQUEST)
                if tran_id:
                    tran_histories.tran_id = tran_id
                else:
                    logging.warning('Status Not Validated4')
                    return Response({'details': 'Status Not Valid.11'},
                                    status=HTTP_400_BAD_REQUEST)
                if val_id:
                    tran_histories.val_id = val_id
                else:
                    logging.warning('Status Not Validated3')
                    return Response({'details': 'Status Not Valid.12'},
                                    status=HTTP_400_BAD_REQUEST)
                if verify_sign:
                    tran_histories.verify_sign = verify_sign
                else:
                    logging.warning('Status Not Validated2')
                    return Response({'details': 'Status Not Valid.13'},
                                    status=HTTP_400_BAD_REQUEST)
                if verify_sign_sha2:
                    tran_histories.verify_sign_sha2 = verify_sign_sha2
                else:
                    logging.warning('Status Not Validated1')
                    return Response({'details': 'Status Not Valid.14'},
                                    status=HTTP_400_BAD_REQUEST)

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
                tran_histories.emi_instalment = emi_instalment
                tran_histories.emi_amount = emi_amount
                tran_histories.discount_amount = discount_amount
                tran_histories.discount_remarks = discount_remarks
                tran_histories.discount_percentage = discount_percentage
                tran_histories.save()
                subscription_info_save(tran_histories)
                return Response(resp_data)
            else:
                logging.warning('Status Not Validated')
                return Response({'details': 'Status Not Validated.'},
                                status=HTTP_400_BAD_REQUEST)
        else:
            logging.warning('Status Not Valid')
            return Response({'details': 'Status Not Valid.'},
                            status=HTTP_400_BAD_REQUEST)