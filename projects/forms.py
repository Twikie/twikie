from django import forms
from projects.models import Project

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ('user')
