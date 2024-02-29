from django.dispatch.dispatcher import receiver
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import conf
from django.db.models import Q
from .models import Profile
from datetime import date, datetime, timedelta
from django.contrib.auth import update_session_auth_hash
from datetime import datetime
from athletes.models import Athlete
from wellness.models import WellnessDaily
from athletes.athletics_functions import *
from training_programme.models import TrainingProgramme

# Create your views here.
def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

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
            return redirect(request.GET['next'] if 'next' in request.GET else 'home')

        else:
            messages.error(request, 'Username OR password is incorrect')

    return render(request, 'users/login.html')

def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out!')
    return redirect('login')


@login_required(login_url='login')
def home(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    try:
        athlete = Athlete.objects.get(profile=profile)
        wellness_registers = WellnessDaily.objects.filter(athlete=athlete.id, registration_date__gte=start_date, registration_date__lte=end_date)
        wellness_7days = get_welness_7days(wellness_registers)
        wellness_graph = wellness(wellness_registers)
        training_programme = TrainingProgramme.objects.filter(athlete=athlete, date=date.today()).first()
    except:
        athlete = None
        wellness_graph=None
        training_programme = None
        wellness_7days = None
    if training_programme is not None:
        warmup = training_programme.warmup.split(';')
    else:
        warmup = ["Sem plano"]
    if training_programme is not None:
        main = training_programme.main.split(';')
    else:
        main = ["Sem plano"]
    if training_programme is not None:
        cooldown = training_programme.cool_down.split(';')
    else:
        cooldown = ["Sem plano"]
    if training_programme is not None:
        obs = training_programme.obs.split(';')
    else:
        obs = ["Sem plano"]
    context = {'wellness_7days': wellness_7days,
               "wellness_data": wellness_graph,
               "training_programme": training_programme,
               "warmup": warmup,
               "main": main,
               "cooldown": cooldown,
               "obs": obs}
    return render(request, 'users/home.html', context)

@login_required(login_url='login')
def editAccount(request, pk):
    profile = Profile.objects.get(user=pk)
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
   
    if request.method == 'POST':
        user = request.user
        profile = Profile.objects.get(user=user)

        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        birth_date_str = request.POST.get('birth_date')
        try:
            birth_date = datetime.strptime(birth_date_str, '%B %d, %Y').strftime('%Y-%m-%d')
        except ValueError:
            birth_date = None
        birth_place = request.POST.get('birth_place')
        nationality = request.POST.get('nationality')
        gender = request.POST.get('gender')
        description = request.POST.get('description')
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_new_password = request.POST.get('confirm_new_password')

        if old_password and new_password and confirm_new_password:
            if user.check_password(old_password):
                if new_password == confirm_new_password:
                    user.set_password(new_password)
                    update_session_auth_hash(request, user)  # Manter a sessão autenticada
                else:
                    messages.error(request, 'A nova senha não coincide com a confirmação de senha.')
                    return redirect('update-profile')  # Redirecionar de volta para a página de atualização
            else:
                messages.error(request, 'A senha antiga não está correta.')
                return redirect('update-profile')  # Redirecionar de volta para a página de atualização

        # Atualizar campos do perfil e do usuário
        user.username = username
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        profile.email = email
        profile.first_name = user.first_name
        profile.last_name = user.last_name
        profile.gender = gender
        profile.birth_date = birth_date
        profile.birth_place = birth_place
        profile.nationality = nationality
        profile.description = description

        user.save()
        profile.save()
        messages.success(request, 'Perfil atualizado com sucesso!')
        return redirect('home')

    context = {'profile': profile,
               'gender_choices': gender_choices,
               'event_group_choices': event_group_choices}
    return render(request, 'users/edit_profile.html', context)


def get_welness_7days(wellness_registers):
    wellness_7days = wellness(wellness_registers)
    weight = round(sum(wellness_7days["weight"])/len(wellness_7days["weight"]),2)
    nutrition = round(sum(wellness_7days["nutrition"])/len(wellness_7days["nutrition"]),2)
    fatigue = round(sum(wellness_7days["fatigue"])/len(wellness_7days["fatigue"]),2)
    sleep_quality = round(sum(wellness_7days["sleep_quality"])/len(wellness_7days["sleep_quality"]),2)
    soreness = round(sum(wellness_7days["soreness"])/len(wellness_7days["soreness"]),2)
    stress = round(sum(wellness_7days["stress"])/len(wellness_7days["stress"]),2)
    hydration = round(sum(wellness_7days["hydration"])/len(wellness_7days["hydration"]),2)
    mood = round(sum(wellness_7days["mood"])/len(wellness_7days["mood"]),2)
    hours_sleep = round(sum(wellness_7days["sleep_hours"])/len(wellness_7days["sleep_hours"]),2)
    return {"weight": weight, "nutrition": nutrition, "fatigue": fatigue, "sleep_quality": sleep_quality, "soreness": soreness, "stress": stress, "hydration": hydration, "mood": mood, "hours_sleep": hours_sleep}

def about(request):
    # Se você quiser passar variáveis para o template, você pode fazê-lo aqui
    context = {
    }

    # Renderize o template com o contexto e retorne a resposta
    return render(request, 'users/about.html', context)