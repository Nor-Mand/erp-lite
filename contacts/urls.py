from django.urls import path
from .views import create_industry, update_industry, delete_industry

app_name = 'contacts'

urlpatterns = [
    path('industry/', create_industry, name='industry'),
    path('industry/update/<int:pk>', update_industry, name='update-industry'),
    path('industry/delete/<int:pk>', delete_industry, name='delete-industry'),
]