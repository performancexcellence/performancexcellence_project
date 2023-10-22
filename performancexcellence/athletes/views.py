from django.shortcuts import render
from athletes.models import *
from competitions.models import *
from django.core.paginator import Paginator
from athletes.athletics_functions import *
from wellness.models import WellnessDaily
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def show_athlete(request, pk):
    athlete = Athlete.objects.get(id=pk)
    profile = Profile.objects.get(id=athlete.profile.id)
    curriculum = AthleticsCurriculum.objects.filter(athlete=athlete).order_by("competition_date")
    context = {
        'athlete': athlete,
        'profile': profile,
        "curriculum": curriculum
    }

    return render(request, 'athletes/athlete_show.html', context)

@login_required(login_url='login')
def athletes_list(request):
    athletes = Athlete.objects.all()
    items_per_page = 1
    paginator = Paginator(athletes, items_per_page)
    page_number = request.GET.get('page')
    page_items = paginator.get_page(page_number)
    context = {'athletes': athletes,
               'page_items': page_items}
    return render(request, 'athletes/athletes_list.html', context)

@login_required(login_url='login')
def show_athlete_wellness(request, pk):
    athlete = Athlete.objects.get(id=pk)
    wellness_registers = WellnessDaily.objects.filter(athlete=athlete.id)
    wellness_graph = weekly_wellness(wellness_registers)
    profile = Profile.objects.get(id=athlete.profile.id)
    wellness_json = str(wellness_graph).replace("'", '"')
    context = {
        'athlete': athlete,
        'profile': profile,
        "wellness_data": wellness_json,
        "tab": 'wellness'
    }

    return render(request, 'athletes/athlete_show_wellness.html', context)

@login_required(login_url='login')
def show_athlete_personal_records(request, pk):
    athlete = Athlete.objects.get(id=pk)
    profile = Profile.objects.get(id=athlete.profile.id)
    personal_records = personal_bests(pk)
    context = {
        'athlete': athlete,
        'profile': profile,
        "personal_records": personal_records,
    }

    return render(request, 'athletes/athlete_show_personal_records.html', context)

@login_required(login_url='login')
def show_athlete_progression(request, pk):
    event = request.GET.get('event')
    athlete = Athlete.objects.get(id=pk)
    profile = Profile.objects.get(id=athlete.profile.id)
    competitions_events = get_competitions_by_athlete(athlete.id)
    if event is None:
        event = competitions_events[0].event_name
    progression = progression_by_year(pk, event)
    progression = progression[event]
    progression_json = str(progression).replace("'", '"')
    context = {
        'competitions_events': competitions_events,
        'athlete': athlete,
        'profile': profile,
        "progression_data": progression_json,
        'event': event
    }
    return render(request, 'athletes/athlete_show_progression.html', context)