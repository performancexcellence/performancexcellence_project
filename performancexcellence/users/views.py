from django.dispatch.dispatcher import receiver
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import conf
from django.db.models import Q
from .models import Profile

# Create your views here.
def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile': profile}
    return render(request, 'users/user-profile.html', context)

def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'profiles')

        else:
            messages.error(request, 'Username OR password is incorrect')

    return render(request, 'users/login.html')

def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('login')


@login_required(login_url='login')
def editAccount(request, pk):
    profile = Profile.objects.get(id=pk)
    gender_choices = (
        ('m', 'Masculino'),
        ('f', 'Feminino')
    )
    event_group_choices = (
        ('Velocidade', 'Velocidade'),
        ('Saltos', 'Saltos'),
        ('Lançamentos', 'Lançamentos'),
        ('Fundo, Meio Fundo e Marcha', 'Fundo, Meio Fundo e Marcha'),
        ('Provas Combinadas', 'Provas Combinadas')
    )
    if request.method == 'POST':

        return redirect('account')

    context = {'profile': profile,
               'gender_choices': gender_choices,
               'event_group_choices': event_group_choices}
    return render(request, 'users/edit_profile.html', context)