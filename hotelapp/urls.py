from django.urls import path
from . import views

urlpatterns = [
    path("we/",views.saveHotels),
]