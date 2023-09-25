from django import forms
from .models import TrainingProgramme

class TrainingProgrammeForm(forms.ModelForm):
    class Meta:
        model = TrainingProgramme
        fields = ['athlete', 'date', 'warmup', 'main', 'cool_down', 'obs', 'local', 'hours', 'intensity']

        widgets = {
            'athlete': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'hours': forms.TextInput(attrs={'class': 'form-control'}),
            'intensity': forms.NumberInput(attrs={'class': 'form-control', 'step': '1'}),
            'local': forms.TextInput(attrs={'class': 'form-control'}),
            'warmup': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Separar os conteudos do treino por ;'}),
            'main': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Separar os conteudos do treino por ;'}),
            'cool_down': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Separar os conteudos do treino por ;'}),
            'obs': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Separar os conteudos do treino por ;'}),
        }
        labels = {
            'athlete': 'Atleta',
            'date': 'Data',
            'hours': 'Horas do Treino',
            'intensity': 'Intensidade Subjetiva do Treino'
        }
