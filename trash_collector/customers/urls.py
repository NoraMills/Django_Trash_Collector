from django.urls import path

from . import views

# TODO: Determine what distinct pages are required for the customer user stories, add a path for each in urlpatterns

app_name = "customers"
urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.create, name="create"),
    path('change_pickup/', views.change_pickup, name="change_pickup"),
    path('account_info/', views.account_info, name="account_info"),
    path('suspend_account/', views.suspend_account, name="suspend_account"),
    path('onetime_pickup', views.onetime_pickup, name="onetime_pickup"),
]
