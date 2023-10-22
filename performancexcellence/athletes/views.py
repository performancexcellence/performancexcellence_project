from django.shortcuts import render
from athletes.models import *
from competitions.models import *
from training_programme.models import *
from django.core.paginator import Paginator
from athletes.athletics_functions import *
from wellness.models import WellnessDaily
from django.contrib.auth.decorators import login_required
from physiology.models import Evaluation
from physiotherapy.models import Injury



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

@login_required(login_url='login')
def show_athlete_goals(request, pk):
    event = request.GET.get('event')
    athlete = Athlete.objects.get(id=pk)
    profile = Profile.objects.get(id=athlete.profile.id)
    goals = Goals.objects.filter(athlete=athlete)
    seasons_periods = Goals.objects.values_list('season', 'season_period').distinct()
    context = {
        'athlete': athlete,
        'profile': profile,
        "goals": goals,
        "seasons_periods": seasons_periods,
        'event': event
    }
    return render(request, 'athletes/athlete_show_goals.html', context)

@login_required(login_url='login')
def show_control_evaluation(request, pk):
    event = request.GET.get('event')
    athlete = Athlete.objects.get(id=pk)
    profile = Profile.objects.get(id=athlete.profile.id)
    physiology_evaluations = Evaluation.objects.filter(athlete=athlete)
    for evaluation in physiology_evaluations:
        evaluation.adductor_deficit = calculate_deficit(
            evaluation.adductor_left_peak_force, 
            evaluation.adductor_right_peak_force
        )
        evaluation.abductor_deficit = calculate_deficit(
            evaluation.abductor_left_peak_force, 
            evaluation.abductor_right_peak_force
        )
        evaluation.hams_deficit = calculate_deficit(
            evaluation.hams_left, 
            evaluation.hams_right
        )
        evaluation.quad_deficit = calculate_deficit(
            evaluation.quad_left, 
            evaluation.quad_right
        )
        evaluation.calf_deficit = calculate_deficit(
            evaluation.calf_left, 
            evaluation.calf_right
        )
    context = {
        'athlete': athlete,
        'profile': profile,
        "physiology_evaluations": physiology_evaluations,
    }
    return render(request, 'athletes/athlete_show_control_evaluation.html', context)

def calculate_deficit(left_force, right_force):
    return (left_force - right_force) / left_force * 100 if left_force else 0


@login_required(login_url='login')
def show_control_injuries(request, pk):
    event = request.GET.get('event')
    athlete = Athlete.objects.get(id=pk)
    profile = Profile.objects.get(id=athlete.profile.id)
    injuries = Injury.objects.filter(athlete=athlete)

    context = {
        'athlete': athlete,
        'profile': profile,
        "injuries": injuries,
    }
    return render(request, 'athletes/athlete_show_injuries.html', context)
