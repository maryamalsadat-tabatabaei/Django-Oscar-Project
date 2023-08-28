from django.conf import settings
from oscar.core.loading import get_model
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from oscar.apps.checkout.views import PaymentDetailsView as CorePaymentDetailsView
from .facade import Facade

from . import PAYMENT_METHOD_STRIPE, PAYMENT_EVENT_PURCHASE, STRIPE_EMAIL, STRIPE_TOKEN

from .forms import StripeTokenForm

SourceType = get_model('payment', 'SourceType')
Source = get_model('payment', 'Source')


class PaymentDetailsView(CorePaymentDetailsView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(PaymentDetailsView, self).dispatch(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        ctx = super(PaymentDetailsView, self).get_context_data(**kwargs)
        if self.preview:
            ctx['stripe_token_form'] = StripeTokenForm(self.request.POST)
            ctx['order_total_incl_tax_cents'] = (
                ctx['order_total'].incl_tax * 100
            ).to_integral_value()
        else:
            ctx['order_total_incl_tax_cents'] = (
                ctx['order_total'].incl_tax * 100
            ).to_integral_value()
            ctx['stripe_publishable_key'] = settings.STRIPE_PUBLISHABLE_KEY
        return ctx

    def handle_payment(self, order_number, total, **kwargs):
        stripe_ref = Facade().charge(
            order_number,
            total,
            card=self.request.POST[STRIPE_TOKEN],
            description=self.payment_description(order_number, total, **kwargs),
            metadata=self.payment_metadata(order_number, total, **kwargs))

        source_type, __ = SourceType.objects.get_or_create(name=PAYMENT_METHOD_STRIPE)
        source = Source(
            source_type=source_type,
            currency=settings.STRIPE_CURRENCY,
            amount_allocated=total.incl_tax,
            amount_debited=total.incl_tax,
            reference=stripe_ref)
        self.add_payment_source(source)

        self.add_payment_event(PAYMENT_EVENT_PURCHASE, total.incl_tax)

    def payment_description(self, order_number, total, **kwargs):
        return self.request.POST[STRIPE_EMAIL]

    def payment_metadata(self, order_number, total, **kwargs):
        return {'order_number': order_number}