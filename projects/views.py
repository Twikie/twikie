from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from projects.models import Project
from projects.models import Revision
from django.http import HttpResponse
from projects.forms import NewProjectForm
from projects.forms import NewRevisionForm

@login_required
def index(request):
    projects = Project.objects.filter(user=request.user)
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
            new_revision = Revision(project=new_project)
            new_revision.save()
            return HttpResponse('Project successfully created, nigga')
    else:
        form = NewProjectForm()
    return render_to_response('new.html', {'form': form, 'type':'project'}, context_instance=RequestContext(request))
    
@login_required
def detail(request, project_id):
    project_details = Project.objects.get(pk=project_id)
    project_revisions = Revision.objects.filter(project=project_id).order_by('-created_at')
    return render_to_response('details.html', {'project': project_details, 'revisions': project_revisions});
    
@login_required
def newrev(request, project_id):
    if request.POST:
        form = NewRevisionForm(request.POST)
        if form.is_valid():
            new_revision = form.save(commit=False)
            new_revision.project = Project.objects.get(pk=project_id)
            new_revision.save()
            return HttpResponse('Revision successfully created')
    else:
        form = NewRevisionForm()
    return render_to_response('new.html', {'form':form, 'type':'revision'}, context_instance=RequestContext(request))
    
    
