from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    author = models.ForeignKey(User, related_name='author_user')
    recipients = models.ManyToManyField(User, through='MessageManager')
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=500)
    sent_at = models.DateTimeField(auto_now_add = True)
    reply_to = models.ForeignKey('self', null=True)
    def __unicode__(self):
        return self.title
        
class MessageManager(models.Model):
    message = models.ForeignKey(Message)
    recipient = models.ForeignKey(User)
    is_read = models.BooleanField(default=False)
