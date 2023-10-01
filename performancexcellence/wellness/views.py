from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import WellnessDaily
from users.models import Profile 
from athletes.models import Athlete
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def daily_registration(request, pk):
    current_user = request.user
    profile = Profile.objects.get(user=current_user.id)
    athlete = Athlete.objects.get(profile=profile)
    if request.method == 'POST':
        weight = request.POST.get('weight')
        fatigue = request.POST.get('fatigue')
        sleep = request.POST.get('sleep')
        soreness = request.POST.get('soreness')
        stress = request.POST.get('stress')
        mood = request.POST.get('mood')
        hidration = request.POST.get('hidration')
        nutrition = request.POST.get('nutrition')

        # Create a new WellnessDaily instance and assign values
        WellnessDaily.objects.create(
            athlete_id=athlete.id,
            weight=weight,
            fatigue=fatigue,
            sleep_quality=sleep,
            muscle_soreness=soreness,
            stress_level=stress,
            mood=mood,
            hidration=hidration,
            nutrition=nutrition,
            registration_date=datetime.now().date()  # Corrected 'registation_date' to 'registration_date'
        )
        
        messages.success(request, 'Questionário enviado com sucesso!')
        return redirect('home')  # Replace 'success_url' with your actual URL name
    
    context = {
        'profile': profile
    }
    return render(request, 'wellness/daily_registration.html', context)

def show_registration(request, pk):
    registration = WellnessDaily.objects.get(id=pk)
    context = {"registration": registration}
    return render(request, 'wellness/show_registration.html', context)

def wellness_registrations(request):
    athlete_name = request.GET.get('athlete')
    athlete_list = Athlete.objects.all()
    if athlete_name is None:
        register_list = WellnessDaily.objects.all()
        for register in register_list:
            register.average = (register.mood + register.stress_level + register.muscle_soreness + register.sleep_quality + register.fatigue) / 5
    else: 
        profile = Profile.objects.get(name=athlete_name)
        athlete = Athlete.objects.get(profile=profile)
        register_list = WellnessDaily.objects.filter(athlete=athlete.id)
        for register in register_list:
            register.average = (register.mood + register.stress_level + register.muscle_soreness + register.sleep_quality + register.fatigue) / 5


    context = {
        'register_list': register_list,
        "athlete_name": athlete_name,
        "athlete_list": athlete_list,
    }
    return render(request, 'wellness/list_registration.html', context)