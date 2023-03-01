from django.views.generic import TemplateView, CreateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from account.models import Availablity
from degrees_subjects.models import Degree, TeacherDegreeSubject
from degrees_subjects.forms import TeacherDegreeSubjectForm, DispoForm
from django.urls import reverse_lazy


@method_decorator(login_required, name="dispatch")
class WorkspaceHome(TemplateView):
    template_name = "workspace/workspace.html"
    degree = Degree.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            if self.request.user.is_teacher:
                user_id = self.request.user.id
                teacher_degree_subject = TeacherDegreeSubject.objects.filter(
                    teacher_id=user_id)
                disponibilite = Availablity.objects.filter(teacher_id=user_id)
                context['degrees'] = self.degree
                context["teacher_degree_subject"] = teacher_degree_subject
                context["disponibilite"] = disponibilite
                return context


@method_decorator(login_required, name="dispatch")
class SkillsSelectionView(CreateView):
    model = TeacherDegreeSubject
    template_name = "workspace/skills_select.html"
    form_class = TeacherDegreeSubjectForm
    sucess_url = reverse_lazy("workspace/workspace.html")

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            if self.request.user.is_teacher:
                user_id = self.request.user.id
                teacher_degree_subject = form.save(commit=False)
                teacher_degree_subject.teacher_id = user_id
                teacher_degree_subject.save()

                return super().form_valid(form)


@method_decorator(login_required, name="dispatch")
class SkillsDelete(DeleteView):
    model = TeacherDegreeSubject
    template_name = "workspace/skills_delete.html"
    success_url = reverse_lazy("workspace:home")


@method_decorator(login_required, name="dispatch")
class DispoSelectionView(CreateView):
    model = Availablity
    template_name = "workspace/dispo_select.html"
    form_class = DispoForm
    sucess_url = reverse_lazy("workspace/workspace.html")

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            if self.request.user.is_teacher:
                user_id = self.request.user.id
                disponibilite = form.save(commit=False)
                disponibilite.teacher_id = user_id
                disponibilite.save()

                return super().form_valid(form)


@method_decorator(login_required, name="dispatch")
class DispoDelete(DeleteView):
    model = Availablity
    template_name = "workspace/dispo_delete.html"
    success_url = reverse_lazy("workspace:home")
