from django import forms
from django_pm.models import *

class NewMessageForm(forms.ModelForm):
    class Meta:
        model = Message
