from django import forms

class EmployeeForm(forms.Form):
    idno = forms.IntegerField(label="IDNO")
    name = forms.CharField(label="NAME")
    salary = forms.DecimalField(label="SALARY",help_text="Enter Salary in Decimal")
    items = (
        ("manager","MANAGER"),
        ("developer","DEVELOPER"),
        ("tester","TESTER"),
    )
    desig = forms.ChoiceField(label="DESIGNATION",choices=items)
    doj = forms.DateField(widget=forms.SelectDateWidget,label="DATE OF JOIN")
    email = forms.EmailField(label="EMAIL")
    image = forms.FileField(label="PHOTO")
    password = forms.CharField(label="PASSWORD",widget=forms.PasswordInput)
    lang1 = forms.BooleanField(label="C-Lang")
    lang2 = forms.BooleanField(label="C++")
    lang3 = forms.BooleanField(label="Python")

    items1 = (
        ("one","Yes"),
        ("two","Maybe"),
        ("three","No"),
    )
    status = forms.ChoiceField(label="Are you Attending",choices=items1,widget=forms.RadioSelect)
    status1 = forms.MultipleChoiceField(label="Are you Attending",choices=items1)
    

