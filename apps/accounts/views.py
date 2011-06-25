from django.shortcuts import render
from accounts.forms import RegistrationForm
from django.template import RequestContext
from django.http import  HttpResponse
from django.contrib.auth.models import User
from frat.models import Project
from frat.cloud_handlers import create_cloud_container

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.set_password(new_user.password)
            create_cloud_container ( new_user.username )
            new_user.save()
            return HttpResponse('User created')
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
