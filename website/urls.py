
from django.urls import path
from .import views
from .views import get_employee_dates

urlpatterns = [

    path('', views.home, name="home"),
    path('get_employee_dates/', get_employee_dates, name='get_employee_dates'),
    path('get_employee_data/', views.get_employee_data, name='get_employee_data'),    
    path('contact.html', views.contact, name="contact"),
    path('about.html', views.about, name="about"),
    path('service.html', views.service, name="service"),
    path('pricing.html', views.pricing, name="pricing"),
    path('appointment.html', views.appointment, name="appointment"),
    path('booknow.html', views.booknow, name="booknow"),
]