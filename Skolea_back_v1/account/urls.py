from django.contrib import admin
from django.urls import path
from account.views import signupChoice, StudentCreate

app_name = "account"

urlpatterns = [
    path("signup/", signupChoice, name="signup-choice"),
    path("signup/student", StudentCreate.as_view(), name="signup-student")
]
