from .models import Task
from django import forms

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placehholder':'Write a titile.'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Write a description'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input m-auto'},)
        }
