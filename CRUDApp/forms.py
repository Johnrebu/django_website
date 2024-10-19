
from django import forms
from django.contrib.auth.models import User

from .models import Employee
from django.contrib.auth.forms import UserCreationForm

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"


class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]



