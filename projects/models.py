from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    
    def __unicode__(self):
        return self.name
        
class Revision(models.Model):
    project = models.ForeignKey(Project)
    created_at = models.DateTimeField(auto_now_add = True)

class Annotation(models.Model):
    revision = models.ForeignKey(Revision)
    author = models.ForeignKey(User)
    x = models.IntegerField()
    y = models.IntegerField()
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    
    def __unicode__(self):
        return self.text
