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
    time_reacao = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    time_10m = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    time_20m = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    time_30m = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    time_40m = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Speed
        fields = '__all__'
        widgets = {
            'athlete': forms.Select(attrs={'class': 'form-control'}),
            'evaluation_choice': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'yyyy-MM-dd'}),
            'partial_reacao': forms.HiddenInput(),
            'partial_10m': forms.HiddenInput(),
            'partial_20m': forms.HiddenInput(),
            'partial_30m': forms.HiddenInput(),
            'partial_40m': forms.HiddenInput(),
        }
        labels = {
            'athlete': 'Atleta',
            'evaluation_choice': 'Tipo de Avaliação',
            'date': 'Data (yyyy-MM-dd)',
        }
    def clean(self):
        cleaned_data = super().clean()
        
        # Crie arrays de tempos e distâncias com os campos individuais
        cleaned_data['time'] = [
            cleaned_data.get('time_reacao', None),
            cleaned_data.get('time_10m', None),
            cleaned_data.get('time_20m', None),
            cleaned_data.get('time_30m', None),
            cleaned_data.get('time_40m', None)
        ]
        # Assumindo que as distâncias são constantes, você pode definir diretamente
        cleaned_data['distance'] = [0, 10, 20, 30, 40]

        return cleaned_data
