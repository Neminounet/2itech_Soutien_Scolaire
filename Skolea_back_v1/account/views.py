from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from account.models import CustomUser, Student
from account.forms import StudentRegistrationForm


def signupChoice(request):
    return render(request, "account/signup.html")


class StudentCreate(CreateView):
    model = CustomUser
    template_name = "account/signup_student.html"
    status = "Etudiant"
    form_class = StudentRegistrationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["status"] = self.status
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
