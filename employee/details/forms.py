from django import forms
from details.models import Employee,EmpAddr

class   EmpForm(forms.ModelForm):
    FirstName=forms.CharField(widget=forms.TextInput(attrs={'Placeholder':'FirstName', 'maxlength':'20', 'Required':'True' }))
    LastName=forms.CharField(widget=forms.TextInput(attrs={'Placeholder':'LastName', 'maxlength':'20', 'Required':'True' }))
    Phone_No=forms.CharField(widget=forms.TextInput(attrs={'Placeholder':'Phone_no', 'maxlength':'20', 'Required':'True'}))
    Email=forms.EmailField(widget=forms.TextInput(attrs={'Placeholder':'Email', 'maxlength':'100', 'Required':'True'}))
    Address1 = forms.CharField(widget=forms.TextInput(attrs={'Placeholder': 'Address1', 'maxlength': '100', 'Required': 'True'}))
    Address2 = forms.CharField(widget=forms.TextInput(attrs={'Placeholder': 'Address2', 'maxlength': '100', 'Required': 'True'}))
    class Meta:
        model = Employee
        fields = ('FirstName', 'LastName', 'Phone_No', 'Email', 'Address1', 'Address2')




    # employee_id = forms.IntegerField()

