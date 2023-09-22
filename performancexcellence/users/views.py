from django.dispatch.dispatcher import receiver
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import conf
from django.db.models import Q
from .models import Profile
from django.contrib.auth import update_session_auth_hash
from datetime import datetime

def about(request):
    # Se você quiser passar variáveis para o template, você pode fazê-lo aqui
    context = {
    }
    
    # Renderize o template com o contexto e retorne a resposta
    return render(request, 'users/about.html', context)

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
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/home.html', context)

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
        profile.name = user.first_name
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

