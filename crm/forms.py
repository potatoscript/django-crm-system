from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer

        fields = [
            "name",
            "industry",
            "website",
            "phone",
            "email",
            "address",
            "country",
        ]