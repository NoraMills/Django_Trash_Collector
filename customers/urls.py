from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.create, name="create"),
    path('account_info/', views.customer_account,
         name="customer_account"),
    path('change_pickup/', views.change_pickup,
         name="change_pickup"),
]
