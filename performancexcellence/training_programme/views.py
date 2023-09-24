from django.shortcuts import render, redirect
from .forms import TrainingProgrammeForm
from .models import TrainingProgramme

# Create your views here.
def training_programme_create(request):
    if request.method == 'POST':
        print("--------------POST-------")
        form = TrainingProgrammeForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'users/home.html')
    else:
        form = TrainingProgrammeForm()

    return render(request, 'training_programme/training_programme_create.html', {'form': form})
