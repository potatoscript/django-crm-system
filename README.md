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
