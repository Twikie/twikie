from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from projects.models import Project
from django.http import HttpResponse
from projects.forms import NewProjectForm

def index(request):
    projects = Project.objects.all()
    return render_to_response('index.html', {'projects': projects})

@login_required
def new(request):
    user = request.user
    if request.POST:
        form = NewProjectForm(request.POST)
        if form.is_valid():
            new_project = form.save(commit=False)
            new_project.user = user
            new_project.save()
            return HttpResponse('Project successfully created, nigga')
    else:
        form = NewProjectForm()
    return render_to_response('new.html', {'form': form})
