from django.shortcuts import render_to_response
from accounts.forms import RegistrationForm
from django.template import RequestContext
from django.http import  HttpResponse
from django.contrib.auth.models import User

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.set_password(new_user.password)
            new_user.save()
            return HttpResponse('User created')
    else:
        form = RegistrationForm()
    return render_to_response('registration.html', {'form': form}, context_instance=RequestContext(request))
    
def users(request):
    users = User.objects.all()
    return render_to_response('users.html', {'users': users})
    
def profile(request, user_name):
    user = User.objects.get(username=user_name);
    return HttpResponse('Username: '+user.username+'<br /> Email: '+user.email);
