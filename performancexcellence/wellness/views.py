from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import WellnessDaily, LoadControl
from users.models import Profile 
from athletes.models import Athlete
from django.contrib.auth.decorators import login_required
import locale

@login_required(login_url='login')
def daily_registration(request, pk):
    current_user = request.user
    profile = Profile.objects.get(user=current_user.id)
    athlete = Athlete.objects.get(profile=profile)
    if request.method == 'POST':
        weight = request.POST.get('weight')
        weight = weight.replace(",", ".")
        fatigue = request.POST.get('fatigue')
        sleep = request.POST.get('sleep')
        soreness = request.POST.get('soreness')
        stress = request.POST.get('stress')
        mood = request.POST.get('mood')
        hydration = request.POST.get('hydration')
        nutrition = request.POST.get('nutrition')
        hours_sleep = request.POST.get('hours_sleep')
        hours_sleep = hours_sleep.replace(",", ".")

        # Create a new WellnessDaily instance and assign values
        WellnessDaily.objects.create(
            athlete_id=athlete.id,
            weight=weight,
            fatigue=fatigue,
            sleep_quality=sleep,
            muscle_soreness=soreness,
            stress_level=stress,
            mood=mood,
            hydration=hydration,
            nutrition=nutrition,
            hours_sleep = hours_sleep,
            registration_date=datetime.now().date()  # Corrected 'registation_date' to 'registration_date'
        )
        
        messages.success(request, 'Questionário enviado com sucesso!')
        return redirect('home')  # Replace 'success_url' with your actual URL name
    
    context = {
        'profile': profile
    }
    return render(request, 'wellness/daily_registration.html', context)

@login_required(login_url='login')
def load_registration(request, pk):
    current_user = request.user
    profile = Profile.objects.get(user=current_user.id)
    athlete = Athlete.objects.get(profile=profile)
    if request.method == 'POST':
        intensity = request.POST.get('intensity')
        intensity = intensity.replace(",", ".")
        training_hours = request.POST.get('training_hours')
        training_hours = training_hours.replace(",", ".")
        obs = request.POST.get('obs')

        LoadControl.objects.create(
            athlete_id=athlete.id,
            intensity=intensity,
            training_hours=training_hours,
            obs=obs,
            load=float(intensity)*float(training_hours),
            registration_date=datetime.now().date()
        )

        messages.success(request, 'Questionário enviado com sucesso!')
        return redirect('home')  # Replace 'success_url' with your actual URL name

    context = {
        'profile': profile
    }
    return render(request, 'wellness/load_registration.html', context)
