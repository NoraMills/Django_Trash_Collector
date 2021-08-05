from django.http import HttpResponse, request
from django.shortcuts import render
from django.urls import reverse
from .models import Customer
# Create your views here.

# TODO: Create a function for each path created in customers/urls.py. Each will need a template as well.


def index(request):
    # The following line will get the logged-in in user (if there is one) within any view function
    user = request.user

    try:
        # This line inside the 'try' will return the customer record of the logged-in user if one exists
        logged_in_customer = Customer.objects.get(user=user)
    except:
        # TODO: Redirect the user to a 'create' function to finish the registration process if no customer record found
        return render(request, 'customers/create.html')

    # It will be necessary while creating a Customer/Employee to assign request.user as the user foreign key

    print(user)
    return render(request, 'customers/index.html', context={"logged_in_customer": logged_in_customer})


def create(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST.get('name')
        zip_code = request.POST.get('zip_code')
        reg_pickup = request.POST.get('reg_pickup')
        customer = Customer()
        customer.user = user
        customer.name = name
        customer.zip_code = zip_code
        customer.reg_pickup = reg_pickup
        customer.balance = 10
        customer.save()
        return render(request, 'customers/index.html', context={'customer': customer})
    else:
        return render(request, 'customers/create.html')