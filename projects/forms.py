from django import forms
from projects.models import Project
from projects.models import Revision

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ('user')

class NewRevisionForm(forms.ModelForm):
    class Meta:
        model = Revision
