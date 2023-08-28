from django.conf import settings
from oscar.apps.payment.exceptions import UnableToTakePayment, InvalidGatewayRequestError

import stripe


class Facade(object):
    def __init__(self):
        stripe.api_key = settings.STRIPE_SECRET_KEY

    @staticmethod
    def get_friendly_decline_message(error):
        return 'The transaction was declined by your bank - please check your bankcard details and try again'

    @staticmethod
    def get_friendly_error_message(error):
        return 'An error occurred when communicating with the payment gateway.'

    def charge(self,
        order_number,
        total,
        card,
        currency=settings.STRIPE_CURRENCY,
        description=None,
        metadata=None,
        **kwargs):
        try:
            return stripe.Charge.create(
                amount=(total.incl_tax * 100).to_integral_value(),
                currency=currency,
                card=card,
                description=description,
                metadata=(metadata or {'order_number': order_number}),
                **kwargs).id
        # except stripe.CardError, e:
        #     raise UnableToTakePayment(self.get_friendly_decline_message(e))
        # except stripe.StripeError, e:
        #     raise InvalidGatewayRequestError(self.get_friendly_error_message(e))
        except stripe.error.CardError as e:
            raise UnableToTakePayment(self.get_friendly_decline_message(e))
        except stripe.error.StripeError as e:
            raise InvalidGatewayRequestError(self.get_friendly_error_message(e))