from django.shortcuts import render, redirect
from .forms import AntropometricDataForm
from .models import AntropometricData

# Create your views here.
def antropometric_data_create(request):
    if request.method == 'POST':
        form = AntropometricDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AntropometricDataForm()

    return render(request, 'nutrition/create_evaluation.html', {'form': form})