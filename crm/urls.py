from django.urls import path
from . import views


urlpatterns = [
    path(
        "",
        views.dashboard,
        name="dashboard"
    ),

    path(
        "customers/",
        views.customer_list,
        name="customer_list"
    ),

    path(
        "customers/add/",
        views.customer_create,
        name="customer_create"
    ),

    path(
        "customers/<int:pk>/",
        views.customer_detail,
        name="customer_detail"
    ),

    path(
        "customers/<int:pk>/edit/",
        views.customer_update,
        name="customer_update"
    ),

    path(
        "customers/<int:pk>/delete/",
        views.customer_delete,
        name="customer_delete"
    ),

    path(
        "contacts/",
        views.contact_list,
        name="contact_list"
    ),

    path(
        "contacts/add/",
        views.contact_create,
        name="contact_create"
    ),

    path(
        "contacts/<int:pk>/",
        views.contact_detail,
        name="contact_detail"
    ),

    path(
        "contacts/<int:pk>/edit/",
        views.contact_update,
        name="contact_update"
    ),

    path(
        "contacts/<int:pk>/delete/",
        views.contact_delete,
        name="contact_delete"
    ),

    path(
        "opportunities/",
        views.opportunity_list,
        name="opportunity_list"
    ),

    path(
        "opportunities/add/",
        views.opportunity_create,
        name="opportunity_create"
    ),

    path(
        "opportunities/<int:pk>/",
        views.opportunity_detail,
        name="opportunity_detail"
    ),

    path(
        "opportunities/<int:pk>/edit/",
        views.opportunity_update,
        name="opportunity_update"
    ),

    path(
        "opportunities/<int:pk>/delete/",
        views.opportunity_delete,
        name="opportunity_delete"
    ),
]