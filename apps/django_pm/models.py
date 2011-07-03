from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    author = models.ForeignKey(User, related_name='author_user')
    recipients = models.ManyToManyField(User)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=500)

    def __unicode__(self):
        return self.title
