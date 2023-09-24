from django.shortcuts import render
from athletes.models import *
from competitions.models import *
from django.core.paginator import Paginator
from athletes.athletics_functions import *
from wellness.models import WellnessDaily
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def show_athlete(request, pk):
    page = request.GET.get('page')
    event = request.GET.get('event')
    athlete = Athlete.objects.get(id=pk)
    wellness_graph = wellness(athlete.id)
    profile = Profile.objects.get(id=athlete.profile.id)
    personal_records = personal_bests(pk)
    if page is None:
        page = "personal_records"
        if len(personal_records) <1:
            event = None
            progression = None
        else:
            event = personal_records[0]["event_name"]
            progression = progression_by_year(pk, event)
            progression = progression[event]
    else:
        progression = progression_by_year(pk, event)
        progression = progression[event]

    # Converte o dicionário 'progression' em uma string JSON
    progression_json = str(progression).replace("'", '"')
    wellness_json = str(wellness_graph).replace("'", '"')
    context = {
        'athlete': athlete,
        'profile': profile,
        "personal_records": personal_records,
        "progression_data": progression_json,  # Passa a string JSON em vez do dicionário
        "page": page,
        'event': event, 
        "wellness_data": wellness_json
    }

    return render(request, 'athletes/athlete_show.html', context)

def athletes_list(request):
    athletes = Athlete.objects.all()
    items_per_page = 1
    paginator = Paginator(athletes, items_per_page)
    page_number = request.GET.get('page')
    page_items = paginator.get_page(page_number)
    context = {'athletes': athletes,
               'page_items': page_items}
    return render(request, 'athletes/athletes_list.html', context)

