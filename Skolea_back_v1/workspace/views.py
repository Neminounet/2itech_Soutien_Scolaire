from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from degrees_subjects.models import Degree


@method_decorator(login_required, name="dispatch")
class WorkspaceHome(TemplateView):
    template_name = "workspace/workspace.html"
    degree = Degree.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['degrees'] = self.degree
        return context
