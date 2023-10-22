from django.shortcuts import render
from .forms import EvaluationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required(login_url='login')
def strength_test_create(request):
    if request.method == 'POST':
        form = EvaluationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Formulário enviado com sucesso!')
            return render(request, 'users/home.html')
    else:
        form = EvaluationForm()

    return render(request, 'physiology/initial_evaluation.html', {'form': form})
