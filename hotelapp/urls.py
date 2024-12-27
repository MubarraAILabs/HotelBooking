from django.urls import path
from . import views

urlpatterns = [
    path("add/",views.saveHotels),
    path("lst/",views.showHotels),
    path("update/",views.updateHotels,name="update"),
    path("lst/delete/<int:id>",views.deleteHotels,name="delete"),
    path("lst/edit/<int:id>",views.editHotels,name="edit"),
]