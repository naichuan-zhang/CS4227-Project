from django import forms


class PaymentForm(forms.Form):

    email = forms.CharField()
    password = forms.CharField()


class CardForm(forms.Form):

    name = forms.CharField()
    number = forms.IntegerField()
