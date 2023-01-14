from django.urls import path
from .views import login_user, logout_user

urlpatterns = [
    path('', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
]