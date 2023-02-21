from account.models import CustomUser, Student, Teacher
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction


# Formulaire de création du profil étudiant :
# =============================================

class StudentRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email", "first_name", "last_name",)

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        return user


# Formulaire de création du profil Intervenant:
# ==============================================

class TeacherRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email", "first_name", "last_name",)

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()
        teacher = Teacher.objects.create(user=user)
        return user
