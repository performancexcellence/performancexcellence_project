from django.shortcuts import render
from .forms import EvaluationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def strength_test_create(request):
    if request.method == 'POST':
        form = EvaluationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)

            # Calculate the adductor deficit
            if instance.adductor_left_peak_force and instance.adductor_right_peak_force:
                adductor_deficit = (instance.adductor_left_peak_force - instance.adductor_right_peak_force) / instance.adductor_right_peak_force
                instance.adductor_deficit = f'{adductor_deficit:.2%}'

            # Calculate the abductor deficit
            if instance.abductor_left_peak_force and instance.abductor_right_peak_force:
                abductor_deficit = (instance.abductor_left_peak_force - instance.abductor_right_peak_force) / instance.abductor_right_peak_force
                instance.abductor_deficit = f'{abductor_deficit:.2%}'

            # Calculate the calf deficit
            if instance.calf_left and instance.calf_right:
                calf_deficit = (instance.calf_left - instance.calf_right) / instance.calf_left
                instance.calf_deficit = f'{calf_deficit:.2%}'

            # Calculate the quad deficit
            if instance.quad_left and instance.quad_right:
                quad_deficit = (instance.quad_left - instance.quad_right) / instance.quad_left
                instance.quad_deficit = f'{quad_deficit:.2%}'

            # Calculate the hams deficit
            if instance.hams_left and instance.hams_right:
                hams_deficit = (instance.hams_left - instance.hams_right) / instance.hams_left
                instance.hams_deficit = f'{hams_deficit:.2%}'

            instance.save()
            return render(request, 'users/home.html')
    else:
        form = EvaluationForm()

    return render(request, 'physiology/initial_evaluation.html', {'form': form})
