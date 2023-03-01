from django.db import models
from django.urls import reverse
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from degrees_subjects.models import Degree


class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, **kwargs):
        if not email:
            raise ValueError("Vous devez entrer une adresse email valide")
        else:
            user = self.model(
                email=self.normalize_email(email),
                first_name=first_name,
                last_name=last_name
            )
            user.set_password(password)
            user.save()
            return user

    def create_superuser(self, email, first_name, last_name, password=None, **kwargs):
        user = self.create_user(email=email, password=password,
                                first_name=first_name, last_name=last_name)
        user.is_admin = True
        user.is_staff = True
        user.is_teacher = True
        user.save()
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(
        unique=True, max_length=255, blank=False, verbose_name="Adresse Email")
    first_name = models.CharField(
        blank=False, max_length=255, default="", verbose_name="Prénom")
    last_name = models.CharField(
        blank=False, max_length=255, default="", verbose_name="Nom de famille")
    telephone = models.CharField(max_length=10, blank=True, null=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]
    objects = MyUserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Student(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, primary_key=True)
    age = models.IntegerField(blank=True, null=True)
    classe = models.ForeignKey(
        Degree, on_delete=models.SET_NULL, null=True, blank=True)


class Teacher(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, primary_key=True)

    @property
    def get_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def __str__(self):
        template = self.get_name
        return template


class Hour(models.Model):
    debut = models.TimeField(null=True, blank=True)
    fin = models.TimeField()
    taken = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.debut}"


class Availablity(models.Model):
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    heure = models.ManyToManyField(Hour)

    def __str__(self):
        return f"{self.date}"

    def get_absolute_url(self):
        return reverse('workspace:home')

# class RDV(models.Model):
#     teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)
#     student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
