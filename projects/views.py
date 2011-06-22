from django.db.models import Q
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from projects.models import Project
from projects.models import Revision
from projects.models import Page
from django.http import HttpResponse
from projects.forms import NewProjectForm
from projects.forms import NewRevisionForm
from projects.forms import NewPageForm


@login_required
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
            new_project.owner = user
            new_project.save()
            form.save_m2m()
            return HttpResponse('Project successfully created, nigga')
    else:
        form = NewProjectForm()
    return render_to_response('new.html', {'form': form, 'type':'project'}, context_instance=RequestContext(request))
    
@login_required
def detail(request, user_name, project_name):
    owner = User.objects.get(username=user_name);
    project = Project.objects.get(owner=owner, name=project_name)
    pages = Page.objects.filter(project=project).order_by('-created_at')

    return render_to_response('project.html', {'project': project, 'pages': pages});
    
@login_required
def newpage(request, project_id):
    if request.POST:
        form = NewPageForm(request.POST)
        if form.is_valid():
            new_page = form.save(commit=False)
            new_page.project = Project.objects.get(pk=project_id)
            new_page.save()
            return HttpResponse('Page successfully created')
    else:
            form = NewPageForm()
    return render_to_response('new.html', {'form':form, 'type':'page'}, context_instance=RequestContext(request))

@login_required
def newrev(request, page_id):
    if request.POST:
        form = NewRevisionForm(request.POST)
        if form.is_valid():
            new_revision = form.save(commit=False)
            new_revision.page = Page.objects.get(pk=page_id)
            new_revision.save()
            return HttpResponse('Revision successfully created')
    else:
        form = NewRevisionForm()
    return render_to_response('new.html', {'form':form, 'type':'revision'}, context_instance=RequestContext(request))

@login_required
def rev(request, project_id, rev_id):
    revision = Revision.objects.get(pk=rev_id)
    return render_to_response('revision.html', {'revision':revision})
    
@login_required
def page(request, project_id, page_id):
    page = Page.objects.get(pk=page_id)
    return render_to_response('page.html', {'page':page})
    
    
