
from django import forms

class EmployeeForm(forms.Form):
    idno = forms.IntegerField()
    name = forms.CharField()
    salary = forms.DecimalField()