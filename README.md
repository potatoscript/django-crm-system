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
<a id="table-of-contents"></a>
# Table of Contents

## Day 1 — CRM Foundation

1. [Development Environment](#1-development-environment)
2. [Create the Project Directory](#2-create-the-project-directory)
3. [Create a Python Virtual Environment](#3-create-a-python-virtual-environment)
4. [Virtual Environment Creation Problem](#4-virtual-environment-creation-problem)
5. [Check pip](#5-check-pip)
6. [Recreate the Virtual Environment](#6-recreate-the-virtual-environment)
7. [Verify the Virtual Environment](#7-verify-the-virtual-environment)
8. [Upgrade pip](#8-upgrade-pip)
9. [Install Django](#9-install-django)
10. [Create the Django Project](#10-create-the-django-project)
11. [Create the Initial Django Database](#11-create-the-initial-django-database)
12. [Start the Django Development Server](#12-start-the-django-development-server)
13. [Create the CRM Application](#13-create-the-crm-application)
14. [Register the CRM Application](#14-register-the-crm-application)
15. [Create the Customer Model](#15-create-the-customer-model)
16. [Create the Customer Database Table](#16-create-the-customer-database-table)
17. [Register Customer in Django Admin](#17-register-customer-in-django-admin)
18. [Create a Django Administrator](#18-create-a-django-administrator)
19. [Create the CRM Dashboard View](#19-create-the-crm-dashboard-view)
20. [Create CRM URL Routing](#20-create-crm-url-routing)
21. [Create the Dashboard Template](#21-create-the-dashboard-template)
22. [Current Dashboard](#22-current-dashboard)
23. [Current Project Structure](#23-current-project-structure)
24. [Development Roadmap](#24-development-roadmap)
25. [Planned CRM Architecture](#25-planned-crm-architecture)
26. [Future AI Features](#26-future-ai-features)
27. [Development Notes](#27-development-notes)

## Day 2 — Customer List and Create

28. [Customer List Page](#28-customer-list-page)
29. [Add the Customer List URL](#29-add-the-customer-list-url)
30. [Create a Shared Base Template](#30-create-a-shared-base-template)
31. [Django Template Inheritance](#31-django-template-inheritance)
32. [Update Dashboard to Use base.html](#32-update-dashboard-to-use-basehtml)
33. [Create the Customer List Template](#33-create-the-customer-list-template)
34. [Connect the Customers Sidebar Link](#34-connect-the-customers-sidebar-link)
35. [Create forms.py](#35-create-formspy)
36. [Create the Add Customer View](#36-create-the-add-customer-view)
37. [Understanding GET Requests](#37-understanding-get-requests)
38. [Understanding POST Requests](#38-understanding-post-requests)
39. [Redirect After Saving](#39-redirect-after-saving)
40. [Add the Customer Create URL](#40-add-the-customer-create-url)
41. [Connect the Add Customer Button](#41-connect-the-add-customer-button)
42. [Error Encountered — Incorrect URL Template Syntax](#42-error-encountered--incorrect-url-template-syntax)
43. [Create the Customer Form Template](#43-create-the-customer-form-template)
44. [CSRF Protection](#44-csrf-protection)
45. [Add Form Styling](#45-add-form-styling)
46. [Error Encountered — redirect Not Defined](#46-error-encountered--redirect-not-defined)
47. [Important Observation About form.save()](#47-important-observation-about-formsave)
48. [Customer Creation Successfully Tested](#48-customer-creation-successfully-tested)
49. [Current CRUD Progress](#49-current-crud-progress)
50. [Updated Project Structure](#50-updated-project-structure)
51. [Updated Development Roadmap](#51-updated-development-roadmap)

## Day 3 — Customer Detail, Update and Delete

52. [Python 3.11 Virtual Environment Problem](#52-python-311-virtual-environment-problem)
53. [Recreate the Virtual Environment with Python 3.13](#53-recreate-the-virtual-environment-with-python-313)
54. [Reinstall Django in the New Virtual Environment](#54-reinstall-django-in-the-new-virtual-environment)
55. [Configure VS Code to Use the New Virtual Environment](#55-configure-vs-code-to-use-the-new-virtual-environment)
56. [Database Configuration Location](#56-database-configuration-location)
57. [Customer Detail Page](#57-customer-detail-page)
58. [Understanding Django Primary Keys](#58-understanding-django-primary-keys)
59. [Import get_object_or_404](#59-import-get_object_or_404)
60. [Create the Customer Detail View](#60-create-the-customer-detail-view)
61. [Add the Customer Detail URL](#61-add-the-customer-detail-url)
62. [Make Customer Names Clickable](#62-make-customer-names-clickable)
63. [Create the Customer Detail Template](#63-create-the-customer-detail-template)
64. [Customer Detail Request Flow](#64-customer-detail-request-flow)
65. [Create the Edit Customer View](#65-create-the-edit-customer-view)
66. [Understanding instance=customer](#66-understanding-instancecustomer)
67. [Add the Edit Customer URL](#67-add-the-edit-customer-url)
68. [Reuse the Customer Form Template](#68-reuse-the-customer-form-template)
69. [Edit Customer Database Operation](#69-edit-customer-database-operation)
70. [Create the Delete Customer View](#70-create-the-delete-customer-view)
71. [Why Delete Uses POST](#71-why-delete-uses-post)
72. [Add the Delete Customer URL](#72-add-the-delete-customer-url)
73. [Add the Delete Customer Button](#73-add-the-delete-customer-button)
74. [Create the Delete Confirmation Page](#74-create-the-delete-confirmation-page)
75. [Delete Customer Request Flow](#75-delete-customer-request-flow)
76. [Primary Keys After Deletion](#76-primary-keys-after-deletion)
77. [Current Customer URL Architecture](#77-current-customer-url-architecture)
78. [Current Customer Request Architecture](#78-current-customer-request-architecture)
79. [Customer CRUD Completed](#79-customer-crud-completed)
80. [Updated Project Structure](#80-updated-project-structure)
81. [Updated Development Roadmap](#81-updated-development-roadmap)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

[⬆ Back to Table of Contents](#table-of-contents)

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

# Day 3 — Customer Detail, Update and Delete

Day 3 continued the Customer Management module.

At the beginning of Day 3, the CRM already supported:

```text
Create    ✅
Read      ✅ Customer List
Update    ⬜
Delete    ⬜
```

The objectives for Day 3 were:

- Add an individual Customer Detail page
- Understand Django primary keys
- Retrieve individual database records
- Edit existing Customer records
- Reuse the existing `CustomerForm`
- Delete Customer records
- Add a confirmation page before deletion
- Complete the basic Customer CRUD cycle

During the development session, the Python environment was also migrated from Python 3.11 to Python 3.13.

[⬆ Back to Table of Contents](#table-of-contents)

---

# 52. Python 3.11 Virtual Environment Problem

Before continuing development, the existing virtual environment stopped working after Python 3.11 was uninstalled from Windows.

Running:

```powershell
python manage.py runserver
```

produced:

```text
No Python at '"C:\Python311\python.exe'
```

Even though PowerShell displayed:

```text
(.venv)
```

the existing virtual environment had originally been created using Python 3.11.

A Python virtual environment remembers the Python installation that was used to create it.

Conceptually:

```text
Old .venv
    │
    └── Created using
            │
            ↓
    C:\Python311\python.exe
```

After Python 3.11 was removed, the virtual environment could no longer find its original Python interpreter.

The CRM source code itself was not damaged.

The problem was only the virtual environment.

[⬆ Back to Table of Contents](#table-of-contents)

---

# 53. Recreate the Virtual Environment with Python 3.13

The old `.venv` was removed and recreated using Python 3.13.

Check the installed Python versions:

```powershell
py -0p
```

Check Python 3.13 directly:

```powershell
py -3.13 --version
```

The old virtual environment can be removed with:

```powershell
Remove-Item -Recurse -Force .venv
```

Verify that it was removed:

```powershell
Test-Path .venv
```

Expected result:

```text
False
```

Create a new virtual environment explicitly using Python 3.13:

```powershell
py -3.13 -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

Verify Python:

```powershell
python --version
```

The environment should now use:

```text
Python 3.13.x
```

The exact Python executable can be checked with:

```powershell
python -c "import sys; print(sys.executable)"
```

It should point to:

```text
D:\MyProjects\crm-system\.venv\Scripts\python.exe
```

The important architecture is now:

```text
Python 3.13
     │
     ↓
.venv
     │
     ├── Python
     ├── pip
     └── Django
          │
          ↓
      CRM Project
```

[⬆ Back to Table of Contents](#table-of-contents)

---

# 54. Reinstall Django in the New Virtual Environment

Because Python packages are stored inside the virtual environment, deleting `.venv` also removed the Django installation associated with the old environment.

Upgrade pip:

```powershell
python -m pip install --upgrade pip
```

Install Django 5.2:

```powershell
python -m pip install "Django>=5.2,<5.3"
```

Verify Django:

```powershell
python -m django --version
```

Then start the existing CRM:

```powershell
python manage.py runserver
```

There was no need to recreate:

- `crm_project`
- `crm`
- Customer model
- migrations
- templates
- SQLite database

Those files exist outside `.venv`.

[⬆ Back to Table of Contents](#table-of-contents)

---

# 55. Configure VS Code to Use the New Virtual Environment

Visual Studio Code was configured to use the new Python 3.13 environment.

Open the Command Palette:

```text
Ctrl + Shift + P
```

Select:

```text
Python: Select Interpreter
```

Then select:

```text
.venv\Scripts\python.exe
```

The selected interpreter should correspond to Python 3.13.

This ensures that VS Code, the terminal, Python extensions, and Django development use the project's virtual environment rather than an unrelated global Python installation.

[⬆ Back to Table of Contents](#table-of-contents)

---

# 56. Database Configuration Location

The Django database configuration is located in:

```text
crm_project/settings.py
```

The current configuration uses SQLite:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

This means:

```text
ENGINE
   ↓
django.db.backends.sqlite3
   ↓
Use SQLite
```

and:

```text
NAME
   ↓
BASE_DIR / "db.sqlite3"
   ↓
D:\MyProjects\crm-system\db.sqlite3
```

There are three related but different parts:

```text
settings.py
    ↓
Defines which database Django uses

models.py
    ↓
Defines the application's data structure

db.sqlite3
    ↓
Contains the actual database records
```

The current Customer data is stored in the SQLite database.

[⬆ Back to Table of Contents](#table-of-contents)

---

# 57. Customer Detail Page

The Customer List already displayed multiple customers.

The next requirement was to allow each Customer to have an individual page.

The desired URL structure was:

```text
/customers/1/
/customers/2/
/customers/3/
```

Each number identifies a specific Customer database record.

For example:

```text
ID 1 → ABC Manufacturing

ID 2 → Kobe Engineering
```

Therefore:

```text
/customers/2/
```

displays Customer 2.

[⬆ Back to Table of Contents](#table-of-contents)

---

# 58. Understanding Django Primary Keys

The Customer model did not explicitly define an `id` field:

```python
class Customer(models.Model):
    name = models.CharField(max_length=200)
```

However, Django automatically provides a primary key when no custom primary key is specified.

Conceptually, the database contains:

```text
crm_customer

id    name
--------------------------------
1     ABC Manufacturing
2     Kobe Engineering
3     Osaka Industries
```

The primary key uniquely identifies a database record.

Django commonly refers to a primary key as:

```text
pk
```

which means:

```text
Primary Key
```

The primary key is used in the Customer Detail, Edit, and Delete URLs.

[⬆ Back to Table of Contents](#table-of-contents)

---

# 59. Import `get_object_or_404`

The following import was added to:

```text
crm/views.py
```

```python
from django.shortcuts import get_object_or_404, redirect, render
```

`get_object_or_404()` is used to retrieve a database object safely.

For example:

```python
customer = get_object_or_404(Customer, pk=pk)
```

means:

```text
Find the Customer
whose primary key equals pk.
```

If the Customer exists, Django returns it.

If it does not exist, Django returns:

```text
404 Not Found
```

instead of allowing an unhandled object lookup error.

[⬆ Back to Table of Contents](#table-of-contents)

---

# 60. Create the Customer Detail View

The following view was added to:

```text
crm/views.py
```

```python
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
```

If the browser requests:

```text
/customers/2/
```

then:

```python
pk = 2
```

Django executes:

```python
get_object_or_404(Customer, pk=2)
```

and retrieves Customer 2.

The resulting object is passed to the template using:

```python
context = {
    "customer": customer,
}
```

The template can then access:

```django
{{ customer.name }}
{{ customer.industry }}
{{ customer.email }}
{{ customer.phone }}
{{ customer.country }}
```

[⬆ Back to Table of Contents](#table-of-contents)

---

# 61. Add the Customer Detail URL

The following URL was added to:

```text
crm/urls.py
```

```python
path(
    "customers/<int:pk>/",
    views.customer_detail,
    name="customer_detail"
),
```

The important part is:

```text
<int:pk>
```

This means:

```text
int
 ↓
Accept an integer from the URL

pk
 ↓
Pass that integer to the view using the name "pk"
```

For example:

```text
/customers/2/
```

becomes:

```python
customer_detail(request, pk=2)
```

The request flow is:

```text
/customers/2/
      ↓
<int:pk>
      ↓
pk = 2
      ↓
customer_detail()
      ↓
get_object_or_404()
      ↓
Customer ID 2
```

[⬆ Back to Table of Contents](#table-of-contents)

---

# 62. Make Customer Names Clickable

The Customer List was updated so that the Customer name links to the individual Customer Detail page.

The Customer name changed from:

```django
<td>
    {{ customer.name }}
</td>
```

to:

```django
<td>
    <a href="{% url 'customer_detail' customer.pk %}">
        {{ customer.name }}
    </a>
</td>
```

This URL requires a Customer primary key.

For example:

```django
{% url 'customer_detail' customer.pk %}
```

for Customer 2 generates:

```text
/customers/2/
```

This is different from a URL such as:

```django
{% url 'customer_create' %}
```

because `customer_create` does not require a database ID.

[⬆ Back to Table of Contents](#table-of-contents)

---

# 63. Create the Customer Detail Template

A new template was created:

```text
crm/templates/crm/customer_detail.html
```

The page displays:

- Customer name
- Industry
- Country
- Email
- Phone
- Website
- Address
- Created date
- Last updated date

Customer fields are accessed using expressions such as:

```django
{{ customer.name }}
```

and:

```django
{{ customer.industry }}
```

Optional values can use the Django `default` filter:

```django
{{ customer.industry|default:"-" }}
```

If the field contains:

```text
Manufacturing
```

the page displays:

```text
Manufacturing
```

If the field is empty, the page displays:

```text
-
```

This provides a cleaner Detail page when optional Customer information is missing.

[⬆ Back to Table of Contents](#table-of-contents)

---

# 64. Customer Detail Request Flow

The complete Customer Detail process is:

```text
Customer List
      ↓
Click Customer
      ↓
/customers/2/
      ↓
crm/urls.py
      ↓
<int:pk>
      ↓
customer_detail(request, pk=2)
      ↓
get_object_or_404(Customer, pk=2)
      ↓
Django ORM
      ↓
SQLite
      ↓
Customer Object
      ↓
customer_detail.html
      ↓
Browser
```

Requesting a non-existing Customer, for example:

```text
/customers/99999/
```

returns:

```text
404 Not Found
```

because the view uses:

```python
get_object_or_404()
```

[⬆ Back to Table of Contents](#table-of-contents)

---

# 65. Create the Edit Customer View

The next step was to implement the Update part of CRUD.

Instead of creating another form, the existing:

```text
CustomerForm
```

was reused.

Add to:

```text
crm/views.py
```

```python
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
```

The most important new concept is:

```python
instance=customer
```

[⬆ Back to Table of Contents](#table-of-contents)

---

# 66. Understanding `instance=customer`

When creating a new Customer, the CRM uses:

```python
CustomerForm()
```

or:

```python
CustomerForm(request.POST)
```

This means:

```text
Create a new Customer
```

For editing, the CRM uses:

```python
CustomerForm(instance=customer)
```

This tells Django:

```text
Use this existing Customer
and populate the form with its current information.
```

When processing the submitted Edit form:

```python
CustomerForm(
    request.POST,
    instance=customer
)
```

tells Django:

```text
Validate the submitted information
and update this existing Customer.
```

Without:

```python
instance=customer
```

the application could create another Customer instead of updating the existing record.

[⬆ Back to Table of Contents](#table-of-contents)

---

# 67. Add the Edit Customer URL

The following URL was added:

```python
path(
    "customers/<int:pk>/edit/",
    views.customer_update,
    name="customer_update"
),
```

The CRM now supports:

```text
/customers/2/
    ↓
View Customer 2


/customers/2/edit/
    ↓
Edit Customer 2
```

The Edit button uses:

```django
{% url 'customer_update' customer.pk %}
```

For Customer 2, Django generates:

```text
/customers/2/edit/
```

[⬆ Back to Table of Contents](#table-of-contents)

---

# 68. Reuse the Customer Form Template

The existing:

```text
customer_form.html
```

was reused for both:

```text
Add Customer
```

and:

```text
Edit Customer
```

The template can determine whether a Customer object exists:

```django
{% if customer %}
```

For editing:

```text
customer exists
      ↓
Edit Customer
```

For creation:

```text
customer does not exist
      ↓
Add Customer
```

For example:

```django
{% if customer %}
    Edit Customer
{% else %}
    Add Customer
{% endif %}
```

The same logic is used for the button:

```django
<button type="submit" class="button">

    {% if customer %}
        Update Customer
    {% else %}
        Save Customer
    {% endif %}

</button>
```

This allows one reusable template to support both operations:

```text
                    customer_form.html
                           │
               ┌───────────┴───────────┐
               ↓                       ↓
      customer_create()       customer_update()
               ↓                       ↓
         Add Customer             Edit Customer
```

This avoids duplicated HTML.

[⬆ Back to Table of Contents](#table-of-contents)

---

# 69. Edit Customer Database Operation

The difference between Create and Update is important.

## Create

```python
form = CustomerForm(request.POST)
form.save()
```

Conceptually performs:

```sql
INSERT INTO crm_customer (...)
VALUES (...);
```

A new database row is created.

## Update

```python
form = CustomerForm(
    request.POST,
    instance=customer
)

form.save()
```

Conceptually performs:

```sql
UPDATE crm_customer
SET ...
WHERE id = 2;
```

The existing database record is modified.

Therefore:

```python
instance=customer
```

is what connects the submitted form to the existing database object.

[⬆ Back to Table of Contents](#table-of-contents)

---

# 70. Create the Delete Customer View

After Update was working, the Delete part of CRUD was implemented.

Add to:

```text
crm/views.py
```

```python
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
```

The Customer is first retrieved using:

```python
get_object_or_404(Customer, pk=pk)
```

The actual deletion only occurs when:

```python
request.method == "POST"
```

and:

```python
customer.delete()
```

is executed.

[⬆ Back to Table of Contents](#table-of-contents)

---

# 71. Why Delete Uses POST

Opening:

```text
/customers/2/delete/
```

does not immediately delete Customer 2.

A GET request only displays the confirmation page.

The flow is:

```text
GET /customers/2/delete/
        ↓
Display confirmation page
        ↓
No database deletion
```

Only after the user confirms deletion does the form send:

```text
POST /customers/2/delete/
```

Then Django executes:

```python
customer.delete()
```

Conceptually:

```sql
DELETE FROM crm_customer
WHERE id = 2;
```

This design prevents a Customer from being deleted simply by visiting a URL.

[⬆ Back to Table of Contents](#table-of-contents)

---

# 72. Add the Delete Customer URL

The following route was added:

```python
path(
    "customers/<int:pk>/delete/",
    views.customer_delete,
    name="customer_delete"
),
```

Customer routing now includes:

```text
/customers/                 Customer List

/customers/add/             Add Customer

/customers/1/               Customer Detail

/customers/1/edit/          Edit Customer

/customers/1/delete/        Delete Customer
```

All Customer-specific operations use the Customer primary key.

[⬆ Back to Table of Contents](#table-of-contents)

---

# 73. Add the Delete Customer Button

The Customer Detail page now contains both:

```text
Edit Customer
Delete Customer
```

The Delete link uses:

```django
<a href="{% url 'customer_delete' customer.pk %}"
   class="delete-button">

    Delete Customer

</a>
```

For Customer 2:

```django
{% url 'customer_delete' customer.pk %}
```

generates:

```text
/customers/2/delete/
```

[⬆ Back to Table of Contents](#table-of-contents)

---

# 74. Create the Delete Confirmation Page

A new template was created:

```text
crm/templates/crm/customer_confirm_delete.html
```

The confirmation page displays the Customer name and warns the user before deleting the record.

The form uses:

```html
<form method="post">
```

and:

```django
{% csrf_token %}
```

The user can choose:

```text
Yes, Delete Customer
```

or:

```text
Cancel
```

Cancel returns to:

```text
/customers/<id>/
```

without changing the database.

Confirming sends a POST request and deletes the Customer.

[⬆ Back to Table of Contents](#table-of-contents)

---

# 75. Delete Customer Request Flow

The complete deletion process is:

```text
Customer Detail
      ↓
Delete Customer
      ↓
GET /customers/2/delete/
      ↓
customer_delete()
      ↓
Confirmation Page
      ↓
User confirms
      ↓
POST /customers/2/delete/
      ↓
customer_delete()
      ↓
customer.delete()
      ↓
SQLite
      ↓
Customer removed
      ↓
redirect("customer_list")
      ↓
/customers/
```

This provides protection against accidental deletion.

[⬆ Back to Table of Contents](#table-of-contents)

---

# 76. Primary Keys After Deletion

Database primary keys should not be treated as continuous Customer numbers.

For example:

```text
ID 1    ABC Manufacturing
ID 2    Kobe Engineering
ID 3    Delete Test Customer
```

After deleting Customer 3:

```text
ID 1    ABC Manufacturing
ID 2    Kobe Engineering
```

the next Customer may receive:

```text
ID 4    New Customer
```

instead of reusing:

```text
ID 3
```

This is normal.

A primary key exists to uniquely identify a database record.

It does not need to remain sequential without gaps.

[⬆ Back to Table of Contents](#table-of-contents)

---

# 77. Current Customer URL Architecture

The Customer Management module now has:

```text
                         Customers
                             │
              ┌──────────────┼──────────────┐
              │              │              │
             List           Create         Detail
              │              │              │
              │              │        ┌─────┴─────┐
              │              │        │           │
              │              │       Edit       Delete
              │              │        │           │
              ↓              ↓        ↓           ↓
       /customers/   /customers/add/  /edit/    /delete/
```

More specifically:

```text
/                           CRM Dashboard

/customers/                 Customer List

/customers/add/             Create Customer

/customers/<pk>/            Customer Detail

/customers/<pk>/edit/       Update Customer

/customers/<pk>/delete/     Delete Customer

/admin/                     Django Admin
```

[⬆ Back to Table of Contents](#table-of-contents)

---

# 78. Current Customer Request Architecture

The Customer Management data flow is now:

```text
                         Browser
                            │
                            ↓
                       crm/urls.py
                            │
              ┌─────────────┼─────────────┐
              ↓             ↓             ↓
        customer_list   customer_create   customer_detail
              │             │             │
              │             │        ┌────┴────┐
              │             │        ↓         ↓
              │             │     update     delete
              │             │        │         │
              └─────────────┼────────┴─────────┘
                            ↓
                       Django ORM
                            ↓
                         Customer
                            ↓
                         SQLite
```

The views communicate with the database through Django's ORM rather than manually writing SQL.

[⬆ Back to Table of Contents](#table-of-contents)

---

# 79. Customer CRUD Completed

The basic Customer CRUD cycle is now complete.

CRUD means:

```text
C = Create
R = Read
U = Update
D = Delete
```

Current implementation:

```text
Create    ✅
│
└── /customers/add/


Read      ✅
│
├── /customers/
│
└── /customers/<pk>/


Update    ✅
│
└── /customers/<pk>/edit/


Delete    ✅
│
└── /customers/<pk>/delete/
```

The CRM can now:

- Create Customers
- Display all Customers
- Display an individual Customer
- Edit Customer information
- Delete Customers safely using a confirmation page

All of these operations are available through the custom CRM interface instead of Django Admin.

[⬆ Back to Table of Contents](#table-of-contents)

---

# 80. Updated Project Structure

The project now has approximately the following structure:

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
│   │       ├── customer_form.html
│   │       ├── customer_detail.html
│   │       └── customer_confirm_delete.html
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

New Customer templates added during Day 3:

```text
customer_detail.html
customer_confirm_delete.html
```

The existing:

```text
customer_form.html
```

is now reused for both Create and Update operations.

[⬆ Back to Table of Contents](#table-of-contents)

---

# 81. Updated Development Roadmap

## Completed

- [x] Python virtual environment
- [x] Django installation
- [x] Django CRM project
- [x] SQLite database
- [x] CRM application
- [x] Customer model
- [x] Database migrations
- [x] Django Admin
- [x] CRM Dashboard
- [x] Dynamic Customer count
- [x] Recent Customers
- [x] Shared base template
- [x] Customer List
- [x] Add Customer
- [x] Django `ModelForm`
- [x] Form validation
- [x] CSRF protection
- [x] Customer Detail
- [x] Primary key URL routing
- [x] `get_object_or_404`
- [x] Edit Customer
- [x] Reuse Customer form for Create and Update
- [x] Delete Customer
- [x] Delete confirmation page
- [x] Complete Customer CRUD
- [x] Migrate development environment from Python 3.11 to Python 3.13

## Next

- [ ] Customer Search
- [ ] Customer List pagination
- [ ] Contact model
- [ ] Link Contacts to Customers
- [ ] Contact Management CRUD
- [ ] Opportunity model
- [ ] Opportunity Management
- [ ] Sales Pipeline
- [ ] Activities / Follow-ups
- [ ] User Authentication
- [ ] User Permissions
- [ ] Reports and Charts
- [ ] PostgreSQL migration
- [ ] REST API
- [ ] AI-assisted CRM functions

---

# Day 3 Project Status

**Customer CRUD completed successfully**

The CRM now provides a complete basic Customer Management workflow:

```text
                    CUSTOMER MANAGEMENT

                           List
                            │
              ┌─────────────┼─────────────┐
              ↓             ↓             ↓
            Create        Detail         Search
              ✅            ✅              ⬜
                            │
                     ┌──────┴──────┐
                     ↓             ↓
                    Edit         Delete
                     ✅             ✅
```

Current CRUD status:

```text
Create    ██████████  Complete
Read      ██████████  Complete
Update    ██████████  Complete
Delete    ██████████  Complete
```

The Customer module now supports:

```text
Customer List
     ↓
Add Customer
     ↓
View Customer
     ↓
Edit Customer
     ↓
Delete Customer
```

The next development milestone is:

**Customer Search and Pagination**

After that, development can move to the second major CRM entity:

**Contact Management**, where Contacts will be linked to Customers through a Django database relationship.

[⬆ Back to Table of Contents](#table-of-contents)

---
