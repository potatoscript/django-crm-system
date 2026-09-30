from django.contrib import admin
from .models import Contact, Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "industry",
        "country",
        "email",
        "phone",
        "created_at",
    )

    search_fields = (
        "name",
        "industry",
        "email",
        "country",
    )

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "customer",
        "job_title",
        "email",
        "phone",
    )

    search_fields = (
        "first_name",
        "last_name",
        "customer__name",
        "job_title",
        "email",
    )