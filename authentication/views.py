from django.http import HttpResponseRedirect
from django.shortcuts import render
from .form import UserForm
from .models import User
from django.urls import reverse

def registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            User.objects.create_user(username=form['username'].data, email=form['email'].data, password=form['password'].data)
            return HttpResponseRedirect(reverse('home:home'))
        else:
            return render(request, 'authentication/registration.html', {'form': form})
    else:
        form = UserForm()
        return render(request, 'authentication/registration.html', {'form': form})

