from django.contrib import admin
from account.models import CustomUser, Teacher, Student, Availablity, Hour


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name")


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("user",)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("user",)


@admin.register(Hour)
class HourAdmin(admin.ModelAdmin):
    list_display = ("debut", "fin", )


@admin.register(Availablity)
class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ("date", "teacher")
