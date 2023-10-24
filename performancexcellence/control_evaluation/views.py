from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Strength
from .forms import StrengthForm, SpeedForm


@login_required(login_url='login')
def strength_test_create(request):
    if request.method == 'POST':
        form = StrengthForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            
            mpv_values = [
                form.cleaned_data['mpv1'],
                form.cleaned_data['mpv2'],
                form.cleaned_data['mpv3'],
            ]
            peak_velocity_values = [
                form.cleaned_data['peak_velocity1'],
                form.cleaned_data['peak_velocity2'],
                form.cleaned_data['peak_velocity3'],
            ]
            rom_values = [
                form.cleaned_data['rom1'],
                form.cleaned_data['rom2'],
                form.cleaned_data['rom3'],
            ]
            mean_power_values = [
                form.cleaned_data['mean_power1'],
                form.cleaned_data['mean_power2'],
                form.cleaned_data['mean_power3'],
            ]
            
            # Define esses arrays no modelo
            instance.mpv = mpv_values
            instance.peak_velocity = peak_velocity_values
            instance.rom = rom_values
            instance.mean_power = mean_power_values
            
            instance.save()
            return render(request, 'users/home.html')  # Redireciona para a página de sucesso após a submissão do formulário
    else:
        form = StrengthForm()

    return render(request, 'control_evaluation/strength_test_create.html', {'form': form})


@login_required(login_url='login')
def create_speed(request):
    if request.method == 'POST':
        form = SpeedForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'users/home.html')  # Redireciona para a lista de registros de velocidade
    else:
        form = SpeedForm()
    
    return render(request, 'control_evaluation/create_speed.html', {'form': form})