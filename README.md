# Django CRM System

A Customer Relationship Management (CRM) system built with **Python and Django**.

The goal of this project is to build a practical CRM application step by step while learning Django application development, database design, Git, and GitHub.

The system will eventually provide:

- CRM Dashboard
- Customer Management
- Contact Management
- Opportunity / Sales Pipeline Management
- Activity and Follow-up Management
- Search
- Reports and Analytics
- User Authentication and Permissions
- PostgreSQL support
- REST API
- AI-assisted CRM features

---

# 1. Development Environment

The project is currently developed with:

| Component | Version / Tool |
|---|---|
| Operating System | Windows |
| Python | 3.11.1 |
| Django | 5.2 LTS |
| Database | SQLite |
| IDE | Visual Studio Code |
| Terminal | PowerShell |
| Version Control | Git |
| Repository Hosting | GitHub |

Project directory:

```text
D:\MyProjects\crm-system
```

---

# 2. Create the Project Directory

The project is stored in:

```text
D:\MyProjects\crm-system
```

Open the folder using Visual Studio Code and open a PowerShell terminal.

Check the installed Python version:

```powershell
python --version
```

Output:

```text
Python 3.11.1
```

## Why check the Python version?

Different Django versions support different Python versions.

Because this project currently uses Python 3.11, Django 5.2 LTS is used rather than Django 6.

---

# 3. Create a Python Virtual Environment

A Python virtual environment keeps the packages required by this project separate from the global Python installation.

This prevents dependencies from different Python projects from interfering with each other.

Create the virtual environment:

```powershell
python -m venv .venv
```

The command means:

```text
python
│
├── -m
│   Run a Python module
│
├── venv
│   Python's built-in virtual environment module
│
└── .venv
    Name of the virtual environment directory
```

After creation, the project contains:

```text
crm-system/
└── .venv/
```

---

# 4. Virtual Environment Creation Problem

During the first attempt, the following command:

```powershell
python -m venv .venv
```

was interrupted while Python was running `ensurepip`.

The error ended with:

```text
KeyboardInterrupt
```

This meant that the virtual environment creation process had been interrupted before it finished.

Because `.venv` may have been only partially created, it was deleted before trying again.

Delete the incomplete environment:

```powershell
Remove-Item -Recurse -Force .venv
```

Explanation:

```text
Remove-Item
    Deletes a file or directory.

-Recurse
    Deletes everything inside the directory.

-Force
    Allows PowerShell to remove hidden or protected items as necessary.

.venv
    The directory being removed.
```

Verify that `.venv` was deleted:

```powershell
Test-Path .venv
```

Output:

```text
False
```

`False` confirms that the directory no longer exists.

---

# 5. Check pip

Before recreating the virtual environment, verify that Python's package manager is working:

```powershell
python -m pip --version
```

The result was:

```text
pip 22.3.1 from C:\Python311\Lib\site-packages\pip (python 3.11)
```

This confirmed that the global Python installation had a working `pip`.

`pip` is Python's package manager and is used to install packages such as Django.

The `ensurepip` module can also be checked with:

```powershell
python -m ensurepip --version
```

`ensurepip` is the Python module used to bootstrap/install `pip`, including when Python creates a virtual environment.

---

# 6. Recreate the Virtual Environment

The virtual environment was then created again:

```powershell
python -m venv .venv
```

After it completed successfully, activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

After activation, the PowerShell prompt changes to:

```text
(.venv) PS D:\MyProjects\crm-system>
```

The `(.venv)` prefix confirms that the virtual environment is active.

---

# 7. Verify the Virtual Environment

Check Python:

```powershell
python --version
```

Result:

```text
Python 3.11.1
```

Check pip:

```powershell
python -m pip --version
```

Result:

```text
pip 22.3.1 from D:\MyProjects\crm-system\.venv\Lib\site-packages\pip (python 3.11)
```

This is important.

Originally pip was located under:

```text
C:\Python311\Lib\site-packages
```

After activating the virtual environment it is located under:

```text
D:\MyProjects\crm-system\.venv\Lib\site-packages
```

This confirms that packages installed from this terminal will belong to this project instead of the global Python environment.

---

# 8. Upgrade pip

Upgrade pip inside the virtual environment:

```powershell
python -m pip install --upgrade pip
```

This updates the package installer used by the project.

---

# 9. Install Django

Because the project uses Python 3.11, install Django 5.2:

```powershell
python -m pip install "Django>=5.2,<5.3"
```

This means:

```text
Django >= 5.2
```

but:

```text
Django < 5.3
```

Therefore the project stays within the Django 5.2 release series.

Check the installed Django version:

```powershell
python -m django --version
```

---

# 10. Create the Django Project

Create the Django project:

```powershell
django-admin startproject crm_project .
```

The command consists of:

```text
django-admin
    Django's command-line administration utility.

startproject
    Creates a new Django project.

crm_project
    Name of the Django project/configuration package.

.
    Create the project in the current directory.
```

The final `.` is important because it prevents Django from creating an unnecessary additional outer directory.

The structure becomes:

```text
crm-system/
│
├── .venv/
│
├── manage.py
│
└── crm_project/
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

### What is `manage.py`?

`manage.py` is Django's project management command-line utility.

It is used for commands such as:

```powershell
python manage.py runserver
python manage.py migrate
python manage.py makemigrations
python manage.py startapp
python manage.py createsuperuser
```

### What is `settings.py`?

This contains the main Django project configuration, including:

- Installed applications
- Database configuration
- Middleware
- Templates
- Language and timezone settings
- Static files
- Security configuration

### What is `urls.py`?

This defines how browser URLs are routed to different parts of the Django application.

---

# 11. Create the Initial Django Database

Run:

```powershell
python manage.py migrate
```

Django includes several built-in applications such as authentication, sessions, and administration.

The `migrate` command creates the database tables required by these applications.

At this stage Django also creates:

```text
db.sqlite3
```

SQLite is being used during the initial development stage because it requires very little configuration.

---

# 12. Start the Django Development Server

Run:

```powershell
python manage.py runserver
```

Django starts its local development web server.

The terminal displays an address similar to:

```text
http://127.0.0.1:8000/
```

Opening the address in a browser displayed:

```text
The install worked successfully!
```

This confirmed that:

- Python was working
- The virtual environment was working
- Django was installed
- The Django project configuration was valid
- The development web server was running

---

# 13. Create the CRM Application

A Django project can contain multiple Django applications.

The overall project configuration is:

```text
crm_project
```

The actual CRM business application is:

```text
crm
```

Create it with:

```powershell
python manage.py startapp crm
```

This creates:

```text
crm/
├── migrations/
│   └── __init__.py
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
└── views.py
```

The difference is:

```text
crm_project
    ↓
Overall Django website configuration

crm
    ↓
CRM business functionality
```

---

# 14. Register the CRM Application

Creating an application does not automatically enable it.

Open:

```text
crm_project/settings.py
```

Add `crm` to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'crm',
]
```

This tells Django that the CRM application belongs to the project.

---

# 15. Create the Customer Model

The first CRM database entity is the Customer.

Open:

```text
crm/models.py
```

Create the following model:

```python
from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=200)
    industry = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    country = models.CharField(max_length=100, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
```

## Model Explanation

A Django model represents data stored in the database.

Conceptually:

```text
Python Model
     ↓
Django ORM
     ↓
Database Table
```

The Customer model contains:

```text
Customer
│
├── name
├── industry
├── website
├── phone
├── email
├── address
├── country
├── created_at
└── updated_at
```

### `CharField`

Example:

```python
name = models.CharField(max_length=200)
```

Used for relatively short text.

`max_length=200` means the field can contain up to 200 characters.

### `blank=True`

Example:

```python
industry = models.CharField(max_length=100, blank=True)
```

This allows the field to be left empty in Django forms.

### `URLField`

```python
website = models.URLField(blank=True)
```

Designed for website addresses.

### `EmailField`

```python
email = models.EmailField(blank=True)
```

Designed for email addresses and provides email-format validation.

### `TextField`

```python
address = models.TextField(blank=True)
```

Used for longer text without requiring a small fixed maximum length.

### `auto_now_add=True`

```python
created_at = models.DateTimeField(auto_now_add=True)
```

Automatically stores the date and time when the customer record is first created.

### `auto_now=True`

```python
updated_at = models.DateTimeField(auto_now=True)
```

Automatically updates the timestamp whenever the record is saved.

### `__str__`

```python
def __str__(self):
    return self.name
```

This controls how a Customer object is displayed by Django.

Instead of seeing something such as:

```text
Customer object (1)
```

Django can display:

```text
ABC Manufacturing
```

---

# 16. Create the Customer Database Table

After modifying a Django model, create a migration:

```powershell
python manage.py makemigrations
```

`makemigrations` examines the Django models and generates migration instructions describing the database changes.

For example:

```text
Migrations for 'crm':
  crm\migrations\0001_initial.py
    + Create model Customer
```

Then apply the migration:

```powershell
python manage.py migrate
```

The process is:

```text
models.py
    ↓
makemigrations
    ↓
Migration file
    ↓
migrate
    ↓
SQLite database
    ↓
crm_customer table
```

A very important rule when developing this project is:

```text
Change model
     ↓
python manage.py makemigrations
     ↓
python manage.py migrate
```

---

# 17. Register Customer in Django Admin

Django provides a built-in administration interface.

Open:

```text
crm/admin.py
```

Add:

```python
from django.contrib import admin
from .models import Customer


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
```

`@admin.register(Customer)` registers the Customer model with Django Admin.

`list_display` determines which fields appear in the customer list.

`search_fields` enables searching those fields from the Django Admin interface.

---

# 18. Create a Django Administrator

Create an administrator account:

```powershell
python manage.py createsuperuser
```

Django requests:

```text
Username:
Email address:
Password:
Password (again):
```

The password is intentionally not displayed while typing.

After successful creation:

```text
Superuser created successfully.
```

Start the server:

```powershell
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/admin/
```

The Django Admin interface can now manage:

```text
Authentication and Authorization
├── Groups
└── Users

CRM
└── Customers
```

The first test customer was created:

```text
Name: ABC Manufacturing
Industry: Manufacturing
Email: abc@abc.com
Country: Japan
```

This confirmed that the CRM application could successfully create and retrieve customer information from the database.

---

# 19. Create the CRM Dashboard View

Django Admin is useful for administration, but the final CRM needs its own user interface.

Open:

```text
crm/views.py
```

Add:

```python
from django.shortcuts import render
from .models import Customer


def dashboard(request):
    customer_count = Customer.objects.count()
    recent_customers = Customer.objects.order_by("-created_at")[:5]

    context = {
        "customer_count": customer_count,
        "recent_customers": recent_customers,
    }

    return render(request, "crm/dashboard.html", context)
```

## Explanation

This line:

```python
customer_count = Customer.objects.count()
```

asks Django's ORM to count all Customer records.

This line:

```python
recent_customers = Customer.objects.order_by("-created_at")[:5]
```

retrieves the five most recently created customers.

The `-` before `created_at` means descending order:

```text
Newest
  ↓
Older
  ↓
Oldest
```

The `context` dictionary:

```python
context = {
    "customer_count": customer_count,
    "recent_customers": recent_customers,
}
```

passes Python data to the HTML template.

Finally:

```python
return render(request, "crm/dashboard.html", context)
```

renders the dashboard HTML and supplies it with the CRM data.

---

# 20. Create CRM URL Routing

Create:

```text
crm/urls.py
```

Add:

```python
from django.urls import path
from . import views


urlpatterns = [
    path("", views.dashboard, name="dashboard"),
]
```

This connects the CRM root URL to the `dashboard` function.

Then modify:

```text
crm_project/urls.py
```

to:

```python
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("crm.urls")),
]
```

The routing process is now:

```text
Browser
   ↓
http://127.0.0.1:8000/
   ↓
crm_project/urls.py
   ↓
crm/urls.py
   ↓
views.dashboard
   ↓
dashboard.html
```

The Django Admin remains available separately at:

```text
/admin/
```

---

# 21. Create the Dashboard Template

Create the following directory structure:

```text
crm/
└── templates/
    └── crm/
        └── dashboard.html
```

The additional `crm` directory inside `templates` provides a namespace for the application's templates.

This becomes increasingly useful when a Django project contains multiple applications.

The dashboard template uses Django Template Language.

For example:

```django
{{ customer_count }}
```

displays the customer count supplied by `views.py`.

The customer list uses:

```django
{% for customer in recent_customers %}
```

This loops through the Customer objects supplied by the view.

Individual fields can then be displayed with:

```django
{{ customer.name }}
{{ customer.industry }}
{{ customer.country }}
{{ customer.email }}
```

The overall data flow is:

```text
SQLite Database
       ↓
Django ORM
       ↓
Customer.objects...
       ↓
views.py
       ↓
context
       ↓
dashboard.html
       ↓
Browser
```

---

# 22. Current Dashboard

The first custom CRM dashboard is now running successfully.

Current dashboard functionality:

- Sidebar navigation
- Customer count
- Contact placeholder
- Opportunity placeholder
- Recent Customer table
- Data retrieved dynamically from SQLite

Current sidebar:

```text
My CRM

Dashboard
Customers
Contacts
Opportunities
Activities
Reports
```

Current test result:

```text
Customers:       1
Contacts:        0
Opportunities:   0

Recent Customers
--------------------------------------------
ABC Manufacturing | Manufacturing | Japan
```

This confirms that the complete flow is working:

```text
Browser
   ↓
Django URL
   ↓
Django View
   ↓
Django ORM
   ↓
SQLite Database
   ↓
Django Template
   ↓
CRM Dashboard
```

---

# 23. Current Project Structure

The project currently has approximately the following structure:

```text
crm-system/
│
├── .venv/
│
├── crm/
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   │
│   ├── templates/
│   │   └── crm/
│   │       └── dashboard.html
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── crm_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
└── README.md
```

---

# 24. Development Roadmap

## Completed

- [x] Create Python project
- [x] Create virtual environment
- [x] Install Django
- [x] Create Django project
- [x] Configure SQLite database
- [x] Create CRM application
- [x] Create Customer model
- [x] Create database migration
- [x] Configure Django Admin
- [x] Create administrator account
- [x] Add first test customer
- [x] Create CRM dashboard
- [x] Display customer count
- [x] Display recent customers

## Next

- [ ] Customer list page
- [ ] Add Customer page
- [ ] Customer detail page
- [ ] Edit Customer
- [ ] Delete Customer
- [ ] Customer search
- [ ] Contact model and management
- [ ] Opportunity model
- [ ] Sales pipeline
- [ ] Activities / follow-ups
- [ ] User authentication
- [ ] User permissions
- [ ] Reports and charts
- [ ] PostgreSQL migration
- [ ] REST API
- [ ] AI-assisted CRM functions

---

# 25. Planned CRM Architecture

```text
                    CRM SYSTEM

                        │
              ┌─────────┴─────────┐
              │                   │
           Django              Database
              │                   │
              │                 SQLite
              │                   │
              │              PostgreSQL
              │               (future)
              │
    ┌─────────┼─────────┐
    │         │         │
 Customers  Contacts  Opportunities
    │         │         │
    └─────────┼─────────┘
              │
          Activities
              │
          Dashboard
              │
           Reports
              │
          REST API
              │
        AI Integration
```

---

# 26. Future AI Features

After the basic CRM is complete, possible AI features include:

- Customer history summarization
- Meeting note summarization
- Automatic extraction of customer information from text
- Suggested follow-up actions
- Opportunity summaries
- Natural-language CRM search
- Detection of customers with overdue follow-ups
- Sales pipeline analysis

Example future query:

```text
Show me opportunities over ¥10 million
that have had no activity during the last 30 days.
```

The objective is to first build a reliable CRM data foundation and then add AI functionality on top of structured CRM data.

---

# 27. Development Notes

To activate the virtual environment when returning to the project:

```powershell
cd D:\MyProjects\crm-system
.\.venv\Scripts\Activate.ps1
```

Then start Django:

```powershell
python manage.py runserver
```

Development dashboard:

```text
http://127.0.0.1:8000/
```

Django administration:

```text
http://127.0.0.1:8000/admin/
```

To stop the development server:

```text
Ctrl + C
```

---

# Project Status

**Day 1 — Initial CRM foundation completed**

The project currently has a working Django backend, SQLite database, Customer model, Django Admin interface, and custom CRM dashboard displaying live customer information.

Next development milestone:

**Customer Management — List, Create, View, Edit, Delete and Search**

---
# 28. Customer List Page

The next step was to create a dedicated Customer Management page.

The goal is to allow users to manage customers through the CRM interface instead of relying on Django Admin.

The first step was to create a Customer List view.

Open:

```text
crm/views.py
```

Keep the existing `dashboard()` function and add:

```python
def customer_list(request):
    customers = Customer.objects.order_by("name")

    context = {
        "customers": customers,
    }

    return render(request, "crm/customer_list.html", context)
```

## Explanation

This line:

```python
customers = Customer.objects.order_by("name")
```

uses the Django ORM to retrieve all Customer records from the database.

`order_by("name")` sorts the results alphabetically by customer name.

For example:

```text
XYZ Industries
ABC Manufacturing
Kobe Engineering
```

will be returned as:

```text
ABC Manufacturing
Kobe Engineering
XYZ Industries
```

The `context` dictionary:

```python
context = {
    "customers": customers,
}
```

passes the Customer QuerySet to the HTML template.

The template can then access the customers using:

```django
{% for customer in customers %}
```

---

# 29. Add the Customer List URL

Open:

```text
crm/urls.py
```

Update the URL configuration:

```python
from django.urls import path
from . import views


urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("customers/", views.customer_list, name="customer_list"),
]
```

The CRM now has the following routes:

```text
/                   → CRM Dashboard

/customers/         → Customer List

/admin/             → Django Administration
```

When the browser requests:

```text
http://127.0.0.1:8000/customers/
```

Django follows:

```text
Browser
   ↓
crm_project/urls.py
   ↓
crm/urls.py
   ↓
customer_list()
   ↓
Customer.objects.order_by("name")
   ↓
customer_list.html
```

---

# 30. Create a Shared Base Template

Originally, the entire page layout and CSS were contained inside:

```text
dashboard.html
```

If the same HTML were copied into every future CRM page, there would be duplicated code for:

- Sidebar
- Page layout
- CSS
- Buttons
- Tables
- Common navigation

Instead, a shared template was created:

```text
crm/templates/crm/base.html
```

The template architecture becomes:

```text
                    base.html
                       │
              Shared CRM Layout
                       │
          ┌────────────┴────────────┐
          │                         │
   dashboard.html            customer_list.html
          │                         │
      Dashboard                  Customers
```

`base.html` contains the common:

- HTML structure
- Sidebar
- Navigation
- CSS
- Main content area
- Button styles
- Table styles

Individual pages only need to provide their own content.

---

# 31. Django Template Inheritance

The shared template contains:

```django
{% block content %}

{% endblock %}
```

This creates a section that child templates can replace with their own content.

A child template begins with:

```django
{% extends "crm/base.html" %}
```

For example:

```django
{% extends "crm/base.html" %}


{% block title %}
CRM Dashboard
{% endblock %}


{% block content %}

<h1>CRM Dashboard</h1>

{% endblock %}
```

The concept is:

```text
base.html
│
├── Sidebar
├── Navigation
├── Common CSS
│
└── {% block content %}
          ↑
          │
          ├── dashboard.html
          ├── customer_list.html
          ├── customer_form.html
          └── future CRM pages
```

This prevents duplicated HTML and makes the CRM interface easier to maintain.

For example, changing the sidebar in `base.html` automatically changes it for every page that extends `base.html`.

---

# 32. Update Dashboard to Use `base.html`

The original `dashboard.html` contained the complete HTML document.

After creating `base.html`, the dashboard was simplified.

It now begins with:

```django
{% extends "crm/base.html" %}
```

and places dashboard-specific content inside:

```django
{% block content %}

...

{% endblock %}
```

The dashboard still receives:

```django
{{ customer_count }}
```

and:

```django
{% for customer in recent_customers %}
```

from the existing dashboard view.

Therefore the database logic did not need to change.

Only the presentation structure was improved.

---

# 33. Create the Customer List Template

Create:

```text
crm/templates/crm/customer_list.html
```

The page extends the common CRM layout:

```django
{% extends "crm/base.html" %}
```

The Customer List receives:

```python
customers
```

from the `customer_list()` view.

The template loops through the records:

```django
{% for customer in customers %}
```

and displays:

```django
{{ customer.name }}
{{ customer.industry }}
{{ customer.country }}
{{ customer.email }}
{{ customer.phone }}
```

The resulting page displays customer information in a table.

Conceptually:

```text
SQLite
   ↓
Customer.objects.order_by("name")
   ↓
customer_list()
   ↓
context["customers"]
   ↓
customer_list.html
   ↓
Customer Table
```

---

# 34. Connect the Customers Sidebar Link

The Customers navigation item originally used:

```html
<a href="#">
    Customers
</a>
```

This was changed to:

```django
<a href="{% url 'customer_list' %}">
    Customers
</a>
```

The Django template tag:

```django
{% url 'customer_list' %}
```

looks for the URL whose name is:

```text
customer_list
```

which was defined in:

```python
path(
    "customers/",
    views.customer_list,
    name="customer_list"
)
```

Django therefore generates:

```text
/customers/
```

Using named URLs is preferable to hard-coding URLs because the actual path can later be changed without rewriting every template.

---

# 35. Create `forms.py`

To allow customers to be created through the CRM interface, a Django `ModelForm` was introduced.

Create:

```text
crm/forms.py
```

Add:

```python
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
```

## What is a ModelForm?

The existing:

```python
class Customer(models.Model):
```

defines how Customer information is stored.

The new:

```python
class CustomerForm(forms.ModelForm):
```

creates a form based on that model.

The relationship is:

```text
Customer Model
      ↓
CustomerForm
      ↓
HTML Form
      ↓
User Input
      ↓
Validation
      ↓
Customer Record
```

The following fields are included:

```text
name
industry
website
phone
email
address
country
```

The following fields are not included:

```text
created_at
updated_at
```

because Django automatically manages them.

---

# 36. Create the Add Customer View

The next step was to create a view that handles both displaying and processing the Customer form.

Open:

```text
crm/views.py
```

The required imports are:

```python
from django.shortcuts import redirect, render

from .forms import CustomerForm
from .models import Customer
```

Add:

```python
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
```

This view handles two different types of HTTP requests:

```text
GET
POST
```

---

# 37. Understanding GET Requests

When the browser first opens:

```text
/customers/add/
```

the browser sends a GET request.

Therefore:

```python
if request.method == "POST":
```

is false.

Django executes:

```python
else:
    form = CustomerForm()
```

This creates an empty Customer form.

The process is:

```text
Browser
   ↓
GET /customers/add/
   ↓
customer_create()
   ↓
CustomerForm()
   ↓
Empty Form
   ↓
customer_form.html
   ↓
Browser
```

GET is normally used when retrieving or displaying information.

---

# 38. Understanding POST Requests

After entering Customer information and clicking the Save button, the browser sends a POST request.

Django executes:

```python
if request.method == "POST":
```

and creates:

```python
form = CustomerForm(request.POST)
```

`request.POST` contains the submitted form data.

For example:

```text
name       = Kobe Engineering
industry   = Engineering
phone      = 078-555-1234
email      = sales@example.com
country    = Japan
```

The form is then validated:

```python
if form.is_valid():
```

If validation succeeds:

```python
form.save()
```

creates the Customer record in the database.

The complete process is:

```text
Customer Form
      ↓
User enters data
      ↓
POST Request
      ↓
CustomerForm(request.POST)
      ↓
form.is_valid()
      ↓
form.save()
      ↓
Django ORM
      ↓
SQLite
```

---

# 39. Redirect After Saving

After successfully creating the Customer:

```python
return redirect("customer_list")
```

redirects the browser to the Customer List.

This produces the workflow:

```text
/customers/add/
      ↓
Enter Customer
      ↓
Save Customer
      ↓
Database
      ↓
redirect()
      ↓
/customers/
```

This prevents the user from remaining on the submitted form after the record has been created.

---

# 40. Add the Customer Create URL

Open:

```text
crm/urls.py
```

Add:

```python
path(
    "customers/add/",
    views.customer_create,
    name="customer_create"
),
```

The URL configuration now contains:

```text
/                       Dashboard

/customers/             Customer List

/customers/add/         Add Customer

/admin/                 Django Admin
```

---

# 41. Connect the Add Customer Button

The Customer List contains an Add Customer button.

The correct link is:

```django
<a href="{% url 'customer_create' %}" class="button">
    + Add Customer
</a>
```

Django resolves:

```django
{% url 'customer_create' %}
```

using:

```python
name="customer_create"
```

and generates:

```text
/customers/add/
```

---

# 42. Error Encountered — Incorrect URL Template Syntax

During development, clicking the Add Customer button initially produced:

```text
Page not found (404)
```

The browser attempted to access:

```text
/customers/% url 'customer_create' %
```

The reason was an incorrectly written Django template tag.

Incorrect:

```text
% url 'customer_create' %
```

Correct:

```django
{% url 'customer_create' %}
```

Django template tags require:

```text
{% ... %}
```

including both:

```text
{
}
```

curly braces.

Without them, Django treats:

```text
% url 'customer_create' %
```

as ordinary text.

The browser then interpreted the text as part of a relative URL.

After correcting the template to:

```django
{% url 'customer_create' %}
```

the button correctly opened:

```text
/customers/add/
```

---

# 43. Create the Customer Form Template

Create:

```text
crm/templates/crm/customer_form.html
```

The form uses:

```html
<form method="post">
```

The fields are displayed using Django form objects.

For example:

```django
{{ form.name }}
{{ form.industry }}
{{ form.website }}
{{ form.phone }}
{{ form.email }}
{{ form.address }}
{{ form.country }}
```

Field errors can also be displayed:

```django
{{ form.name.errors }}
```

The Save button uses:

```html
<button type="submit" class="button">
    Save Customer
</button>
```

When clicked, the browser submits the form as a POST request.

---

# 44. CSRF Protection

The Customer form includes:

```django
{% csrf_token %}
```

CSRF stands for:

```text
Cross-Site Request Forgery
```

Django uses CSRF protection for POST requests.

The standard Django POST form pattern is:

```html
<form method="post">

    {% csrf_token %}

    ...

</form>
```

The CSRF token helps Django verify that the request came from a valid form generated by the application.

Without the token, Django will normally reject the POST request.

---

# 45. Add Form Styling

The shared:

```text
base.html
```

was extended with CSS for:

- Form container
- Form fields
- Labels
- Text areas
- Focus states
- Buttons
- Cancel links
- Validation errors

Because the styles are stored in `base.html`, they can later be reused by:

```text
Add Customer
Edit Customer
Add Contact
Edit Contact
Add Opportunity
Edit Opportunity
```

This is another advantage of having a shared base template.

---

# 46. Error Encountered — `redirect` Not Defined

After submitting the Customer form, Django returned:

```text
NameError at /customers/add/

name 'redirect' is not defined
```

The error occurred at:

```python
return redirect("customer_list")
```

The reason was that `redirect` had not been imported.

The original import was:

```python
from django.shortcuts import render
```

It was changed to:

```python
from django.shortcuts import redirect, render
```

## Explanation

Python only knows names that have been:

- Defined
- Imported
- Made available by another valid mechanism

Although Django provides a `redirect()` helper, it must be imported before it can be used in `views.py`.

After importing:

```python
redirect
```

the following works:

```python
return redirect("customer_list")
```

---

# 47. Important Observation About `form.save()`

The `redirect` error happened after:

```python
form.save()
```

had already executed.

Therefore the Customer may already have been inserted into SQLite even though the browser displayed an error page.

The sequence was:

```text
form.is_valid()
      ↓
form.save()          ← Customer saved successfully
      ↓
redirect()           ← Error occurred here
```

For this reason, the Customer List was checked before submitting the same form again.

Otherwise a duplicate Customer could have been created.

This is an important debugging lesson:

> A web request can fail after some database operations have already completed.

---

# 48. Customer Creation Successfully Tested

After fixing the missing `redirect` import, the complete Customer creation process worked successfully.

The user can now:

1. Open the Customer List.
2. Click **+ Add Customer**.
3. Enter Customer information.
4. Submit the form.
5. Have Django validate the information.
6. Save the Customer to SQLite.
7. Automatically return to the Customer List.
8. See the new Customer in the table.

The Dashboard Customer count also updates automatically because it uses:

```python
Customer.objects.count()
```

For example:

```text
Before adding customer:

Customers
1
```

After adding another customer:

```text
Customers
2
```

No dashboard source code needs to be changed.

---

# 49. Current CRUD Progress

CRUD means:

```text
C = Create
R = Read
U = Update
D = Delete
```

Current status:

```text
Create    ✅
Read      ✅
Update    ⬜
Delete    ⬜
```

### Create

Implemented using:

```text
/customers/add/
```

### Read

Implemented using:

```text
/customers/
```

The next stages will implement:

```text
/customers/<id>/

/customers/<id>/edit/

/customers/<id>/delete/
```

---

# 50. Updated Project Structure

The project now contains:

```text
crm-system/
│
├── .venv/
│
├── crm/
│   │
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   │
│   ├── templates/
│   │   └── crm/
│   │       ├── base.html
│   │       ├── dashboard.html
│   │       ├── customer_list.html
│   │       └── customer_form.html
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── crm_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── db.sqlite3
├── manage.py
└── README.md
```

The important additions from this development session are:

```text
forms.py
base.html
customer_list.html
customer_form.html
```

---

# 51. Updated Development Roadmap

## Completed

- [x] Create Python project
- [x] Create virtual environment
- [x] Install Django
- [x] Create Django project
- [x] Configure SQLite database
- [x] Create CRM application
- [x] Create Customer model
- [x] Create database migration
- [x] Configure Django Admin
- [x] Create administrator account
- [x] Add first test customer
- [x] Create CRM dashboard
- [x] Display customer count
- [x] Display recent customers
- [x] Create shared base template
- [x] Implement template inheritance
- [x] Create Customer List page
- [x] Connect Customers navigation
- [x] Create `CustomerForm`
- [x] Create Add Customer page
- [x] Process GET requests
- [x] Process POST requests
- [x] Validate Customer data
- [x] Save Customer to database
- [x] Redirect after Customer creation
- [x] Add CSRF protection
- [x] Add reusable form styling
- [x] Debug incorrect Django URL template syntax
- [x] Debug missing `redirect` import

## Next

- [ ] Customer Detail page
- [ ] Customer ID / Primary Key routing
- [ ] Edit Customer
- [ ] Delete Customer
- [ ] Customer search
- [ ] Contact model and management
- [ ] Opportunity model
- [ ] Sales pipeline
- [ ] Activities / follow-ups
- [ ] User authentication
- [ ] User permissions
- [ ] Reports and charts
- [ ] PostgreSQL migration
- [ ] REST API
- [ ] AI-assisted CRM functions

---

# Day 2 Project Status

**Customer Management — Create and Read completed**

The CRM can now create and display Customer records through its own user interface without requiring Django Admin.

Current request flow:

```text
Browser
   ↓
CRM URL
   ↓
Django View
   ↓
CustomerForm
   ↓
Validation
   ↓
Django ORM
   ↓
SQLite Database
   ↓
Redirect
   ↓
Customer List
```

Current CRUD status:

```text
Create    ██████████  Complete
Read      ██████████  Complete
Update    ░░░░░░░░░░  Next
Delete    ░░░░░░░░░░  Next
```

Next development milestone:

**Customer Details, Edit, Delete and Search**

Append that directly after your existing README. For today's Git commit, I would use:

```powershell
git add .
git commit -m "Day 2 - Add Customer List and Create Customer Form"
git push
```


