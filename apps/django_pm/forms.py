from django import forms
from django_pm.models import *

class NewMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ('author', 'reply_to', 'is_unread')
