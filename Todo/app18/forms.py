from django import forms
from app18.models import Todo

class Task(forms.ModelForm):
    class Meta():
        model=Todo
        fields="__all__"


