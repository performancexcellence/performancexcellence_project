from django.shortcuts import render, redirect
from .models import AntropometricData
from django.contrib.auth.decorators import login_required

# Create your views here.
#@login_required(login_url='login')
#def antropometric_data_create(request):
#    if request.method == 'POST':
#        form = AntropometricDataForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('home')
#    else:
#        form = AntropometricDataForm()
#
#    return render(request, 'nutrition/create_evaluation.html', {'form': form})