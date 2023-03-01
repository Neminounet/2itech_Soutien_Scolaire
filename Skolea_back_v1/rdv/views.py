from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from degrees_subjects.models import Degree, Subject, TeacherDegreeSubject


@method_decorator(login_required, name="dispatch")
class CreateRDV(TemplateView):
    template_name = "rdv/create_rdv.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Afficher la liste des classes et des matières
        context["student"] = self.request.user
        context['degrees'] = Degree.objects.all()
        context['subjects'] = Subject.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        student = self.request.user.student
        degree_id = request.POST.get('degree-select')
        subject_id = request.POST.get('subject-select')
        print(student.user.first_name)

        try:
            # ATTENTION ici pour obtenir le subject_id attaché au TeacherDegreeSubject.id il faut faire subject__id=(il y a deux_ _)
            teacher_degree_subject = TeacherDegreeSubject.objects.filter(
                degree_id=degree_id, subject__id=subject_id)
            print(f"YEAH voici ton/tes prof => {teacher_degree_subject}")
        except TeacherDegreeSubject.DoesNotExist:
            messages.error(
                request, "Aucun enseignant compétent trouvé pour cette classe et cette matière.")
            return redirect('workspace:home')

        return redirect('workspace:home')
