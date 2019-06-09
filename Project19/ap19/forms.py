
from django import forms
from .models import EmployeeModel


# class EmployeeForm(forms.Form):
#     idno = forms.IntegerField()
#     name = forms.CharField()
#     email = forms.EmailField()


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeModel
        fields = ["idno","name","email"]
