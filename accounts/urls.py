from django.urls import path
from accounts.views import create_user

urlpatterns = [
    path("register", create_user, name="account.register"),
]
