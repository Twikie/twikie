from django import forms

from projects.models import *

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ('owner')

class NewRevisionForm(forms.ModelForm):
    class Meta:
        model = Revision
        exclude = ('page')
        
class NewPageForm(forms.ModelForm):
    class Meta:
        model = Page
        exclude = ('project')
