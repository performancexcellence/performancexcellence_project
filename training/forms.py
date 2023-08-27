from django import forms
from .models import StrengthTraining, JumpsTraining


class StrengthTrainingForm(forms.ModelForm):
    best_rep_avg_speed = forms.FloatField(
        label="Velocidade média",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    best_rep_max_speed = forms.FloatField(
        label="Velocidade Máxima",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    best_rep_rom = forms.FloatField(
        label="ROM em cm",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    best_rep_power = forms.FloatField(
        label="Potência",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = StrengthTraining
        fields = '__all__' 
        widgets = {
            'date': forms.DateTimeInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                    'data-inputmask-inputformat': 'yyyy-mm-dd',
                    'inputmode': 'numeric',
                    'data-inputmask-alias': 'datetime',
                    'placeholder': 'yyyy-mm-dd'
                }
            ),
            'exercise': forms.Select(attrs={'class': 'custom-select'}),
            'athlete': forms.Select(attrs={'class': 'custom-select'}),
            'exercise_notes': forms.Select(attrs={'class': 'custom-select'}),
            'set': forms.NumberInput(attrs={'class': 'form-control'}),  # Change to NumberInput
            'nr_repetitions': forms.NumberInput(attrs={'class': 'form-control'}),  # Change to NumberInput
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),  # Change to NumberInput
            'median_speed': forms.NumberInput(attrs={'class': 'form-control'}),  # Change to NumberInput
            'median_rom': forms.NumberInput(attrs={'class': 'form-control'}),  # Change to NumberInput
            'left_in_tank': forms.NumberInput(attrs={'class': 'form-control'}),  # Change to NumberInput
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.date:
            self.initial['date'] = self.instance.date.strftime('%Y-%m-%d')

class JumpsTrainingForm(forms.ModelForm):
    poles_info_pega = forms.FloatField(
        label="Altura da Pega",
        widget=forms.NumberInput(attrs={'class': 'form-control', "value": "0"})
    )
    poles_info_height = forms.FloatField(
        label="Altura da Vara",
        widget=forms.NumberInput(attrs={'class': 'form-control', "value": "0"})
    )
    poles_info_flex = forms.FloatField(
        label="Flexibilidade Vara",
        widget=forms.NumberInput(attrs={'class': 'form-control', "value": "0"})
    )
    class Meta:
        model = JumpsTraining
        fields = '__all__'
        widgets = {
            'date': forms.DateTimeInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                    'data-inputmask-inputformat': 'yyyy-mm-dd',
                    'inputmode': 'numeric',
                    'data-inputmask-alias': 'datetime',
                    'placeholder': 'yyyy-mm-dd'
                }
            ),
            'athlete': forms.Select(attrs={'class': 'custom-select'}),
            'jumps_training_type': forms.Select(attrs={'class': 'custom-select'}),  # Add class attribute
            'technical_training': forms.Select(attrs={'class': 'custom-select'}), 
            'multijumps_training': forms.Select(attrs={'class': 'custom-select'}),  # Add class attribute
            'nr_steps': forms.NumberInput(attrs={'class': 'form-control'}),  # Add class attribute
            'result': forms.NumberInput(attrs={'class': 'form-control'}),
            'high_jump_technique': forms.Select(attrs={'class': 'custom-select'})
        }