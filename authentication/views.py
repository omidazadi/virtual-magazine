from django.http import HttpResponseRedirect
from django.shortcuts import render
from .form import UserForm
from django.urls import reverse

def registration(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('home:home'))
        else:
            return render(request, 'authentication/registration.html', {'form': form})
    else:
        form = UserForm()
        return render(request, 'authentication/registration.html', {'form': form})

