from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    owner = models.ForeignKey(User)
    members = models.ManyToManyField(User, related_name="Project")
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    class Meta:
        unique_together = ("owner", "name")
    def __unicode__(self):
        return self.name
        
class Page(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project)
    created_at = models.DateTimeField(auto_now_add = True)
    class Meta:
        unique_together = ("project", "name")
        
class Revision(models.Model):
    page = models.ForeignKey(Page)
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
