from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
# from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from account.models import CustomUser
from account.forms import StudentRegistrationForm, TeacherRegistrationForm

# Vue du choix de création de compte étudiant/professeur
# =======================================================


def signupChoice(request):
    return render(request, "account/signup.html")

# Vue Création de profil étudiant
# =================================


class StudentCreate(CreateView):
    model = CustomUser
    template_name = "account/signup_profile.html"
    status = "étudiant"
    form_class = StudentRegistrationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["status"] = self.status
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


# Vue Création de profil professeur
# ====================================

class TeacherCreate(CreateView):
    model = CustomUser
    template_name = "account/signup_profile.html"
    status = "Intervenant"
    form_class = TeacherRegistrationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["status"] = self.status
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


# Vue de login
# ==================================

class LoginView(TemplateView):
    template_name = "account/login.html"

    def post(self, request, **kwargs):
        email = request.POST.get("login-email", False)
        password = request.POST.get("login-password", False)
        user = authenticate(email=email, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect("home")

        return render(request, self.template_name)


# Vue de logout
# =============================

class LogoutView(TemplateView):
    template_name = "home.html"

    def get(self, request, **kwargs):
        logout(request)
        return redirect("home")
