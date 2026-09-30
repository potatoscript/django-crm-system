from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect,render
from .models import Contact, Customer
from .forms import ContactForm, CustomerForm


def dashboard(request):
    customer_count = Customer.objects.count()
    recent_customers = Customer.objects.order_by("-created_at")[:5]

    context = {
        "customer_count": customer_count,
        "recent_customers": recent_customers,
    }

    return render(request, "crm/dashboard.html", context)

def customer_list(request):
    query = request.GET.get("q", "")

    customers = Customer.objects.all()

    if query:
        customers = customers.filter(
            Q(name__icontains=query)
            | Q(industry__icontains=query)
            | Q(email__icontains=query)
            | Q(phone__icontains=query)
            | Q(country__icontains=query)
        )

    customers = customers.order_by("name")

    paginator = Paginator(customers, 5)

    page_number = request.GET.get("page")

    page_obj = paginator.get_page(page_number)

    context = {
        "customers": page_obj,
        "page_obj": page_obj,
        "query": query,
    }

    return render(
        request,
        "crm/customer_list.html",
        context
    )

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)

    context = {
        "customer": customer,
    }

    return render(
        request,
        "crm/customer_detail.html",
        context
    )


def customer_create(request):

    if request.method == "POST":
        form = CustomerForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("customer_list")

    else:
        form = CustomerForm()

    context = {
        "form": form,
    }

    return render(
        request,
        "crm/customer_form.html",
        context
    )


def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)

    if request.method == "POST":
        form = CustomerForm(
            request.POST,
            instance=customer
        )

        if form.is_valid():
            form.save()

            return redirect(
                "customer_detail",
                pk=customer.pk
            )

    else:
        form = CustomerForm(instance=customer)

    context = {
        "form": form,
        "customer": customer,
    }

    return render(
        request,
        "crm/customer_form.html",
        context
    )

def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)

    if request.method == "POST":
        customer.delete()

        return redirect("customer_list")

    context = {
        "customer": customer,
    }

    return render(
        request,
        "crm/customer_confirm_delete.html",
        context
    )

def contact_list(request):
    contacts = Contact.objects.select_related(
        "customer"
    ).order_by(
        "last_name",
        "first_name"
    )

    context = {
        "contacts": contacts,
    }

    return render(
        request,
        "crm/contact_list.html",
        context
    )

def contact_create(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            contact = form.save()

            return redirect(
                "contact_detail",
                pk=contact.pk
            )

    else:
        form = ContactForm()

    context = {
        "form": form,
    }

    return render(
        request,
        "crm/contact_form.html",
        context
    )

def contact_detail(request, pk):
    contact = get_object_or_404(
        Contact.objects.select_related("customer"),
        pk=pk
    )

    context = {
        "contact": contact,
    }

    return render(
        request,
        "crm/contact_detail.html",
        context
    )

def contact_update(request, pk):
    contact = get_object_or_404(Contact, pk=pk)

    if request.method == "POST":
        form = ContactForm(
            request.POST,
            instance=contact
        )

        if form.is_valid():
            form.save()

            return redirect(
                "contact_detail",
                pk=contact.pk
            )

    else:
        form = ContactForm(instance=contact)

    context = {
        "form": form,
        "contact": contact,
    }

    return render(
        request,
        "crm/contact_form.html",
        context
    )

def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)

    if request.method == "POST":
        contact.delete()

        return redirect("contact_list")

    context = {
        "contact": contact,
    }

    return render(
        request,
        "crm/contact_confirm_delete.html",
        context
    )