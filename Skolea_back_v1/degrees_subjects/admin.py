from django.contrib import admin
from degrees_subjects.models import Degree, Subject, TeacherDegreeSubject


@admin.register(Degree)
class DegreeAdmin(admin.ModelAdmin):
    list_display = ("libelle", "price", )


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("libelle",)


@admin.register(TeacherDegreeSubject)
class TeacherDegreeSubjectAdmin(admin.ModelAdmin):
    list_display = ("teacher", "degree")
