from django.shortcuts import render, redirect
from .forms import TrainingProgrammeForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
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
