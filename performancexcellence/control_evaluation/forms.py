from django import forms
from .models import Strength, Speed

class StrengthForm(forms.ModelForm):
    mpv1 = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    mpv2 = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    mpv3 = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    peak_velocity1 = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    peak_velocity2 = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    peak_velocity3 = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    rom1 = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    rom2 = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    rom3 = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    mean_power1 = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    mean_power2 = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    mean_power3 = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Strength
        fields = '__all__'
        widgets = {
            'athlete': forms.Select(attrs={'class': 'form-control'}),
            'goal': forms.Select(attrs={'class': 'form-control'}),
            'exercise': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'yyyy-MM-dd'}),
            'sets': forms.NumberInput(attrs={'class': 'form-control'}),
            'mpv': forms.HiddenInput(),  # Adicione campos ocultos para os arrays
            'peak_velocity': forms.HiddenInput(),
            'rom': forms.HiddenInput(),
            'mean_power': forms.HiddenInput(),
        }
        labels = {
            'athlete': 'Atleta',
            'goal': 'Objetivo',
            'exercise': 'Exercício',
            'date': 'Data (yyyy-MM-dd)',
            'sets': 'Série',
        }

class SpeedForm(forms.ModelForm):
    class Meta:
        model = Speed
        fields = ['athlete', 'evaluation_choice', 'date', 'distance', 'time']