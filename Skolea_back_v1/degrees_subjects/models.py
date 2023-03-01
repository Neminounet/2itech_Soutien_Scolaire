from django.db import models
from django.urls import reverse


class Subject(models.Model):
    libelle = models.CharField(max_length=255, blank=False, null=False)

    class Meta:
        verbose_name = "Matière"

    def __str__(self):
        return self.libelle


class Degree(models.Model):
    libelle = models.CharField(max_length=255, blank=False, null=False)
    # subject = models.ManyToManyField(Subject)
    price = models.IntegerField(blank=False, null=False)

    class Meta:
        verbose_name = "Classe"

    def __str__(self):
        return self.libelle


class TeacherDegreeSubject(models.Model):
    teacher = models.ForeignKey(
        "account.Teacher", on_delete=models.SET_NULL, null=True)
    degree = models.ForeignKey(
        "degrees_subjects.Degree", on_delete=models.SET_NULL, null=True)
    subject = models.ManyToManyField(Subject)

    def get_absolute_url(self):
        return reverse('workspace:home')
