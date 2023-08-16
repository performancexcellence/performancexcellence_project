from django.shortcuts import render
from athletes.models import *
from django.core.paginator import Paginator
# Create your views here.

def show_athlete(request, pk):
    athlete = Athlete.objects.get(id=pk)
    profile = Profile.objects.get(id=athlete.profile.id)
    context = {'athlete': athlete,
               'profile': profile}
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