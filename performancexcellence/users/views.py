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
        ('M', 'Masculino'),
        ('F', 'Feminino')
    )
    event_group_choices = (
        ('Speed', 'Velocidade'),
        ('Jumps', 'Saltos'),
        ('Throws', 'Lançamentos'),
        ('Long distance, Middle Distance e Racewalking', 'Fundo, Meio Fundo e Marcha'),
        ('Combined Events', 'Provas Combinadas')
    )
    athletics_events = (
        # Corridas
        ("100m", "100m"),
        ("200m", "200m"),
        ("400m", "400m"),
        ("800m", "800m"),
        ("1500m", "1500m"),
        ("3000m", "3000m"),
        ("5000m", "5000m"),
        ("10000m", "10000m"),
        ("Half Marathon", "Half Marathon"),
        ("Marathon", "Marathon"),
        # Barreiras
        ("100m Hurdles", "100m Hurdles"),
        ("110m Hurdles", "110m Hurdles"),
        ("400m Hurdles", "400m Hurdles"),
        # Corrida com obstáculos
        ("2000m Steeplechase", "2000m Steeplechase"),
        ("3000m Steeplechase", "3000m Steeplechase"),
        # Revezamentos
        ("4x100m Relay", "4x100m Relay"),
        ("4x400m Relay", "4x400m Relay"),
        # Saltos
        ("High Jump", "High Jump"),
        ("Long Jump", "Long Jump"),
        ("Triple Jump", "Triple Jump"),
        ("Pole Vault", "Pole Vault"),
        # Arremessos e Lançamentos
        ("Shot Put", "Shot Put"),
        ("Discus Throw", "Discus Throw"),
        ("Hammer Throw", "Hammer Throw"),
        ("Javelin Throw", "Javelin Throw"),
        # Provas combinadas
        ("Decathlon", "Decathlon"), # Homens
        ("Heptathlon", "Heptathlon"), # Mulheres
        # Categorias específicas para atletas mais jovens
        ("60m", "60m"),
        ("60m Hurdles", "60m Hurdles"),
        ("300m", "300m"),
        ("300m Hurdles", "300m Hurdles"),
        ("1000m", "1000m"),
        ("Octathlon", "Octathlon"),
        ("Triathlon", "Triathlon"),
    )
    if request.method == 'POST':

        return redirect('account')

    context = {'profile': profile,
               'gender_choices': gender_choices,
               'event_group_choices': event_group_choices,
               "athletics_events": athletics_events}
    return render(request, 'users/edit_profile.html', context)