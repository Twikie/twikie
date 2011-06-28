from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    author = models.ForeignKey(User, related_name='author_user')
    recievers = models.ManyToManyField(User, through='Reciever')
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=500)

    def __unicode__(self):
        return self.title

class Reciever(models.Model):
    reciever = models.ForeignKey(User, related_name='reciever_user')
    message = models.ForeignKey(Message)
