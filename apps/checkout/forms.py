from django import forms


class StripeTokenForm(forms.Form):
    stripeEmail = forms.EmailField(widget=forms.HiddenInput())
    stripeToken = forms.CharField(widget=forms.HiddenInput())