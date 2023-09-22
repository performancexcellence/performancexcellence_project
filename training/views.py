from django.shortcuts import render, redirect
from django.contrib import messages
from .models import StrengthTraining
from .forms import StrengthTrainingForm, JumpsTrainingForm

def create_strength_training(request):
    if request.method == 'POST':
        form = StrengthTrainingForm(request.POST)
        
        if form.is_valid():
            best_rep_avg_speed = form.cleaned_data['best_rep_avg_speed']
            best_rep_max_speed = form.cleaned_data['best_rep_max_speed']
            best_rep_rom = form.cleaned_data['best_rep_rom']
            best_rep_power = form.cleaned_data['best_rep_power']
            best_rep = {
                'best_rep_avg_speed': best_rep_avg_speed,
                'best_rep_max_speed': best_rep_max_speed,
                'best_rep_rom': best_rep_rom,
                'best_rep_power': best_rep_power
            }
            form.instance.best_rep = best_rep
            form.save()
            messages.success(request, 'Gravado com sucesso')
            return redirect('strength_registation')  
    else:
        form = StrengthTrainingForm()

    context = {'form': form}
    return render(request, 'training/register_strength.html', context)

def create_jumps_training(request):
    if request.method == 'POST':
        form = JumpsTrainingForm(request.POST)
        if form.is_valid():

            form.save()
            messages.success(request, 'Gravado com sucesso')
            return redirect('jumps_registration')  
    else:
        form = JumpsTrainingForm()

    context = {'form': form}
    return render(request, 'training/register_jumps.html', context)
