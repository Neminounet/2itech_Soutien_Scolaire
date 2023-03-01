from django.urls import path
from workspace.views import WorkspaceHome, SkillsSelectionView, SkillsDelete, DispoSelectionView, DispoDelete

app_name = "workspace"

urlpatterns = [
    path("", WorkspaceHome.as_view(), name="home"),
    path("skills/", SkillsSelectionView.as_view(), name="skills_selector"),
    path("skills/delete/<int:pk>", SkillsDelete.as_view(), name="skills_delete"),
    path("dispo/", DispoSelectionView.as_view(), name="dispo_select"),
    path("dispo/delete/<int:pk>", DispoDelete.as_view(), name="dispo_delete")
]
