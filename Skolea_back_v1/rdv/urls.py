from django.urls import path, include
from rdv.views import CreateRDV

app_name = "rdv"

urlpatterns = [
    path("create/", CreateRDV.as_view(), name="create"),
]
