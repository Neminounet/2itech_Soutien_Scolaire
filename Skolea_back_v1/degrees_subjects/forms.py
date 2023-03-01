from django.forms import ModelForm, CheckboxSelectMultiple, DateField, SelectDateWidget
from degrees_subjects.models import TeacherDegreeSubject
from account.models import Availablity


class TeacherDegreeSubjectForm(ModelForm):
    class Meta:
        model = TeacherDegreeSubject
        fields = ["degree", 'subject']
        widget = {
            'subject': CheckboxSelectMultiple
        }


class DispoForm(ModelForm):
    date = DateField(widget=SelectDateWidget(years=range(2020, 2040)))

    class Meta:
        model = Availablity
        fields = ["date", 'heure']
        widget = {
            'heure': CheckboxSelectMultiple,
        }
