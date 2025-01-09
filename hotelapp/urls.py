from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.addhotel, name="add_hotel"),
    path("view/", views.viewhotels, name="view"),
    path("update/",views.updateHotel,name="update"),
    path("view/edit/<int:id>", views.editHotel, name="edit"),
    path("view/delete/<int:id>", views.deleteHotel),
    path("view/category/<int:id>",views.addcategory, name="add_category"),
    path("category_list", views.category_list, name='category_list'),
    path("view/category_list/<int:id>", views.category_list, name='category_list'),
    path("update_category/<int:id>", views.update_category),
    path("delete_category/<int:id>", views.delete_category),
    path("book_room/<int:id>",views.create_booking, name='book_room'),
    path("create/",views.create_booking, name='create_booking'),
    path("view/", views.viewhotels, name="view"),
    path('home/',views.index, name='home'),
    path('viewbooking/',views.showBookings, name='viewbooking'),
    path('booking_table/', views.booking_table, name='booking_table'),
    path('booking_confirm_list/', views.confirm_bookings, name='booking_confirm_list'), 


]
