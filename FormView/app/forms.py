
from django import forms

class EmployeeForm(forms.Form):
    idno = forms.IntegerField(label="IDNO")
    name = forms.CharField(label="NAME")
    salary = forms.DecimalField()
    username = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)