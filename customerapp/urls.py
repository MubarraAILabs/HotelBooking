from django.urls import path
from . import views

urlpatterns = [
    path("addcustomer/",views.addCustomer, name="addcustomer"),
    path("customers/",views.viewCustomers, name="viewcustomers"),
    path("cupdate/",views.updateCustomer,name="cupdate"),
    path("customers/edit/<str:email>", views.editCustomer, name="edit"),
    path("customers/delete/<str:email>", views.deleteCustomer, name="delete"),
]