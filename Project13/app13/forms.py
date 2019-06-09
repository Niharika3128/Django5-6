from django import forms

class EmployeeForm(forms.Form):
    idno = forms.IntegerField(label="IDNO",help_text="Enter Number only")
    name = forms.CharField(label="NAME",help_text="Use a to z and A to Z")
    salary = forms.DecimalField(label="SALARY",help_text="Use Decimal")
    