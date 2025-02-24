from django.urls import path
from . import views

urlpatterns = [
    path('register',views.registrationform,name='registerform'),
    path('login',views.loginform,name='loginform'),
    path('display',views.displaydetailes,name='displaydata'),
    path('update',views. updatedetailes,name='update_detailes'),
    path('delete',views.deletedetails,name='deletedata'),
    path('booking',views.booking,name='booking'),
    path('booking_delete',views. deletebooking,name='booking delete'),
    path('search',views.search_view,name='search view'),
    path('logout',views.logout,name='logout'),
]