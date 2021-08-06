from customers.models import Customer
from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.apps import apps
from .models import Employee
from customers.models import Customer
from datetime import date, datetime

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.


def index(request):
    user = request.user
    try:
        logged_in_employee = Employee.objects.get(user=user)
    except:
        return render(request, 'employees/create.html')

    # It will be necessary while creating a Customer/Employee to assign request.user as the user foreign key
    # Customer = apps.get_model('customers.Customer')
    Customers = Customer.objects.all()
    now = datetime.now()
    today = now.strftime('%a')
    date = datetime.today().strftime('%Y-%m-%d')

    return render(request, 'employees/index.html', context={'logged_in_employee': logged_in_employee, 'Customers': Customers, 'now': now, 'today': today, 'date': date})


def create(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST.get('name')
        zipcode = request.POST.get('zipcode')
        employee = Employee()
        employee.user = user
        employee.name = name
        employee.zipcode = zipcode
        employee.save()
        return render(request, 'employees/index.html', context={'employee': employee})
    else:
        return render(request, 'employees/create.html')
