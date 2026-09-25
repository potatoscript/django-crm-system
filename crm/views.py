from django.shortcuts import redirect,render
from .models import Customer
from .forms import CustomerForm


def dashboard(request):
    customer_count = Customer.objects.count()
    recent_customers = Customer.objects.order_by("-created_at")[:5]

    context = {
        "customer_count": customer_count,
        "recent_customers": recent_customers,
    }

    return render(request, "crm/dashboard.html", context)

def customer_list(request):
    customers = Customer.objects.order_by("name")

    context = {
        "customers": customers,
    }

    return render(request, "crm/customer_list.html", context)

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