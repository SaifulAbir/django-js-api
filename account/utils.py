from dateutil.relativedelta import relativedelta
from pro.models import SubscriptionInfo, Cart, Professional
from datetime import datetime, timedelta


def subscription_info_save(tran_histories):
    cart = Cart.objects.get(invoice_id = tran_histories.tran_id)
    professional = Professional.objects.get(id=cart.professional.id)
    subscription_info = SubscriptionInfo(professional=cart.professional, subscription_duration=cart.subscription_duration,
                                         subscription_duration_type=cart.subscription_duration_type, is_payment_successful=True,
                                         payment_reference=tran_histories)

    subscription_info.start_date = datetime.now()
    professional.last_subscription_start_date = datetime.now()

    if cart.professional.last_subscription_expire_date:
        if cart.professional.last_subscription_expire_date >= datetime.now():
            if cart.subscription_duration_type == 'MONTHLY':
                subscription_info.end_date = professional.last_subscription_expire_date = cart.professional.last_subscription_expire_date + relativedelta(months=cart.subscription_duration)
            if cart.subscription_duration_type == 'YEARLY':
                subscription_info.end_date = professional.last_subscription_expire_date = cart.professional.last_subscription_expire_date + relativedelta(years=cart.subscription_duration)
        else:
            if cart.subscription_duration_type == 'MONTHLY':
                subscription_info.end_date = professional.last_subscription_expire_date = datetime.now() + relativedelta(months=cart.subscription_duration)
            if cart.subscription_duration_type == 'YEARLY':
                subscription_info.end_date = professional.last_subscription_expire_date = datetime.now() + relativedelta(years=cart.subscription_duration)
    else:
        if cart.subscription_duration_type == 'MONTHLY':
            subscription_info.end_date = professional.last_subscription_expire_date = datetime.now() + relativedelta(months=cart.subscription_duration)
        if cart.subscription_duration_type == 'YEARLY':
            subscription_info.end_date = professional.last_subscription_expire_date = datetime.now() + relativedelta(years=cart.subscription_duration)

    subscription_info.save()
    professional.save()


