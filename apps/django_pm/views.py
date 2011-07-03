from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django_pm.models import *
from django_pm.forms import *

@login_required
def index(request):
    user = request.user
    messages = Message.objects.filter(recipients=user)

    return render(request, 'inbox.html', {'messages': messages})

@login_required
def newmessage(request):
    user = request.user
    if request.POST:
        form = NewMessageForm(request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.author = user
            new_message.save()
            form.save_m2m()
            return HttpResponse('Message Sent')
    else:
        form = NewMessageForm()

    return render(request, 'new.html', {'form': form, 'type': 'message'})

@login_required
def message(request, message_id):
    user = request.user
    message = Message.objects.get(id=message_id)
    return render(request, 'message.html', {'message': message})
