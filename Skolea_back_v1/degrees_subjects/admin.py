from django.contrib import admin
from degrees_subjects.models import Degree, Subject

# admin.site.register(Degree)
# admin.site.register(Subject)


@admin.register(Degree)
class DegreeAdmin(admin.ModelAdmin):
    list_display = ("libelle", "price", )


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("libelle",)
