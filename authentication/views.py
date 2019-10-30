from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


def home(request):

    # count number of users
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form,
    })


