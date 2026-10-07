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


## Day 4 — Customer Search and Pagination

82. [Customer Search](#82-customer-search)  
83. [Customer Pagination](#83-customer-pagination)

## Day 5 — Contact Management

84. [Contact Model and Customer Relationship](#84-contact-model-and-customer-relationship)  
85. [Contact Management](#85-contact-management)

## Day 6 — Opportunity and Sales Pipeline Management

86. [Opportunity Model and Customer Relationship](#86-opportunity-model-and-customer-relationship)  
87. [Opportunity Management](#87-opportunity-management)  
88. [Sales Pipeline](#88-sales-pipeline)


## Day 7 — Sales Pipeline Value and Forecast

89. [Sales Pipeline Value and Forecast](#89-sales-pipeline-value-and-forecast)


## Day 8 — Opportunity Search, Stage Filtering and Pagination

90. [Opportunity Search and Stage Filtering](#90-opportunity-search-and-stage-filtering)  
91. [Opportunity Pagination](#91-opportunity-pagination)

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


# Day 4 — Customer Search and Pagination

Day 4 improves the Customer Management module with two features:

- Customer Search
- Customer Pagination

The Customer CRUD functions were completed during Day 3:

```text
Create    ✅
Read      ✅
Update    ✅
Delete    ✅
```

Day 4 extends the Customer List so that it can handle a larger number of Customer records more effectively.

---

# 82. Customer Search

The Customer List page was updated with a search function.

The search can match Customer information from the following fields:

```text
Name
Industry
Email
Phone
Country
```

For example, searching:

```text
Kobe
```

can find a Customer whose name contains:

```text
Kobe Engineering
```

Searching:

```text
Manufacturing
```

can find Customers whose Industry contains:

```text
Manufacturing
```

Searching:

```text
Japan
```

can find Customers whose Country contains:

```text
Japan
```

## Django `Q` Objects

The following import was added to:

```text
crm/views.py
```

```python
from django.db.models import Q
```

Django `Q` objects allow multiple search conditions to be combined.

The CRM search requires:

```text
Name contains query
        OR
Industry contains query
        OR
Email contains query
        OR
Phone contains query
        OR
Country contains query
```

The Customer List view was updated with:

```python
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

    context = {
        "customers": customers,
        "query": query,
    }

    return render(
        request,
        "crm/customer_list.html",
        context
    )
```

The line:

```python
query = request.GET.get("q", "")
```

reads the search value from the browser URL.

For example:

```text
/customers/?q=Kobe
```

contains:

```text
q = Kobe
```

The search process is:

```text
Search Box
     ↓
Kobe
     ↓
GET Request
     ↓
/customers/?q=Kobe
     ↓
request.GET.get("q", "")
     ↓
query = "Kobe"
```

## `icontains`

A search condition such as:

```python
Q(name__icontains=query)
```

means:

```text
name
 ↓
Customer model field

icontains
 ↓
Case-insensitive "contains"

query
 ↓
Search text
```

Therefore a search for:

```text
kobe
```

can match:

```text
Kobe Engineering
KOBE INDUSTRIES
ABC Kobe Manufacturing
```

The `|` operator means:

```text
OR
```

Therefore:

```python
Q(name__icontains=query)
| Q(industry__icontains=query)
| Q(email__icontains=query)
| Q(phone__icontains=query)
| Q(country__icontains=query)
```

searches multiple Customer fields.

## Search Form

The following form was added to:

```text
crm/templates/crm/customer_list.html
```

```django
<form method="get"
      action="{% url 'customer_list' %}"
      class="search-form">

    <input
        type="text"
        name="q"
        value="{{ query }}"
        placeholder="Search customers..."
        class="search-input"
    >

    <button type="submit"
            class="button">
        Search
    </button>

    {% if query %}

        <a href="{% url 'customer_list' %}"
           class="cancel-button">
            Clear
        </a>

    {% endif %}

</form>
```

The important connection is:

```text
HTML
name="q"
     ↓
Browser URL
?q=Japan
     ↓
Django
request.GET.get("q", "")
     ↓
query = "Japan"
```

Search uses a GET request because it retrieves information without modifying the database.

```text
Search Customer    → GET

Add Customer       → POST
Edit Customer      → POST
Delete Customer    → POST
```

The search text is preserved using:

```django
value="{{ query }}"
```

The Clear button returns to:

```text
/customers/
```

and removes the search filter.

If no Customers match the search, Django's:

```django
{% empty %}
```

can display:

```text
No customers found.
```

The completed Search flow is:

```text
Customer List
      ↓
Search Box
      ↓
GET ?q=...
      ↓
customer_list()
      ↓
Q Objects
      ↓
Django ORM
      ↓
SQLite
      ↓
Matching Customers
      ↓
Customer List Template
```

[⬆ Back to Table of Contents](#table-of-contents)

---

# 83. Customer Pagination

Pagination was added so the CRM does not need to display every Customer on one page.

During development, the Customer List is configured to display:

```text
5 Customers per page
```

For example, 12 Customers are divided into:

```text
Page 1 → 5 Customers
Page 2 → 5 Customers
Page 3 → 2 Customers
```

## Django `Paginator`

The following import was added to:

```text
crm/views.py
```

```python
from django.core.paginator import Paginator
```

The final `customer_list()` view combines Search and Pagination:

```python
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
```

This line:

```python
paginator = Paginator(customers, 5)
```

means:

```text
Customer QuerySet
       ↓
Paginator
       ↓
Maximum 5 Customers per page
```

The current page number is read using:

```python
page_number = request.GET.get("page")
```

For:

```text
/customers/?page=2
```

Django receives:

```text
page = 2
```

Then:

```python
page_obj = paginator.get_page(page_number)
```

retrieves the appropriate Customer records for Page 2.

## Pagination Controls

The following controls were added underneath the Customer table:

```django
{% if page_obj.paginator.num_pages > 1 %}

    <div class="pagination">

        {% if page_obj.has_previous %}

            <a href="?q={{ query }}&page={{ page_obj.previous_page_number }}">
                ← Previous
            </a>

        {% endif %}

        <span class="page-info">
            Page {{ page_obj.number }}
            of
            {{ page_obj.paginator.num_pages }}
        </span>

        {% if page_obj.has_next %}

            <a href="?q={{ query }}&page={{ page_obj.next_page_number }}">
                Next →
            </a>

        {% endif %}

    </div>

{% endif %}
```

Django automatically provides:

```text
page_obj.has_previous
page_obj.previous_page_number

page_obj.has_next
page_obj.next_page_number

page_obj.number
page_obj.paginator.num_pages
```

For three pages:

```text
Page 1

Page 1 of 3          Next →


Page 2

← Previous     Page 2 of 3     Next →


Page 3

← Previous     Page 3 of 3
```

## Search and Pagination Together

Search and Pagination were designed to work together.

For example:

```text
/customers/?q=Japan&page=1
```

means:

```text
Search = Japan
Page   = 1
```

Clicking Next preserves the search:

```text
/customers/?q=Japan&page=2
```

This is why the pagination links contain both:

```django
?q={{ query }}&page={{ page_obj.next_page_number }}
```

instead of only:

```django
?page={{ page_obj.next_page_number }}
```

Otherwise the search would disappear when changing pages.

The processing order is:

```text
Customer.objects.all()
        ↓
Search Filter
        ↓
Matching Customers
        ↓
order_by("name")
        ↓
Paginator
        ↓
Current Page
        ↓
customer_list.html
```

For example:

```text
100 Customers
      ↓
Search "Japan"
      ↓
20 Matching Customers
      ↓
5 Customers per page
      ↓
4 Pages
```

The Customer List can now handle:

```text
/customers/
```

All Customers.

```text
/customers/?q=Japan
```

Search results.

```text
/customers/?page=2
```

Page 2.

```text
/customers/?q=Japan&page=2
```

Page 2 of the Japan search results.

## Day 4 Project Status

Customer Management now supports:

```text
Create Customer             ✅
Customer List               ✅
Customer Detail             ✅
Edit Customer               ✅
Delete Customer             ✅
Delete Confirmation         ✅
Customer Search             ✅
Multi-field Search          ✅
No-results Handling         ✅
Customer Pagination         ✅
Search + Pagination         ✅
```

The Customer module now has:

```text
                 CUSTOMER MANAGEMENT

                         Customer
                            │
          ┌─────────────────┼─────────────────┐
          ↓                 ↓                 ↓
        Create             Read             Search
          ✅                ✅                ✅
                            │
                      ┌─────┴─────┐
                      ↓           ↓
                    List        Detail
                      ✅           ✅
                      │
                      ↓
                  Pagination
                      ✅

                            │
                     ┌──────┴──────┐
                     ↓             ↓
                   Update        Delete
                     ✅             ✅
```

The next major development stage is **Contact Management**.

This will introduce the first relationship between CRM models:

```text
Customer
    │
    │ One
    │
    └──────────────┐
                   │
                   │ Many
                   ↓
                Contacts
```

Django's:

```python
ForeignKey
```

will be used to connect each Contact to a Customer.

[⬆ Back to Table of Contents](#table-of-contents)

---

# Day 5 — Contact Management and Customer Relationships

Day 5 expands the CRM beyond Customer Management by introducing **Contacts**.

A Customer represents a company or organization, while a Contact represents a person associated with that Customer.

For example:

```text
ABC Manufacturing
│
├── John Tan
│   ├── Sales Manager
│   ├── john@example.com
│   └── 090-1111-2222
│
├── Yuki Sato
│   ├── Engineering Manager
│   └── yuki@example.com
│
└── Ken Suzuki
    ├── Purchasing Manager
    └── ken@example.com
```

This introduces the first database relationship in the CRM:

```text
Customer
    │
    │ One
    │
    └───────────────┐
                    │ Many
                    ↓
                 Contacts
```

The main Django concept introduced during Day 5 is:

```python
models.ForeignKey
```

This allows each Contact to belong to a Customer while allowing one Customer to have multiple Contacts.

---

# 84. Contact Model and Customer Relationship

## Create the Contact Model

The Contact model was added to:

```text
crm/models.py
```

The model is:

```python
class Contact(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="contacts"
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=150, blank=True)

    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    mobile = models.CharField(max_length=50, blank=True)

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
```

The Contact model contains:

```text
Contact
│
├── customer
├── first_name
├── last_name
├── job_title
├── email
├── phone
├── mobile
├── notes
├── created_at
└── updated_at
```

The most important field is:

```python
customer = models.ForeignKey(
    Customer,
    on_delete=models.CASCADE,
    related_name="contacts"
)
```

This creates the relationship between Customers and Contacts.

---

## Understanding `ForeignKey`

A Django `ForeignKey` represents a many-to-one relationship.

In this CRM:

```text
One Customer
     │
     ├── Contact
     ├── Contact
     ├── Contact
     └── Contact
```

Each Contact belongs to only one Customer:

```text
John Tan
   │
   └── ABC Manufacturing
```

but one Customer can have many Contacts:

```text
ABC Manufacturing
│
├── John Tan
├── Yuki Sato
└── Ken Suzuki
```

In the database, the Contact table contains a reference to the Customer:

```text
crm_contact

id | customer_id | first_name | last_name | job_title
------------------------------------------------------
1  | 1           | John       | Tan       | Manager
2  | 1           | Yuki       | Sato      | Engineer
3  | 2           | Taro       | Yamada    | Manager
```

The:

```text
customer_id
```

column identifies which Customer owns each Contact.

Conceptually:

```text
crm_customer
                       crm_contact

id = 1                 id = 1
ABC Manufacturing  ←── customer_id = 1
                       John Tan

                   ←── id = 2
                       customer_id = 1
                       Yuki Sato


id = 2                 id = 3
Kobe Engineering   ←── customer_id = 2
                       Taro Yamada
```

---

## Understanding `on_delete=models.CASCADE`

The ForeignKey contains:

```python
on_delete=models.CASCADE
```

This determines what happens to Contacts if their Customer is deleted.

For example:

```text
ABC Manufacturing
│
├── John Tan
├── Yuki Sato
└── Ken Suzuki
```

If:

```text
ABC Manufacturing
```

is deleted, Django will also delete its related Contacts:

```text
John Tan
Yuki Sato
Ken Suzuki
```

The relationship therefore behaves as:

```text
Delete Customer
      ↓
Find related Contacts
      ↓
Delete related Contacts
```

For the current CRM implementation, Contacts are considered part of the Customer relationship.

A future production CRM could instead introduce archiving or soft deletion if historical records need to be retained.

---

## Understanding `related_name="contacts"`

The ForeignKey also contains:

```python
related_name="contacts"
```

This creates a convenient reverse relationship.

Starting from a Contact:

```python
contact.customer
```

returns the Contact's Customer.

Starting from a Customer:

```python
customer.contacts.all()
```

returns all Contacts belonging to that Customer.

The relationship therefore works in both directions:

```text
Contact
   │
   │ contact.customer
   ↓
Customer


Customer
   │
   │ customer.contacts.all()
   ↓
Contacts
```

For example:

```python
customer = Customer.objects.get(pk=1)

contacts = customer.contacts.all()
```

can retrieve all Contacts belonging to Customer 1.

---

## Create the Contact Database Table

Because `models.py` was changed, a new migration was required.

The Django model update process remains:

```text
models.py
    ↓
makemigrations
    ↓
Migration File
    ↓
migrate
    ↓
SQLite Database
```

Create the migration:

```powershell
python manage.py makemigrations
```

Django creates a migration similar to:

```text
crm\migrations\0002_contact.py
```

with an operation similar to:

```text
Create model Contact
```

Apply the migration:

```powershell
python manage.py migrate
```

Django then creates the Contact database table in:

```text
db.sqlite3
```

The important development rule remains:

```text
Change Django Model
        ↓
python manage.py makemigrations
        ↓
python manage.py migrate
```

---

## Register Contact in Django Admin

The Contact model was registered in:

```text
crm/admin.py
```

The model import was updated to:

```python
from .models import Contact, Customer
```

The Contact Admin configuration was added:

```python
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
```

The Django Admin now contains:

```text
CRM
│
├── Customers
└── Contacts
```

An important new ORM concept appears here:

```python
"customer__name"
```

The double underscore allows Django to follow the ForeignKey relationship:

```text
Contact
   ↓
customer
   ↓
Customer
   ↓
name
```

This allows Django Admin to search Contacts using the related Customer name.

[⬆ Back to Table of Contents](#table-of-contents)

---

# 85. Contact Management

After creating the Contact database model, the custom CRM interface was extended with Contact Management.

The Contact module now provides:

```text
Contacts
│
├── List
├── Create
├── Detail
├── Update
└── Delete
```

This follows the same CRUD architecture previously created for Customers.

---

## Create `ContactForm`

The existing:

```text
crm/forms.py
```

was updated to import both models:

```python
from django import forms

from .models import Contact, Customer
```

A new `ContactForm` was added:

```python
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
```

Because:

```python
customer
```

is a ForeignKey, Django automatically creates a Customer selection field in the form.

Conceptually:

```text
Customer
[ ABC Manufacturing ▼ ]

First Name
[ John ]

Last Name
[ Tan ]

Job Title
[ Sales Manager ]

Email
[ john@example.com ]
```

The Customer options come from the existing Customer records in the database.

This demonstrates another advantage of Django `ModelForm`:

```text
Django Model
     ↓
ForeignKey
     ↓
ModelForm
     ↓
Customer Dropdown
```

---

## Update the View Imports

The imports in:

```text
crm/views.py
```

were updated to include Contact functionality:

```python
from .forms import ContactForm, CustomerForm
from .models import Contact, Customer
```

The existing Django imports continue to provide functionality such as:

```python
get_object_or_404
redirect
render
```

---

## Contact List

The Contact List view was created:

```python
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
```

Contacts are ordered by:

```text
Last Name
    ↓
First Name
```

The view also introduces:

```python
select_related("customer")
```

Because each Contact belongs to a Customer, the Contact List needs related Customer information such as:

```python
contact.customer.name
```

`select_related()` allows Django to efficiently retrieve the related Customer information together with the Contact records.

Conceptually:

```text
Contact Query
     │
     └── select_related("customer")
                    ↓
            Contact + Customer
                    ↓
               Template
```

---

## Contact List Template

A new template was created:

```text
crm/templates/crm/contact_list.html
```

The Contact table displays:

```text
Name
Customer
Job Title
Email
Phone
```

The main loop is:

```django
{% for contact in contacts %}
```

Contact names link to the Contact Detail page:

```django
<a href="{% url 'contact_detail' contact.pk %}">
    {{ contact.first_name }}
    {{ contact.last_name }}
</a>
```

The related Customer is displayed with:

```django
{{ contact.customer.name }}
```

This demonstrates using the ForeignKey relationship directly from the template:

```text
contact
   ↓
customer
   ↓
name
```

If no Contacts exist, the template displays:

```text
No contacts found.
```

using Django's:

```django
{% empty %}
```

functionality.

---

## Contact Create

The Contact Create view was added:

```python
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
```

The request flow is:

```text
GET /contacts/add/
        ↓
Create empty ContactForm
        ↓
Display Form
        ↓
User enters Contact information
        ↓
POST /contacts/add/
        ↓
ContactForm(request.POST)
        ↓
form.is_valid()
        ↓
form.save()
        ↓
New Contact
        ↓
Redirect to Contact Detail
```

The Customer ForeignKey is selected through the Customer dropdown in the form.

---

## Reusable Contact Form Template

A new template was created:

```text
crm/templates/crm/contact_form.html
```

The same template is used for:

```text
Add Contact
     +
Edit Contact
```

The template determines which operation is being performed using:

```django
{% if contact %}
```

When no existing Contact is supplied:

```text
Add Contact
```

is displayed.

When an existing Contact is supplied:

```text
Edit Contact
```

is displayed.

This follows the same reusable form pattern used for Customer Management.

---

## Contact Detail

The Contact Detail view was created:

```python
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
```

The Contact is retrieved using its primary key:

```text
/contacts/1/
          ↑
          pk
```

`get_object_or_404()` returns the Contact if it exists.

If it does not exist, Django returns:

```text
404 Not Found
```

The Contact Detail page displays information such as:

```text
John Tan

Customer       ABC Manufacturing
Job Title      Sales Manager
Email          john@example.com
Phone          078-123-4567
Mobile         090-1234-5678
Notes          Main sales contact.
Created        ...
Last Updated   ...
```

The Customer name links back to the related Customer Detail page:

```django
<a href="{% url 'customer_detail' contact.customer.pk %}">
    {{ contact.customer.name }}
</a>
```

This creates navigation between the two CRM entities:

```text
Contact Detail
      ↓
Related Customer
      ↓
Customer Detail
```

---

## Edit Contact

The Contact Update view was added:

```python
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
```

The important concept is:

```python
instance=contact
```

Without `instance=contact`, Django would create a new Contact.

With:

```python
instance=contact
```

Django updates the existing record.

The process is:

```text
Existing Contact
       ↓
ContactForm(instance=contact)
       ↓
Existing values displayed
       ↓
User changes information
       ↓
POST
       ↓
ContactForm(
    request.POST,
    instance=contact
)
       ↓
form.save()
       ↓
UPDATE existing Contact
```

---

## Delete Contact

The Contact Delete view was added:

```python
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
```

The delete operation follows the same safety pattern as Customer deletion:

```text
GET
 ↓
Show Confirmation Page

POST
 ↓
Delete Contact
```

The user first sees:

```text
Delete Contact

Are you sure?

You are about to delete:

John Tan

Customer: ABC Manufacturing

This action cannot be undone.

[ Yes, Delete Contact ] [ Cancel ]
```

The actual deletion only occurs after a POST request.

The form therefore contains:

```django
<form method="post">

    {% csrf_token %}

    ...

</form>
```

This prevents simply opening a URL from immediately deleting data.

---

## Contact URL Architecture

The following Contact routes were added to:

```text
crm/urls.py
```

```python
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
```

The CRM now has parallel Customer and Contact URL structures:

```text
CUSTOMERS

/customers/
      ↓
Customer List

/customers/add/
      ↓
Add Customer

/customers/<pk>/
      ↓
Customer Detail

/customers/<pk>/edit/
      ↓
Edit Customer

/customers/<pk>/delete/
      ↓
Delete Customer


CONTACTS

/contacts/
      ↓
Contact List

/contacts/add/
      ↓
Add Contact

/contacts/<pk>/
      ↓
Contact Detail

/contacts/<pk>/edit/
      ↓
Edit Contact

/contacts/<pk>/delete/
      ↓
Delete Contact
```

---

## Connect Contacts to the Sidebar

The Contacts navigation item in:

```text
crm/templates/crm/base.html
```

was connected to:

```django
{% url 'contact_list' %}
```

The CRM sidebar can therefore navigate between:

```text
My CRM

Dashboard
Customers
Contacts
Opportunities
Activities
Reports
```

The Contacts item now opens:

```text
/contacts/
```

---

## Display Contacts on Customer Detail

The Customer Detail page was also extended to display the Contacts belonging to that Customer.

The relationship is accessed using:

```django
customer.contacts.all
```

This is available because the Contact ForeignKey was defined with:

```python
related_name="contacts"
```

The Customer Detail template can therefore use:

```django
{% for contact in customer.contacts.all %}

    ...

{% endfor %}
```

For example:

```text
ABC Manufacturing

Industry: Manufacturing
Country: Japan
Email: abc@abc.com


Contacts

Name          Job Title              Email
---------------------------------------------------
John Tan      Sales Manager          john@example.com
Yuki Sato     Engineering Manager    yuki@example.com
Ken Suzuki    Purchasing Manager     ken@example.com
```

Each Contact name links to its Contact Detail page:

```django
<a href="{% url 'contact_detail' contact.pk %}">
    {{ contact.first_name }}
    {{ contact.last_name }}
</a>
```

The CRM therefore supports navigation in both directions:

```text
Customer Detail
      │
      └── Contacts
             │
             ↓
        Contact Detail
             │
             ↓
       Related Customer
             │
             ↓
       Customer Detail
```

---

## Day 5 Database Relationship

Before Day 5, the main CRM database structure was essentially:

```text
Customer
```

After Day 5:

```text
                 CRM DATABASE

                      │
                      ↓

                   Customer
                      │
                      │ 1
                      │
                      │
                      │ *
                      ↓
                   Contact
```

This represents:

```text
Customer 1 ──────── * Contact
```

or:

```text
One Customer
      ↓
Many Contacts
```

The relationship can be accessed in Python using:

```python
contact.customer
```

from Contact to Customer, and:

```python
customer.contacts.all()
```

from Customer to Contacts.

---

## Day 5 Request Architecture

The Contact module now follows:

```text
                         Browser
                            │
                            ↓
                        crm/urls.py
                            │
          ┌─────────────────┼─────────────────┐
          │                 │                 │
          ↓                 ↓                 ↓
     Contact List      Contact Create    Contact Detail
          │                 │                 │
          └─────────────────┼─────────────────┘
                            │
                            ↓
                         views.py
                            │
                            ↓
                     Django ORM
                            │
              ┌─────────────┴─────────────┐
              ↓                           ↓
           Contact                     Customer
              │                           ↑
              └────── ForeignKey ─────────┘
                            │
                            ↓
                         SQLite
                            │
                            ↓
                       Templates
                            │
                            ↓
                         Browser
```

---

## Day 5 Project Status

The CRM now supports two major business entities:

```text
CRM
│
├── Customers
│   ├── Create               ✅
│   ├── List                 ✅
│   ├── Detail               ✅
│   ├── Edit                 ✅
│   ├── Delete               ✅
│   ├── Search               ✅
│   └── Pagination           ✅
│
└── Contacts
    ├── Customer Relationship ✅
    ├── Create                ✅
    ├── List                  ✅
    ├── Detail                ✅
    ├── Edit                  ✅
    └── Delete                ✅
```

New Django concepts introduced during Day 5:

```text
ForeignKey                       ✅
One-to-Many Relationships        ✅
on_delete=models.CASCADE         ✅
related_name                     ✅
Reverse Relationships            ✅
select_related()                 ✅
Related Model Form Dropdown      ✅
Cross-model Navigation           ✅
```

The most important architectural change is:

```text
Day 1–4

Customer
   │
   └── Independent CRM entity


Day 5

Customer
   │
   ├── Contact
   ├── Contact
   └── Contact
```

The CRM has therefore started moving from basic CRUD screens toward a **relational CRM data model**.

A future development stage can introduce **Opportunity / Sales Pipeline Management**, connecting sales opportunities to Customers and eventually Contacts.

For example:

```text
Customer
   │
   ├── Contacts
   │
   └── Opportunities
          │
          ├── Opportunity Name
          ├── Sales Stage
          ├── Amount
          ├── Probability
          ├── Expected Close Date
          └── Status
```

[⬆ Back to Table of Contents](#table-of-contents)

---

# Day 6 — Opportunity and Sales Pipeline Management

Day 6 expands the CRM with **Opportunity Management** and a basic **Sales Pipeline**.

Customers and Contacts describe **who we do business with**, while Opportunities represent **potential sales or business deals**.

The CRM data structure now becomes:

```text
Customer
│
├── Contacts
│     └── People associated with the customer
│
└── Opportunities
      └── Potential sales / business deals
```

For example:

```text
ABC Manufacturing
│
├── Contacts
│   ├── John Tan
│   └── Yuki Sato
│
└── Opportunities
    ├── New Heat Exchanger Project
    │   ├── Stage: Proposal
    │   ├── Amount: ¥12,000,000
    │   ├── Probability: 60%
    │   └── Expected Close: 2026-12-20
    │
    └── Maintenance Contract
        ├── Stage: Negotiation
        ├── Amount: ¥2,000,000
        └── Probability: 80%
```

Day 6 introduces several new Django concepts:

- Model field `choices`
- `DecimalField`
- `PositiveIntegerField`
- `DateField`
- `get_<field>_display`
- Django Admin `list_filter`
- Sales pipeline calculations using `filter()` and `count()`
- Multiple relationships from Customer
- Dashboard integration with additional models

---

# 86. Opportunity Model and Customer Relationship

## Create the Opportunity Model

A new `Opportunity` model was added to:

```text
crm/models.py
```

The model represents a potential sales deal associated with a Customer.

```python
class Opportunity(models.Model):

    STAGE_CHOICES = [
        ("lead", "Lead"),
        ("qualification", "Qualification"),
        ("proposal", "Proposal"),
        ("negotiation", "Negotiation"),
        ("won", "Closed Won"),
        ("lost", "Closed Lost"),
    ]

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="opportunities"
    )

    name = models.CharField(max_length=200)

    stage = models.CharField(
        max_length=20,
        choices=STAGE_CHOICES,
        default="lead"
    )

    amount = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0
    )

    probability = models.PositiveIntegerField(default=0)

    expected_close_date = models.DateField(
        blank=True,
        null=True
    )

    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
```

The Opportunity model contains:

```text
Opportunity
│
├── customer
├── name
├── stage
├── amount
├── probability
├── expected_close_date
├── description
├── created_at
└── updated_at
```

---

## Opportunity Stage Choices

Opportunity stages are defined using:

```python
STAGE_CHOICES = [
    ("lead", "Lead"),
    ("qualification", "Qualification"),
    ("proposal", "Proposal"),
    ("negotiation", "Negotiation"),
    ("won", "Closed Won"),
    ("lost", "Closed Lost"),
]
```

The `stage` field uses these choices:

```python
stage = models.CharField(
    max_length=20,
    choices=STAGE_CHOICES,
    default="lead"
)
```

Using `choices` prevents inconsistent stage values from being entered manually.

Instead of allowing values such as:

```text
Proposal
proposal
PROPOSAL
Proposing
Waiting for Proposal
```

the application provides predefined stages:

```text
Lead
Qualification
Proposal
Negotiation
Closed Won
Closed Lost
```

Each choice contains two values:

```text
Database Value       Display Value

lead                 Lead
qualification        Qualification
proposal             Proposal
negotiation          Negotiation
won                  Closed Won
lost                 Closed Lost
```

For example, the database can store:

```text
proposal
```

while the user sees:

```text
Proposal
```

---

## Opportunity and Customer Relationship

The Opportunity belongs to a Customer through:

```python
customer = models.ForeignKey(
    Customer,
    on_delete=models.CASCADE,
    related_name="opportunities"
)
```

This creates another one-to-many relationship:

```text
Customer
   │
   │ 1
   │
   └───────────────┐
                   │ *
                   ↓
             Opportunities
```

One Customer can therefore have multiple Opportunities:

```text
ABC Manufacturing
│
├── Heat Exchanger Project
├── Maintenance Contract
└── Plant Upgrade Project
```

Starting from an Opportunity, its Customer can be accessed using:

```python
opportunity.customer
```

Starting from a Customer, all related Opportunities can be retrieved using:

```python
customer.opportunities.all()
```

The Customer model now has two important reverse relationships:

```text
Customer
│
├── customer.contacts.all()
│
└── customer.opportunities.all()
```

This gives the CRM a more realistic relational structure:

```text
                  Customer
                     │
             ┌───────┴────────┐
             │                │
             ↓                ↓
          Contacts       Opportunities
```

---

## Opportunity Amount

Sales value is stored using:

```python
amount = models.DecimalField(
    max_digits=15,
    decimal_places=2,
    default=0
)
```

`DecimalField` is suitable for financial values where decimal precision is important.

Example:

```text
1000000.00
12000000.00
8500000.00
```

The CRM displays the value with the Yen symbol:

```text
¥1000000.00
```

---

## Opportunity Probability

The probability of winning the Opportunity is stored using:

```python
probability = models.PositiveIntegerField(default=0)
```

Example values:

```text
10%
25%
50%
75%
100%
```

At the current stage of the CRM, **Stage and Probability are independent fields**.

For example:

```text
Stage: Qualification
Probability: 25%
```

The user manually enters the probability.

The system does not yet automatically assign a probability based on the selected sales stage.

---

## Expected Close Date

The expected closing date uses:

```python
expected_close_date = models.DateField(
    blank=True,
    null=True
)
```

This stores a date without a time.

For example:

```text
2026-10-31
```

The field is optional because:

```python
blank=True
null=True
```

are enabled.

---

## Create the Opportunity Database Table

After adding the Opportunity model, a new migration was created:

```powershell
python manage.py makemigrations
```

Django generated a migration similar to:

```text
crm/migrations/0003_opportunity.py
```

The migration was then applied:

```powershell
python manage.py migrate
```

The SQLite database now contains the main CRM entities:

```text
db.sqlite3
│
├── crm_customer
├── crm_contact
└── crm_opportunity
```

The standard Django model workflow remains:

```text
Change models.py
       ↓
makemigrations
       ↓
Migration File
       ↓
migrate
       ↓
Database Updated
```

---

## Register Opportunity in Django Admin

The Opportunity model was registered in:

```text
crm/admin.py
```

The model import was updated:

```python
from .models import Contact, Customer, Opportunity
```

The Opportunity Admin configuration was added:

```python
@admin.register(Opportunity)
class OpportunityAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "customer",
        "stage",
        "amount",
        "probability",
        "expected_close_date",
    )

    list_filter = (
        "stage",
    )

    search_fields = (
        "name",
        "customer__name",
        "description",
    )
```

A new Django Admin feature introduced here is:

```python
list_filter = (
    "stage",
)
```

This allows Opportunities to be filtered by:

```text
Lead
Qualification
Proposal
Negotiation
Closed Won
Closed Lost
```

The Django Admin now manages:

```text
CRM
│
├── Customers
├── Contacts
└── Opportunities
```

[⬆ Back to Table of Contents](#table-of-contents)

---

# 87. Opportunity Management

After creating the Opportunity database model, full Opportunity CRUD functionality was added to the custom CRM interface.

The Opportunity module now supports:

```text
Opportunities
│
├── Create
├── List
├── Detail
├── Update
└── Delete
```

---

## Create `OpportunityForm`

The model imports in:

```text
crm/forms.py
```

were updated:

```python
from .models import Contact, Customer, Opportunity
```

The following ModelForm was added:

```python
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
```

Because `stage` uses model choices, Django automatically creates a dropdown containing:

```text
Lead
Qualification
Proposal
Negotiation
Closed Won
Closed Lost
```

Because `customer` is a ForeignKey, Django automatically creates a Customer dropdown.

The form therefore resembles:

```text
Customer
[ Kumamoto Tech ▼ ]

Opportunity Name
[ ABC Opportunity ]

Stage
[ Qualification ▼ ]

Amount
[ 1000000 ]

Probability
[ 25 ]

Expected Close Date
[ 2026-10-31 ]

Description
[ ... ]
```

---

## Date Input Widget

The expected close date uses:

```python
forms.DateInput(
    attrs={
        "type": "date",
    }
)
```

This tells the browser to display a date input control.

Instead of manually typing arbitrary date text, the browser can provide a date selector.

---

## Opportunity List

The Opportunity List view retrieves Opportunities and their related Customers:

```python
opportunities = Opportunity.objects.select_related(
    "customer"
).order_by(
    "-created_at"
)
```

The use of:

```python
select_related("customer")
```

efficiently retrieves the related Customer because each Opportunity contains a ForeignKey to Customer.

The Opportunity table displays:

```text
Opportunity
Customer
Stage
Amount
Probability
Expected Close
```

For example:

```text
Opportunity       Customer        Stage           Amount        Probability
--------------------------------------------------------------------------
ABC Opportunity   Kumamoto Tech   Qualification   ¥1000000.00   25%
```

---

## Display the Stage Name

The database stores values such as:

```text
qualification
proposal
negotiation
won
lost
```

However, the application should display the human-readable value.

Django automatically provides:

```django
{{ opportunity.get_stage_display }}
```

For example:

```text
Database:
qualification

Display:
Qualification
```

Another example:

```text
Database:
won

Display:
Closed Won
```

Django provides this functionality automatically for model fields using `choices`.

---

## Create Opportunity

The Opportunity Create view uses:

```python
OpportunityForm(request.POST)
```

to process submitted data.

The workflow is:

```text
GET /opportunities/add/
        ↓
Create Empty OpportunityForm
        ↓
Display Form
        ↓
User Enters Opportunity
        ↓
POST
        ↓
Validate Form
        ↓
form.save()
        ↓
Opportunity Created
        ↓
Redirect to Opportunity Detail
```

After saving:

```python
opportunity = form.save()
```

the application redirects using the new Opportunity primary key:

```python
return redirect(
    "opportunity_detail",
    pk=opportunity.pk
)
```

---

## Opportunity Detail

Each Opportunity has its own detail page:

```text
/opportunities/<pk>/
```

For example:

```text
/opportunities/1/
```

The page displays:

```text
ABC Opportunity

Customer              Kumamoto Tech
Stage                 Qualification
Amount                ¥1000000.00
Probability           25%
Expected Close Date   Oct. 31, 2026
Description           ...
```

The related Customer name links back to the Customer Detail page:

```django
<a href="{% url 'customer_detail' opportunity.customer.pk %}">
    {{ opportunity.customer.name }}
</a>
```

This creates navigation between the related CRM entities:

```text
Opportunity
     ↓
Customer
     ↓
Customer Detail
```

---

## Edit Opportunity

The Opportunity Update view retrieves the existing Opportunity and passes it into the form:

```python
form = OpportunityForm(
    instance=opportunity
)
```

When the form is submitted:

```python
form = OpportunityForm(
    request.POST,
    instance=opportunity
)
```

The important part is:

```python
instance=opportunity
```

This tells Django:

```text
Update this existing Opportunity
```

instead of:

```text
Create another Opportunity
```

The update flow is:

```text
Existing Opportunity
        ↓
OpportunityForm(instance=opportunity)
        ↓
Display Existing Values
        ↓
User Changes Values
        ↓
POST
        ↓
Validate
        ↓
Save
        ↓
Existing Opportunity Updated
```

---

## Delete Opportunity

Opportunity deletion follows the same safe pattern previously used for Customers and Contacts.

Opening the Delete page performs a:

```text
GET
```

and displays a confirmation page.

The actual deletion requires:

```text
POST
```

The form contains:

```django
{% csrf_token %}
```

The process is:

```text
Opportunity Detail
        ↓
Delete Opportunity
        ↓
Confirmation Page
        ↓
Confirm Delete
        ↓
POST Request
        ↓
opportunity.delete()
        ↓
Redirect to Opportunity List
```

---

## Opportunity URL Architecture

The Opportunity routes were added to:

```text
crm/urls.py
```

```python
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
```

The CRM now has three parallel areas:

```text
CUSTOMERS

/customers/
/customers/add/
/customers/<pk>/
/customers/<pk>/edit/
/customers/<pk>/delete/


CONTACTS

/contacts/
/contacts/add/
/contacts/<pk>/
/contacts/<pk>/edit/
/contacts/<pk>/delete/


OPPORTUNITIES

/opportunities/
/opportunities/add/
/opportunities/<pk>/
/opportunities/<pk>/edit/
/opportunities/<pk>/delete/
```

---

## Display Opportunities on Customer Detail

The Customer Detail page was extended to show Opportunities belonging to the Customer.

Because the Opportunity ForeignKey contains:

```python
related_name="opportunities"
```

the template can use:

```django
customer.opportunities.all
```

For example:

```django
{% for opportunity in customer.opportunities.all %}

    {{ opportunity.name }}
    {{ opportunity.get_stage_display }}
    {{ opportunity.amount }}
    {{ opportunity.probability }}

{% endfor %}
```

The Customer Detail page can therefore show:

```text
Kumamoto Tech

CONTACTS
--------------------------------
John Tan
Yuki Sato


OPPORTUNITIES
---------------------------------------------------------
ABC Opportunity
Qualification
¥1000000.00
25%
Oct. 31, 2026
```

The Customer page is becoming the central location for related CRM information:

```text
                     Customer
                        │
             ┌──────────┴──────────┐
             │                     │
             ↓                     ↓
          Contacts            Opportunities
```

---

## Dashboard Integration

The Dashboard was updated to count:

```python
customer_count = Customer.objects.count()
contact_count = Contact.objects.count()
opportunity_count = Opportunity.objects.count()
```

These values are sent through the context:

```python
context = {
    "customer_count": customer_count,
    "contact_count": contact_count,
    "opportunity_count": opportunity_count,
    "recent_customers": recent_customers,
}
```

The Dashboard can now display actual database counts for:

```text
Customers
Contacts
Opportunities
```

instead of placeholder values.

The Dashboard therefore connects to all three main CRM models:

```text
                 Dashboard
                     │
        ┌────────────┼────────────┐
        ↓            ↓            ↓
    Customers     Contacts    Opportunities
```

[⬆ Back to Table of Contents](#table-of-contents)

---

# 88. Sales Pipeline

Day 6 also introduces the first version of the CRM **Sales Pipeline**.

An Opportunity moves through different stages during the sales process:

```text
Lead
  ↓
Qualification
  ↓
Proposal
  ↓
Negotiation
  ↓
 ┌───────────────┐
 ↓               ↓
Closed Won    Closed Lost
```

These stages correspond directly to the values defined in:

```python
STAGE_CHOICES
```

---

## Pipeline Stage Counts

The Opportunity List view calculates the number of Opportunities in each stage.

For example:

```python
lead_count = opportunities.filter(
    stage="lead"
).count()

qualification_count = opportunities.filter(
    stage="qualification"
).count()

proposal_count = opportunities.filter(
    stage="proposal"
).count()

negotiation_count = opportunities.filter(
    stage="negotiation"
).count()

won_count = opportunities.filter(
    stage="won"
).count()

lost_count = opportunities.filter(
    stage="lost"
).count()
```

The logic is:

```text
All Opportunities
        ↓
Filter by Stage
        ↓
Count Matching Records
        ↓
Display Pipeline Number
```

For example:

```python
opportunities.filter(
    stage="qualification"
).count()
```

means:

```text
Find all Opportunities
        ↓
Keep only Stage = Qualification
        ↓
Count them
```

---

## Send Pipeline Data to the Template

The calculated values are passed to the template through the Django context:

```python
context = {
    "opportunities": opportunities,
    "lead_count": lead_count,
    "qualification_count": qualification_count,
    "proposal_count": proposal_count,
    "negotiation_count": negotiation_count,
    "won_count": won_count,
    "lost_count": lost_count,
}
```

This allows the template to access values such as:

```django
{{ lead_count }}

{{ qualification_count }}

{{ proposal_count }}

{{ negotiation_count }}

{{ won_count }}

{{ lost_count }}
```

---

## Display Pipeline Cards

The Opportunity List page contains a pipeline summary:

```django
<div class="pipeline-summary">

    <div class="pipeline-card">
        <h3>Lead</h3>

        <div class="pipeline-number">
            {{ lead_count }}
        </div>
    </div>

    <div class="pipeline-card">
        <h3>Qualification</h3>

        <div class="pipeline-number">
            {{ qualification_count }}
        </div>
    </div>

    <div class="pipeline-card">
        <h3>Proposal</h3>

        <div class="pipeline-number">
            {{ proposal_count }}
        </div>
    </div>

    <div class="pipeline-card">
        <h3>Negotiation</h3>

        <div class="pipeline-number">
            {{ negotiation_count }}
        </div>
    </div>

    <div class="pipeline-card">
        <h3>Closed Won</h3>

        <div class="pipeline-number">
            {{ won_count }}
        </div>
    </div>

    <div class="pipeline-card">
        <h3>Closed Lost</h3>

        <div class="pipeline-number">
            {{ lost_count }}
        </div>
    </div>

</div>
```

For example, if the database contains one Opportunity:

```text
ABC Opportunity

Stage:
Qualification
```

the pipeline displays:

```text
Lead             0

Qualification    1

Proposal         0

Negotiation      0

Closed Won       0

Closed Lost      0
```

If another Opportunity is moved from:

```text
Qualification
```

to:

```text
Proposal
```

the pipeline counts automatically change based on the database records.

---

## Stage, Pipeline, and Amount

The relationship between Opportunity Stage, Pipeline and Amount is:

```text
                   Opportunity
                        │
             ┌──────────┼──────────┐
             ↓          ↓          ↓
           Stage      Amount   Probability
             │
             ↓
        Sales Pipeline
```

For example:

```text
ABC Opportunity
│
├── Customer: Kumamoto Tech
├── Stage: Qualification
├── Amount: ¥1,000,000
├── Probability: 25%
└── Expected Close: 2026-10-31
```

The Opportunity appears in:

```text
Qualification
```

because its database stage is:

```text
qualification
```

The Amount belongs to the Opportunity itself:

```text
¥1,000,000
```

At the current Day 6 implementation, the pipeline cards show the **number of Opportunities in each stage**.

They do not yet calculate the total sales Amount for each stage.

For example, the current version provides:

```text
Qualification
1
```

rather than:

```text
Qualification
1 Opportunity
¥1,000,000
```

Pipeline value aggregation can be added as a future improvement.

---

## Sales Pipeline CSS

The pipeline layout uses CSS Grid:

```css
.pipeline-summary {
    display: grid;

    grid-template-columns:
        repeat(auto-fit, minmax(140px, 1fr));

    gap: 15px;

    margin: 25px 0;
}
```

Each pipeline stage is displayed using:

```css
.pipeline-card {
    background: white;

    padding: 20px;

    border-radius: 8px;

    border: 1px solid #e5e7eb;

    text-align: center;
}
```

The pipeline count uses:

```css
.pipeline-number {
    font-size: 28px;

    font-weight: bold;

    margin-top: 10px;
}
```

This creates a responsive pipeline summary containing:

```text
Lead | Qualification | Proposal | Negotiation | Closed Won | Closed Lost
```

---

## Day 6 CRM Data Model

After Day 6, the core database relationship is:

```text
                         Customer
                            │
              ┌─────────────┴─────────────┐
              │                           │
              ↓                           ↓
           Contact                   Opportunity
                                          │
                             ┌────────────┼─────────────┐
                             ↓            ↓             ↓
                           Stage        Amount      Probability
                             │
                             ↓
                       Sales Pipeline
```

In database terms:

```text
crm_customer
     │
     ├─────────────── crm_contact
     │
     └─────────────── crm_opportunity
```

Both Contact and Opportunity contain a ForeignKey to Customer.

---

## Day 6 CRM Architecture

The application now contains:

```text
                         My CRM
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ↓                  ↓                  ↓
    Customers           Contacts        Opportunities
        │                  │                  │
        │                  │                  ↓
        │                  │             Sales Pipeline
        │                  │
        └──────────────────┴──────────────────┐
                                              ↓
                                           Dashboard
```

The Opportunity request flow follows the standard Django architecture:

```text
Browser
   ↓
crm/urls.py
   ↓
views.py
   ↓
Django ORM
   ↓
Opportunity Model
   ↓
SQLite
   ↓
Template
   ↓
Browser
```

---

## Day 6 Project Status

The CRM now supports:

```text
CRM
│
├── Dashboard
│   ├── Customer Count            ✅
│   ├── Contact Count             ✅
│   └── Opportunity Count         ✅
│
├── Customers
│   ├── Create                    ✅
│   ├── List                      ✅
│   ├── Detail                    ✅
│   ├── Edit                      ✅
│   ├── Delete                    ✅
│   ├── Search                    ✅
│   └── Pagination                ✅
│
├── Contacts
│   ├── Customer Relationship     ✅
│   ├── Create                    ✅
│   ├── List                      ✅
│   ├── Detail                    ✅
│   ├── Edit                      ✅
│   └── Delete                    ✅
│
└── Opportunities
    ├── Customer Relationship     ✅
    ├── Create                    ✅
    ├── List                      ✅
    ├── Detail                    ✅
    ├── Edit                      ✅
    ├── Delete                    ✅
    ├── Sales Stage               ✅
    ├── Amount                    ✅
    ├── Probability               ✅
    ├── Expected Close Date       ✅
    └── Sales Pipeline            ✅
```

New Django concepts introduced during Day 6:

```text
Model choices                    ✅
DecimalField                     ✅
PositiveIntegerField             ✅
DateField                        ✅
get_<field>_display              ✅
Admin list_filter                ✅
Opportunity ForeignKey           ✅
Reverse Opportunity Relationship ✅
Pipeline Filtering               ✅
Pipeline Counting                ✅
Dashboard Model Counts           ✅
```

The development progression is now:

```text
Day 1
Django Setup + Dashboard
        ↓
Day 2
Customer List + Create
        ↓
Day 3
Customer CRUD
        ↓
Day 4
Customer Search + Pagination
        ↓
Day 5
Contacts + Customer Relationships
        ↓
Day 6
Opportunities + Sales Pipeline
```

The CRM has now moved beyond basic CRUD and contains the beginning of an actual **sales management workflow**.

[⬆ Back to Table of Contents](#table-of-contents)

---

# Day 7 — Sales Pipeline Value and Forecast

Day 7 improves the Sales Pipeline created on Day 6.

Previously, the pipeline displayed only the **number of Opportunities** in each sales stage.

For example:

```text
Lead             0
Qualification    1
Proposal         0
Negotiation      0
Closed Won       0
Closed Lost      0
```

This tells us how many Opportunities exist, but it does not tell us how much those Opportunities are worth.

Day 7 extends the pipeline so that it can also calculate:

- Total Opportunity Amount for each sales stage
- Total Open Pipeline value
- Weighted Sales Forecast

The pipeline can now represent both the **number of deals** and their **financial value**.

For example:

```text
Lead
0
¥0

Qualification
1
¥1,000,000

Proposal
0
¥0

Negotiation
0
¥0

Closed Won
0
¥0

Closed Lost
0
¥0
```

The CRM also calculates:

```text
Open Pipeline
¥1,000,000

Weighted Forecast
¥10,000
```

if the Opportunity has:

```text
Amount:      ¥1,000,000
Probability: 1%
```

---

# 89. Sales Pipeline Value and Forecast

## Pipeline Stage Amounts

The Day 6 Sales Pipeline counted Opportunities using:

```python
qualification_count = opportunities.filter(
    stage="qualification"
).count()
```

This answers:

```text
How many Opportunities are in Qualification?
```

For example:

```text
Qualification
1
```

Day 7 adds financial aggregation so that the CRM can also answer:

```text
What is the total value of Opportunities in Qualification?
```

For example:

```text
Qualification

1 Opportunity
¥1,000,000
```

---

## Import Django `Sum`

The following Django ORM imports are used in:

```text
crm/views.py
```

```python
from django.db.models import (
    DecimalField,
    ExpressionWrapper,
    F,
    Q,
    Sum,
)
```

The new concepts introduced during Day 7 include:

```text
Sum
F
ExpressionWrapper
DecimalField
aggregate()
exclude()
__in
```

`Sum` is used to calculate the total of a database field.

For example:

```python
Sum("amount")
```

means:

```text
Add together the values stored in the amount field.
```

---

## Calculate Amount for Each Pipeline Stage

The CRM calculates the total Opportunity Amount for each sales stage.

For Lead:

```python
lead_amount = opportunities.filter(
    stage="lead"
).aggregate(
    total=Sum("amount")
)["total"] or 0
```

For Qualification:

```python
qualification_amount = opportunities.filter(
    stage="qualification"
).aggregate(
    total=Sum("amount")
)["total"] or 0
```

For Proposal:

```python
proposal_amount = opportunities.filter(
    stage="proposal"
).aggregate(
    total=Sum("amount")
)["total"] or 0
```

For Negotiation:

```python
negotiation_amount = opportunities.filter(
    stage="negotiation"
).aggregate(
    total=Sum("amount")
)["total"] or 0
```

For Closed Won:

```python
won_amount = opportunities.filter(
    stage="won"
).aggregate(
    total=Sum("amount")
)["total"] or 0
```

For Closed Lost:

```python
lost_amount = opportunities.filter(
    stage="lost"
).aggregate(
    total=Sum("amount")
)["total"] or 0
```

The basic calculation process is:

```text
All Opportunities
        ↓
Filter by Stage
        ↓
Select Amount
        ↓
Sum the Amounts
        ↓
Total Stage Value
```

For example:

```text
Proposal Opportunities

Opportunity A     ¥2,000,000
Opportunity B     ¥5,000,000
Opportunity C     ¥3,000,000
                  -----------
Total             ¥10,000,000
```

The ORM performs this using:

```python
.aggregate(
    total=Sum("amount")
)
```

---

## Understanding `aggregate()`

`aggregate()` calculates a value from a collection of database records.

For example:

```python
opportunities.filter(
    stage="proposal"
).aggregate(
    total=Sum("amount")
)
```

can return something conceptually similar to:

```python
{
    "total": 10000000
}
```

The value is retrieved using:

```python
["total"]
```

Therefore:

```python
proposal_amount = opportunities.filter(
    stage="proposal"
).aggregate(
    total=Sum("amount")
)["total"]
```

retrieves the calculated total.

---

## Why `or 0` Is Used

If there are no Opportunities in a particular stage, `Sum()` can return:

```python
None
```

For example:

```text
Closed Lost

No Opportunities
```

could result in:

```python
{
    "total": None
}
```

The code therefore uses:

```python
["total"] or 0
```

For example:

```python
lost_amount = opportunities.filter(
    stage="lost"
).aggregate(
    total=Sum("amount")
)["total"] or 0
```

This changes an empty total from:

```text
None
```

to:

```text
0
```

so the interface can display:

```text
Closed Lost
0
¥0
```

instead of an empty value.

---

## Send Pipeline Amounts to the Template

The calculated amounts are passed from:

```text
crm/views.py
```

to the template through the Django context.

```python
context = {
    "opportunities": opportunities,

    "lead_count": lead_count,
    "qualification_count": qualification_count,
    "proposal_count": proposal_count,
    "negotiation_count": negotiation_count,
    "won_count": won_count,
    "lost_count": lost_count,

    "lead_amount": lead_amount,
    "qualification_amount": qualification_amount,
    "proposal_amount": proposal_amount,
    "negotiation_amount": negotiation_amount,
    "won_amount": won_amount,
    "lost_amount": lost_amount,

    "open_pipeline_amount": open_pipeline_amount,
    "weighted_forecast": weighted_forecast,
}
```

The data flow is:

```text
SQLite
   ↓
Opportunity Model
   ↓
Django ORM
   ↓
filter()
   ↓
aggregate()
   ↓
Sum("amount")
   ↓
views.py
   ↓
context
   ↓
opportunity_list.html
```

---

## Display Amounts on Pipeline Cards

The pipeline cards in:

```text
crm/templates/crm/opportunity_list.html
```

were updated to display both:

```text
Opportunity Count
+
Opportunity Amount
```

For example:

```django
<div class="pipeline-card">

    <h3>Qualification</h3>

    <div class="pipeline-number">
        {{ qualification_count }}
    </div>

    <div class="pipeline-amount">
        ¥{{ qualification_amount }}
    </div>

</div>
```

The complete pipeline now displays information such as:

```text
Lead
0
¥0

Qualification
1
¥1000000.00

Proposal
0
¥0

Negotiation
0
¥0

Closed Won
0
¥0

Closed Lost
0
¥0
```

The relationship is therefore:

```text
Opportunity
     │
     ├── Stage
     │     ↓
     │   Pipeline
     │
     └── Amount
           ↓
      Pipeline Value
```

---

## Pipeline Amount Styling

The pipeline amount was styled in:

```text
crm/templates/crm/base.html
```

using:

```css
.pipeline-amount {
    margin-top: 8px;
    font-size: 14px;
    color: #666;
}
```

The visual structure of each card is now:

```text
┌──────────────────────┐
│    Qualification     │
│                      │
│          1           │
│                      │
│     ¥1000000.00      │
└──────────────────────┘
```

---

## Open Pipeline

The next improvement was calculating the value of all Opportunities that are still active.

The CRM currently has six stages:

```text
Lead
Qualification
Proposal
Negotiation
Closed Won
Closed Lost
```

The first four represent active Opportunities:

```text
Lead
Qualification
Proposal
Negotiation
```

The final two represent completed Opportunities:

```text
Closed Won
Closed Lost
```

Therefore, Open Pipeline should exclude:

```text
Closed Won
Closed Lost
```

This is done using:

```python
open_pipeline = opportunities.exclude(
    stage__in=["won", "lost"]
)
```

---

## Understanding `exclude()`

Django's:

```python
filter()
```

keeps records matching a condition.

For example:

```python
opportunities.filter(
    stage="proposal"
)
```

means:

```text
Keep Proposal Opportunities
```

By comparison:

```python
exclude()
```

removes records matching a condition.

Therefore:

```python
opportunities.exclude(
    stage__in=["won", "lost"]
)
```

means:

```text
All Opportunities
        ↓
Remove Closed Won
        ↓
Remove Closed Lost
        ↓
Open Opportunities
```

---

## Understanding `__in`

The following condition:

```python
stage__in=["won", "lost"]
```

means:

```text
Stage is contained in:

[
    "won",
    "lost"
]
```

In other words:

```text
stage = won
OR
stage = lost
```

Combining it with `exclude()` means:

```text
Exclude Stage = Won
OR
Exclude Stage = Lost
```

leaving:

```text
Lead
Qualification
Proposal
Negotiation
```

---

## Calculate Open Pipeline Amount

After retrieving the open Opportunities:

```python
open_pipeline = opportunities.exclude(
    stage__in=["won", "lost"]
)
```

their Amounts are added together:

```python
open_pipeline_amount = open_pipeline.aggregate(
    total=Sum("amount")
)["total"] or 0
```

For example:

```text
Lead             ¥3,000,000
Qualification    ¥1,000,000
Proposal         ¥10,000,000
Negotiation      ¥5,000,000
                 -----------
Open Pipeline    ¥19,000,000
```

Closed Opportunities are not included:

```text
Closed Won       Excluded
Closed Lost      Excluded
```

The Open Pipeline therefore represents the current potential value of active sales Opportunities.

---

## Weighted Sales Forecast

Day 7 also introduces a basic weighted sales forecast.

An Opportunity's full Amount does not necessarily represent the amount that is likely to be won.

For example:

```text
Opportunity A

Amount:      ¥10,000,000
Probability: 20%
```

has a weighted value of:

```text
¥10,000,000 × 20%

= ¥2,000,000
```

Another Opportunity:

```text
Opportunity B

Amount:      ¥10,000,000
Probability: 80%
```

has a weighted value of:

```text
¥10,000,000 × 80%

= ¥8,000,000
```

Although both Opportunities have the same Amount, Opportunity B contributes more to the weighted forecast because it has a higher probability.

The basic formula is:

```text
Weighted Value
=
Opportunity Amount × Probability ÷ 100
```

---

## Using Django `F()` Expressions

The weighted calculation uses:

```python
F("amount")
```

and:

```python
F("probability")
```

An `F()` expression refers directly to a database field.

Therefore:

```python
F("amount") * F("probability") / 100
```

means:

```text
Current Opportunity Amount
             ×
Current Opportunity Probability
             ÷
            100
```

For example:

```text
Amount:      ¥1,000,000
Probability: 25%
```

becomes:

```text
1,000,000 × 25 ÷ 100

= ¥250,000
```

This calculation can be performed by the database rather than manually retrieving each Opportunity and calculating it in Python.

---

## Using `ExpressionWrapper`

The weighted calculation is defined as:

```python
weighted_expression = ExpressionWrapper(
    F("amount") * F("probability") / 100,
    output_field=DecimalField(
        max_digits=15,
        decimal_places=2
    )
)
```

`ExpressionWrapper` allows Django to understand the result of the database calculation.

The calculation:

```python
F("amount") * F("probability") / 100
```

produces a financial value.

The output type is therefore defined as:

```python
DecimalField(
    max_digits=15,
    decimal_places=2
)
```

Conceptually:

```text
amount
   │
   ├──────────┐
   │          │
   ↓          ↓
¥1,000,000   probability
                25
   │            │
   └─────┬──────┘
         ↓
     Multiply
         ↓
     Divide 100
         ↓
      ¥250,000
```

---

## Calculate the Weighted Forecast

The weighted expression is applied to all Open Pipeline Opportunities:

```python
weighted_forecast = open_pipeline.aggregate(
    total=Sum(weighted_expression)
)["total"] or 0
```

For example:

```text
Opportunity A
¥3,000,000 × 10%
= ¥300,000


Opportunity B
¥1,000,000 × 25%
= ¥250,000


Opportunity C
¥10,000,000 × 50%
= ¥5,000,000


Opportunity D
¥5,000,000 × 75%
= ¥3,750,000
```

The total weighted forecast becomes:

```text
¥300,000
+ ¥250,000
+ ¥5,000,000
+ ¥3,750,000
----------------
¥9,300,000
```

The CRM therefore distinguishes between:

```text
Open Pipeline
¥19,000,000

Weighted Forecast
¥9,300,000
```

The first number represents the full potential value of active Opportunities.

The second number adjusts each Opportunity using its probability.

---

## Display Pipeline Totals

The Open Pipeline and Weighted Forecast are displayed in:

```text
crm/templates/crm/opportunity_list.html
```

using:

```django
<div class="pipeline-totals">

    <div class="summary-card">

        <h3>Open Pipeline</h3>

        <div class="summary-value">
            ¥{{ open_pipeline_amount }}
        </div>

    </div>


    <div class="summary-card">

        <h3>Weighted Forecast</h3>

        <div class="summary-value">
            ¥{{ weighted_forecast }}
        </div>

    </div>

</div>
```

The page structure is now:

```text
Opportunities

┌──────────────┐
│ Lead         │
│ 2            │
│ ¥3,000,000   │
└──────────────┘

┌──────────────┐
│Qualification │
│ 1            │
│ ¥1,000,000   │
└──────────────┘

┌──────────────┐
│ Proposal     │
│ 3            │
│ ¥10,000,000  │
└──────────────┘

...


┌───────────────────────┐
│ Open Pipeline         │
│ ¥19,000,000           │
└───────────────────────┘

┌───────────────────────┐
│ Weighted Forecast     │
│ ¥9,300,000            │
└───────────────────────┘


Opportunity List
------------------------------------------------
...
```

---

## Pipeline Summary Styling

The two summary cards were styled in:

```text
crm/templates/crm/base.html
```

using:

```css
.pipeline-totals {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 15px;
    margin: 20px 0 30px;
}


.summary-card {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 8px;
    padding: 20px;
}


.summary-card h3 {
    margin-top: 0;
    color: #666;
}


.summary-value {
    font-size: 26px;
    font-weight: bold;
}
```

The visual hierarchy is now:

```text
Sales Stages
     ↓
Stage Counts + Stage Amounts
     ↓
Open Pipeline
     ↓
Weighted Forecast
     ↓
Opportunity Table
```

---

## Example — ABC Opportunity

A useful test Opportunity used during development was:

```text
Opportunity:
ABC Opportunity

Customer:
Kumamoto Tech

Stage:
Qualification

Amount:
¥1,000,000

Probability:
1%

Expected Close:
Oct. 31, 2026
```

Because the Stage is:

```text
Qualification
```

the pipeline shows:

```text
Qualification

1

¥1,000,000
```

Because this is not:

```text
Closed Won
```

or:

```text
Closed Lost
```

it is included in the Open Pipeline:

```text
Open Pipeline
¥1,000,000
```

Its weighted value is:

```text
¥1,000,000 × 1 ÷ 100

= ¥10,000
```

Therefore:

```text
Weighted Forecast
¥10,000
```

This test confirms that the relationship between:

```text
Stage
Amount
Probability
```

and:

```text
Pipeline
Open Pipeline
Weighted Forecast
```

is working correctly.

---

## Day 7 Sales Pipeline Architecture

The Opportunity data now flows through several levels of sales analysis:

```text
                     Opportunity
                          │
            ┌─────────────┼─────────────┐
            ↓             ↓             ↓
          Stage         Amount      Probability
            │             │             │
            ↓             ↓             │
       Stage Count   Stage Amount       │
            │             │             │
            └──────┬──────┘             │
                   ↓                    │
             Sales Pipeline             │
                   │                    │
                   ↓                    │
             Open Pipeline ─────────────┘
                   │
                   ↓
           Weighted Forecast
```

The CRM is no longer only storing Opportunity records.

It is beginning to use those records for sales analysis.

---

## Day 7 Project Status

The Opportunity module now supports:

```text
Opportunities
│
├── Customer Relationship          ✅
├── Create                         ✅
├── List                           ✅
├── Detail                         ✅
├── Edit                           ✅
├── Delete                         ✅
├── Sales Stage                    ✅
├── Amount                         ✅
├── Probability                    ✅
├── Expected Close Date            ✅
├── Pipeline Deal Count            ✅
├── Pipeline Stage Amount          ✅
├── Open Pipeline Value            ✅
└── Weighted Sales Forecast        ✅
```

New Django concepts introduced during Day 7:

```text
Sum()                              ✅
aggregate()                        ✅
exclude()                          ✅
__in lookup                        ✅
F() expressions                    ✅
ExpressionWrapper                  ✅
Calculated database expressions    ✅
Financial aggregation              ✅
Weighted forecasting               ✅
```

The development progression is now:

```text
Day 1
Django Setup + Dashboard
        ↓
Day 2
Customer List + Create
        ↓
Day 3
Customer CRUD
        ↓
Day 4
Customer Search + Pagination
        ↓
Day 5
Contacts + Customer Relationships
        ↓
Day 6
Opportunities + Sales Pipeline
        ↓
Day 7
Pipeline Value + Weighted Forecast
```

The next development stage can build on this by adding **Opportunity Search, Stage Filtering, and Pagination**.

[⬆ Back to Table of Contents](#table-of-contents)

---

# Day 8 — Opportunity Search, Stage Filtering and Pagination

Day 8 improves the Opportunity List by making it easier to work with a growing number of sales Opportunities.

The CRM already supported:

```text
Opportunity CRUD
        ↓
Sales Stages
        ↓
Pipeline Counts
        ↓
Pipeline Amounts
        ↓
Open Pipeline
        ↓
Weighted Forecast
```

Day 8 adds:

```text
Opportunity Search
        +
Stage Filtering
        +
Pagination
```

The Opportunity List can now be used more efficiently as the amount of CRM data increases.

For example:

```text
Search: [ ABC                    ]

Stage:  [ Qualification ▼ ]

[ Filter ] [ Clear ]
```

The user can search and filter Opportunities while the Sales Pipeline at the top continues to represent the complete Opportunity database.

---

# 90. Opportunity Search and Stage Filtering

## Read Search and Filter Parameters

The Opportunity List view in:

```text
crm/views.py
```

now reads two GET parameters:

```python
query = request.GET.get("q", "")
stage = request.GET.get("stage", "")
```

The `q` parameter contains the search text.

For example:

```text
/opportunities/?q=ABC
```

produces:

```python
query = "ABC"
```

The `stage` parameter contains the selected Opportunity stage.

For example:

```text
/opportunities/?stage=qualification
```

produces:

```python
stage = "qualification"
```

Both parameters can be used together:

```text
/opportunities/?q=ABC&stage=qualification
```

This represents:

```text
Search:
ABC

Stage:
Qualification
```

---

## Separate Pipeline Data from Table Data

An important architectural improvement was introduced on Day 8.

Previously, the Opportunity List used one QuerySet:

```python
opportunities
```

for everything.

However, search and filtering should affect the Opportunity table without changing the overall Sales Pipeline statistics.

The view therefore starts with:

```python
all_opportunities = Opportunity.objects.select_related(
    "customer"
)

opportunities = all_opportunities
```

These two QuerySets have different responsibilities:

```text
all_opportunities
        │
        ├── Pipeline Counts
        ├── Pipeline Amounts
        ├── Open Pipeline
        └── Weighted Forecast


opportunities
        │
        ├── Search
        ├── Stage Filtering
        ├── Ordering
        ├── Pagination
        └── Opportunity Table
```

This means filtering the table does not incorrectly change the Sales Pipeline summary.

---

## Opportunity Search

Search is applied using Django's `Q` objects:

```python
if query:
    opportunities = opportunities.filter(
        Q(name__icontains=query)
        | Q(customer__name__icontains=query)
        | Q(description__icontains=query)
    )
```

The search covers:

```text
Opportunity Name
Customer Name
Description
```

For example:

```text
Search:
ABC
```

can find:

```text
ABC Opportunity
```

Searching:

```text
Kumamoto
```

can also find an Opportunity belonging to:

```text
Kumamoto Tech
```

even when the word `Kumamoto` does not appear in the Opportunity name.

---

## Understanding `Q`

`Q` objects allow more complex database conditions.

For example:

```python
Q(name__icontains=query)
| Q(customer__name__icontains=query)
| Q(description__icontains=query)
```

The `|` operator means:

```text
OR
```

Therefore the search condition means:

```text
Opportunity Name contains query

OR

Customer Name contains query

OR

Description contains query
```

Conceptually:

```text
                Search Query
                     │
          ┌──────────┼──────────┐
          ↓          ↓          ↓
     Opportunity   Customer   Description
        Name         Name
          │          │          │
          └──────────┼──────────┘
                     ↓
               Matching Records
```

---

## Understanding `icontains`

The lookup:

```python
__icontains
```

performs a case-insensitive partial-text search.

For example:

```python
name__icontains="abc"
```

can match:

```text
ABC Opportunity
abc opportunity
New ABC Project
Project for ABC Manufacturing
```

The user therefore does not need to enter the complete Opportunity name.

---

## Searching Through a ForeignKey

The following lookup:

```python
customer__name__icontains=query
```

searches through the relationship between Opportunity and Customer.

Breaking it down:

```text
customer
    ↓
Follow Opportunity.customer ForeignKey

name
    ↓
Use Customer.name

icontains
    ↓
Perform partial case-insensitive search
```

Therefore:

```python
customer__name__icontains="Kumamoto"
```

can find Opportunities belonging to:

```text
Kumamoto Tech
```

This demonstrates how Django ORM queries can follow relationships between models.

---

## Stage Filtering

The selected sales stage is applied using:

```python
if stage:
    opportunities = opportunities.filter(
        stage=stage
    )
```

For example:

```text
stage = qualification
```

results in:

```python
opportunities.filter(
    stage="qualification"
)
```

Only Qualification Opportunities are displayed in the table.

Available stages are:

```text
Lead
Qualification
Proposal
Negotiation
Closed Won
Closed Lost
```

---

## Search and Stage Filtering Together

Search and filtering are applied sequentially:

```text
All Opportunities
        ↓
Search
        ↓
Stage Filter
        ↓
Order Results
        ↓
Display Results
```

For example:

```text
Search:
ABC

Stage:
Qualification
```

produces:

```text
/opportunities/?q=ABC&stage=qualification
```

The CRM first searches for matching Opportunities and then keeps only records whose stage is:

```text
Qualification
```

This allows multiple conditions to be combined without creating separate pages.

---

## Order Filtered Results

After search and stage filtering, Opportunities are ordered using:

```python
opportunities = opportunities.order_by(
    "-created_at"
)
```

The minus sign:

```text
-
```

means descending order.

Therefore:

```python
"-created_at"
```

means:

```text
Newest Opportunity
        ↓
Older Opportunity
        ↓
Oldest Opportunity
```

---

## Keep Pipeline Calculations Independent

Pipeline calculations now use:

```python
all_opportunities
```

instead of the filtered:

```python
opportunities
```

For example:

```python
lead_count = all_opportunities.filter(
    stage="lead"
).count()

qualification_count = all_opportunities.filter(
    stage="qualification"
).count()

proposal_count = all_opportunities.filter(
    stage="proposal"
).count()

negotiation_count = all_opportunities.filter(
    stage="negotiation"
).count()

won_count = all_opportunities.filter(
    stage="won"
).count()

lost_count = all_opportunities.filter(
    stage="lost"
).count()
```

The same principle is used for Pipeline Amounts:

```python
lead_amount = all_opportunities.filter(
    stage="lead"
).aggregate(
    total=Sum("amount")
)["total"] or 0
```

and the other stages.

The Open Pipeline also uses:

```python
open_pipeline = all_opportunities.exclude(
    stage__in=["won", "lost"]
)
```

This separation is important.

If the user selects:

```text
Stage:
Proposal
```

the Opportunity table shows only Proposal Opportunities.

However, the top Sales Pipeline still displays the complete business pipeline:

```text
Lead
Qualification
Proposal
Negotiation
Closed Won
Closed Lost
```

The architecture is:

```text
                 Opportunity Database
                         │
                         ↓
                 all_opportunities
                         │
              ┌──────────┴──────────┐
              │                     │
              ↓                     ↓
        Sales Analysis        Table QuerySet
              │                     │
        Pipeline Counts            Search
        Pipeline Amounts             ↓
        Open Pipeline          Stage Filter
        Forecast                     ↓
                                 Ordering
                                     ↓
                                   Table
```

---

## Send Search State to the Template

The current search and stage values are passed through the context:

```python
context = {
    "opportunities": opportunities,

    "query": query,
    "stage": stage,

    # other context values...
}
```

This allows the HTML template to remember what the user entered.

For example:

```django
value="{{ query }}"
```

keeps the search text inside the search box.

Likewise:

```django
{% if stage == "qualification" %}selected{% endif %}
```

keeps Qualification selected in the dropdown.

---

## Opportunity Search and Filter Form

The following form was added to:

```text
crm/templates/crm/opportunity_list.html
```

```django
<form method="get"
      action="{% url 'opportunity_list' %}"
      class="opportunity-filter-form">

    <input
        type="text"
        name="q"
        value="{{ query }}"
        placeholder="Search opportunities..."
        class="search-input"
    >


    <select name="stage"
            class="filter-select">

        <option value="">
            All Stages
        </option>

        <option value="lead"
                {% if stage == "lead" %}selected{% endif %}>
            Lead
        </option>

        <option value="qualification"
                {% if stage == "qualification" %}selected{% endif %}>
            Qualification
        </option>

        <option value="proposal"
                {% if stage == "proposal" %}selected{% endif %}>
            Proposal
        </option>

        <option value="negotiation"
                {% if stage == "negotiation" %}selected{% endif %}>
            Negotiation
        </option>

        <option value="won"
                {% if stage == "won" %}selected{% endif %}>
            Closed Won
        </option>

        <option value="lost"
                {% if stage == "lost" %}selected{% endif %}>
            Closed Lost
        </option>

    </select>


    <button type="submit"
            class="button">
        Filter
    </button>


    {% if query or stage %}

        <a href="{% url 'opportunity_list' %}"
           class="cancel-button">
            Clear
        </a>

    {% endif %}

</form>
```

The form uses:

```html
method="get"
```

because searching and filtering do not modify database data.

Instead, they control which data is displayed.

---

## Why Search Uses GET Instead of POST

Creating or editing data normally uses:

```text
POST
```

because the database is being changed.

Searching uses:

```text
GET
```

because the database is not being changed.

For example:

```text
GET

/opportunities/?q=ABC&stage=qualification
```

simply asks:

```text
Show me Opportunities matching these conditions.
```

This also makes search/filter state visible in the URL.

---

## Clear Search and Filter

The Clear link is displayed only when:

```django
{% if query or stage %}
```

is true.

The link points to:

```django
{% url 'opportunity_list' %}
```

without any query parameters.

Therefore:

```text
/opportunities/?q=ABC&stage=qualification
```

becomes:

```text
/opportunities/
```

and the full Opportunity List is displayed again.

---

## Search and Filter Styling

The search/filter area was styled in:

```text
crm/templates/crm/base.html
```

using:

```css
.opportunity-filter-form {
    display: flex;
    align-items: center;
    gap: 10px;
    margin: 25px 0;
}


.filter-select {
    padding: 10px 12px;
    border: 1px solid #ccc;
    border-radius: 6px;
    background: white;
    font-size: 15px;
}
```

The existing Customer Search styling can also be reused for:

```css
.search-input
```

The resulting interface is approximately:

```text
[ Search opportunities... ] [ All Stages ▼ ] [ Filter ] [ Clear ]
```

[⬆ Back to Table of Contents](#table-of-contents)

---

# 91. Opportunity Pagination

As the CRM grows, displaying every Opportunity on one page becomes inefficient.

Day 8 therefore adds pagination to the Opportunity List.

The application displays:

```text
5 Opportunities per page
```

using Django's built-in:

```python
Paginator
```

---

## Import `Paginator`

In:

```text
crm/views.py
```

the following import is used:

```python
from django.core.paginator import Paginator
```

This was already introduced during Customer Pagination on Day 4 and is now reused for Opportunities.

---

## Create the Opportunity Paginator

After search, filtering and ordering:

```python
opportunities = opportunities.order_by(
    "-created_at"
)
```

the QuerySet is passed into:

```python
paginator = Paginator(
    opportunities,
    5
)
```

The number:

```text
5
```

means:

```text
Maximum 5 Opportunities per page
```

For example, if there are 12 matching Opportunities:

```text
Page 1 → Opportunities 1–5

Page 2 → Opportunities 6–10

Page 3 → Opportunities 11–12
```

---

## Read the Requested Page Number

The page number is retrieved from the URL:

```python
page_number = request.GET.get(
    "page"
)
```

For example:

```text
/opportunities/?page=2
```

results in:

```text
page_number = 2
```

---

## Create `page_obj`

The requested page is retrieved using:

```python
page_obj = paginator.get_page(
    page_number
)
```

`page_obj` contains both:

```text
The Opportunities for the current page

and

Pagination information
```

For example, Django can determine:

```text
Current Page
Total Pages
Previous Page
Next Page
Has Previous?
Has Next?
```

---

## Send `page_obj` to the Template

The context was changed from:

```python
"opportunities": opportunities,
```

to:

```python
"opportunities": page_obj,
"page_obj": page_obj,
```

The existing template can therefore continue using:

```django
{% for opportunity in opportunities %}
```

without rewriting the Opportunity table.

At the same time:

```django
page_obj
```

is available for pagination controls.

---

## Pagination Request Flow

The Opportunity List now follows this sequence:

```text
Database
   ↓
All Opportunities
   ↓
Search
   ↓
Stage Filter
   ↓
Ordering
   ↓
Paginator
   ↓
Current Page
   ↓
Template
```

This order is important.

Pagination occurs **after** search and filtering.

For example:

```text
100 Opportunities
        ↓
Search "Project"
        ↓
20 matching Opportunities
        ↓
Stage = Proposal
        ↓
8 matching Opportunities
        ↓
Paginator
        ↓
Page 1 = 5 records
Page 2 = 3 records
```

---

## Pagination Controls

The following pagination controls were added below the Opportunity table:

```django
{% if page_obj.paginator.num_pages > 1 %}

    <div class="pagination">

        {% if page_obj.has_previous %}

            <a href="?q={{ query }}&stage={{ stage }}&page={{ page_obj.previous_page_number }}">
                ← Previous
            </a>

        {% endif %}


        <span class="page-info">

            Page {{ page_obj.number }}
            of {{ page_obj.paginator.num_pages }}

        </span>


        {% if page_obj.has_next %}

            <a href="?q={{ query }}&stage={{ stage }}&page={{ page_obj.next_page_number }}">
                Next →
            </a>

        {% endif %}

    </div>

{% endif %}
```

The controls display only when:

```django
page_obj.paginator.num_pages > 1
```

Therefore, if there are only three Opportunities:

```text
3 records
5 records per page
```

pagination controls are not necessary and remain hidden.

---

## Understanding `has_previous`

This condition:

```django
{% if page_obj.has_previous %}
```

checks whether an earlier page exists.

For example:

```text
Current Page = 1

Previous Page = None
```

so:

```text
← Previous
```

is not displayed.

On Page 2:

```text
Current Page = 2

Previous Page = 1
```

so the Previous link appears.

---

## Understanding `has_next`

This condition:

```django
{% if page_obj.has_next %}
```

checks whether another page exists.

For example:

```text
Page 1 of 3
```

has a next page.

Therefore:

```text
Next →
```

is displayed.

But:

```text
Page 3 of 3
```

has no next page, so the Next link disappears.

---

## Preserve Search During Pagination

An important Day 8 improvement is preserving search parameters when changing pages.

The Next link contains:

```django
?q={{ query }}
```

For example:

```text
Search:
Project
```

followed by clicking:

```text
Next →
```

can produce:

```text
/opportunities/?q=Project&stage=&page=2
```

The search therefore remains:

```text
Project
```

on Page 2.

Without preserving `q`, clicking Next could accidentally return to the unfiltered Opportunity List.

---

## Preserve Stage Filter During Pagination

The pagination URL also contains:

```django
&stage={{ stage }}
```

For example:

```text
Search:
Project

Stage:
Proposal

Page:
2
```

produces a URL similar to:

```text
/opportunities/?q=Project&stage=proposal&page=2
```

All three pieces of application state are preserved:

```text
q
│
└── Search Text


stage
│
└── Sales Stage


page
│
└── Pagination Page
```

---

## Combining Search, Filtering and Pagination

Day 8 demonstrates how several GET parameters can work together.

Example:

```text
/opportunities/?q=Project&stage=proposal&page=2
```

can be understood as:

```text
q=Project
     ↓
Search for Project


stage=proposal
     ↓
Only Proposal Opportunities


page=2
     ↓
Display second page
```

The processing flow becomes:

```text
                   HTTP GET
                      │
                      ↓
           q / stage / page
                      │
                      ↓
              Opportunity ORM
                      │
                Search with Q
                      │
                      ↓
                Stage Filter
                      │
                      ↓
                   Order
                      │
                      ↓
                 Paginator
                      │
                      ↓
                  page_obj
                      │
                      ↓
                   Template
```

---

## Final `opportunity_list()` Architecture

After Day 8, the Opportunity List view performs several different responsibilities in a defined order:

```text
1. Read Search Parameters
          ↓
2. Retrieve All Opportunities
          ↓
3. Create Table QuerySet
          ↓
4. Apply Search
          ↓
5. Apply Stage Filter
          ↓
6. Order Results
          ↓
7. Paginate Results
          ↓
8. Calculate Pipeline Counts
          ↓
9. Calculate Pipeline Amounts
          ↓
10. Calculate Open Pipeline
          ↓
11. Calculate Weighted Forecast
          ↓
12. Build Context
          ↓
13. Render Template
```

Two logical data paths now exist:

```text
                      Opportunity
                          │
                          ↓
                  all_opportunities
                          │
              ┌───────────┴───────────┐
              │                       │
              ↓                       ↓
        SALES ANALYSIS            TABLE DATA
              │                       │
        Stage Counts                Search
        Stage Amounts                 ↓
        Open Pipeline            Stage Filter
        Weighted Forecast             ↓
                                  Ordering
                                      ↓
                                  Pagination
                                      ↓
                                  page_obj
                                      ↓
                                    Table
```

This separation prevents user interface filters from accidentally changing overall pipeline statistics.

---

## Day 8 Opportunity Module Status

The Opportunity module now supports:

```text
Opportunities
│
├── Customer Relationship          ✅
├── Create                         ✅
├── List                           ✅
├── Detail                         ✅
├── Edit                           ✅
├── Delete                         ✅
│
├── Sales Management
│   ├── Sales Stage                ✅
│   ├── Amount                     ✅
│   ├── Probability                ✅
│   └── Expected Close Date        ✅
│
├── Pipeline Analysis
│   ├── Stage Counts               ✅
│   ├── Stage Amounts              ✅
│   ├── Open Pipeline              ✅
│   └── Weighted Forecast          ✅
│
└── Opportunity List Tools
    ├── Search by Opportunity      ✅
    ├── Search by Customer         ✅
    ├── Search by Description      ✅
    ├── Stage Filtering            ✅
    ├── Combined Search + Filter   ✅
    ├── Pagination                 ✅
    └── Preserve Filters by Page   ✅
```

---

## Django Concepts Reinforced on Day 8

Day 8 reused and combined several Django concepts:

```text
request.GET                     ✅
Q objects                       ✅
icontains                       ✅
ForeignKey relationship lookup  ✅
filter()                        ✅
order_by()                      ✅
select_related()                ✅
Paginator                       ✅
page_obj                        ✅
Template conditions             ✅
GET query parameters            ✅
```

The important new architectural concept was separating:

```text
Global analytical data
```

from:

```text
User-filtered table data
```

using:

```python
all_opportunities
```

and:

```python
opportunities
```

respectively.

---

## Development Progress

The CRM development progression is now:

```text
Day 1
Django Setup + Dashboard
        ↓
Day 2
Customer List + Create
        ↓
Day 3
Customer CRUD
        ↓
Day 4
Customer Search + Pagination
        ↓
Day 5
Contacts + Customer Relationships
        ↓
Day 6
Opportunities + Sales Pipeline
        ↓
Day 7
Pipeline Value + Weighted Forecast
        ↓
Day 8
Opportunity Search
+ Stage Filtering
+ Pagination
```

The Opportunity module has now progressed from basic CRUD into a much more practical sales-management interface.

[⬆ Back to Table of Contents](#table-of-contents)

---
