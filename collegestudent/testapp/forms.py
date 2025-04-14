from django import forms 
from django.contrib.auth.models import User

class SignUpform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password','first_name','last_name']

class EnrollmentSearchForm(forms.Form):
    enrollment_no = forms.IntegerField(label="Enrollment Number")
