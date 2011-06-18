from django.db import models
from django.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, unique=True)

    def __unicode__(self):
        return self.user.username
