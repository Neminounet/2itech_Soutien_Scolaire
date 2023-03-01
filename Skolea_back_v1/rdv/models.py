from django.db import models
from account.models import Student, Teacher
from degrees_subjects.models import Degree, Subject


class RendezVous(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, verbose_name="Etudiant")
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, verbose_name="Professeur")
    degree = models.ForeignKey(
        Degree, on_delete=models.CASCADE, verbose_name="Classe choisie")
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, verbose_name="Matière choisie")
    time_slot = models.ForeignKey(
        "account.Availablity", on_delete=models.CASCADE, verbose_name="Période choisie")
    price = models.IntegerField(verbose_name="Prix")

    def __str__(self):
        return f"Rendez-vous pour {self.student}, avec {self.teacher} le {self.time_slot} à {self.time_slot.heure}"
