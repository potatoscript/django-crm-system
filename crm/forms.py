from django import forms
from .models import Contact, Customer, Opportunity


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

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact

        fields = [
            "customer",
            "first_name",
            "last_name",
            "job_title",
            "email",
            "phone",
            "mobile",
            "notes",
        ]

        widgets = {
            "notes": forms.Textarea(
                attrs={
                    "rows": 4,
                }
            ),
        }

class OpportunityForm(forms.ModelForm):

    class Meta:
        model = Opportunity

        fields = [
            "customer",
            "name",
            "stage",
            "amount",
            "probability",
            "expected_close_date",
            "description",
        ]

        widgets = {
            "expected_close_date": forms.DateInput(
                attrs={
                    "type": "date",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "rows": 4,
                }
            ),
        }