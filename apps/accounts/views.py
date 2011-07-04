from django.shortcuts import render
from accounts.forms import RegistrationForm
from django.template import RequestContext
from django.http import  HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from frat.models import Project
from frat.cloud_handlers import create_cloud_container
from django_pm.models import Message

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            password = new_user.password
            new_user.set_password(password)
            create_cloud_container ( new_user.username )
            new_user.save()
            user = authenticate(username=new_user.username, password=password)
            login(request, user)
            return HttpResponseRedirect('/%s' % user.username)
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form}, context_instance=RequestContext(request))
    
def users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})
    
def profile(request, user_name):
    user = User.objects.get(username=user_name);
    projects = Project.objects.filter(owner=user)
    return render(request, 'profile.html', {'owner': user, 'projects': projects} );
    
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')
