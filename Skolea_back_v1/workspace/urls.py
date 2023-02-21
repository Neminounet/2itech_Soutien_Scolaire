from django.urls import path
from workspace.views import WorkspaceHome

app_name = "workspace"

urlpatterns = [
    path("", WorkspaceHome.as_view(), name="home")
]
