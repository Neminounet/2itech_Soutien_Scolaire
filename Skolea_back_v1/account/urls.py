from django.contrib import admin
from django.urls import path, include
from account.views import signupChoice, StudentCreate, TeacherCreate, LoginView, LogoutView


app_name = "account"

urlpatterns = [
    path("signup/", signupChoice, name="signup-choice"),
    path("signup/student", StudentCreate.as_view(), name="signup-student"),
    path("signup/teacher", TeacherCreate.as_view(), name="signup-teacher"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout")
]
