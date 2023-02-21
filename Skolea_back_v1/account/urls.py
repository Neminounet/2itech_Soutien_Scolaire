from django.urls import path
from account.views import SignupProfile, StudentCreate, TeacherCreate, Login, Logout, ResetPassword, ResetPasswordDone, ResetPasswordConfirm, ResetPasswordComplete

app_name = "account"

urlpatterns = [
    path("signup/", SignupProfile.as_view(), name="signup-choice"),
    path("signup/student", StudentCreate.as_view(), name="signup-student"),
    path("signup/teacher", TeacherCreate.as_view(), name="signup-teacher"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path("password_reset/", ResetPassword.as_view(), name="password_reset"),
    path('password_reset/done/', ResetPasswordDone.as_view(),
         name="password_reset_done"),
    path("reset/<uidb64>/<token>/", ResetPasswordConfirm.as_view(),
         name="password_reset_confirm"),
    path("reset/complete/", ResetPasswordComplete.as_view(),
         name="password_reset_complete")
]
