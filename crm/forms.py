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

    def clean_probability(self):
        probability = self.cleaned_data["probability"]

        if not 0 <= probability <= 100:
            raise forms.ValidationError(
                "Probability must be between 0 and 100."
            )

        return probability

    def clean_amount(self):
        amount = self.cleaned_data["amount"]

        if amount < 0:
            raise forms.ValidationError(
                "Amount cannot be negative."
            )

        return amount