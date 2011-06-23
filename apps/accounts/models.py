from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User, unique=True)
    url = models.URLField(blank=True)
    company = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=100, blank=True)
    is_hireable = models.BooleanField(default=False)

    def __unicode__(self):
        return self.user.username
