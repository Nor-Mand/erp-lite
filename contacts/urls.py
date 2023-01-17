from django.urls import path
from .views import *

app_name = 'contacts'

urlpatterns = [
    path('industry/', create_industry, name='industry'),
    path('industry/update/<int:pk>', update_industry, name='update-industry'),
    path('industry/delete/<int:pk>', delete_industry, name='delete-industry'),
    path('country/', home_countries, name='country'),
    path('country/update/<int:pk>', update_country, name='update-country'),
    path('country/delete/<int:pk>', delete_country, name='delete-country'),
    path('cities/', home_cities, name='cities'),
    path('cities/update/<int:pk>', update_cities, name='update-cities'),
    path('cities/delete/<int:pk>', delete_cities, name='delete-cities'),
    path('employees/', home_employees, name='employees'),
    path('customers/', home_customers, name='customers'),
    path('customers/new/', create_customers, name='create-customers'),
    path('customers/update/<int:pk>', update_customers, name='update-customers'),
    path('customers/delete/<int:pk>', delete_customers, name='delete-customers'),
    path('suppliers/', home_suppliers, name='suppliers'),
]
