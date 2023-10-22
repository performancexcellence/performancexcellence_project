from django import forms
from .models import Evaluation

class EvaluationForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = [
            'athlete',
            'date',
            'cmj',
            'average_rsi',
            'imtp_peak_force',
            'adductor_left_peak_force',
            'adductor_right_peak_force',
            'abductor_left_peak_force',
            'abductor_right_peak_force',
            'hams_right',
            'hams_left',
            'quad_left',
            'quad_right',
            'calf_left',
            'calf_right',
        ]
        widgets = {
            'athlete': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'yyyy-MM-dd'}),
            'cmj': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'average_rsi': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'imtp_peak_force': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'adductor_left_peak_force': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'adductor_right_peak_force': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'abductor_left_peak_force': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'abductor_right_peak_force': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'hams_right': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'hams_left': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'quad_left': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'quad_right': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'calf_left': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'calf_right': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }
        labels = {
            'athlete': 'Atleta',
            'date': 'Data (yyyy-MM-dd)',
            'cmj': 'Counter Movement Jump (CMJ)',
            'average_rsi': 'Average RSI',
            'imtp_peak_force': 'IMTP Peak Force',
            'adductor_left_peak_force': 'Adductor Left Peak Force',
            'adductor_right_peak_force': 'Adductor Right Peak Force',
            'abductor_left_peak_force': 'Abductor Left Peak Force',
            'abductor_right_peak_force': 'Abductor Right Peak Force',
            'hams_right': 'Hamstrings Right',
            'hams_left': 'Hamstrings Left',
            'quad_left': 'Quad Left',
            'quad_right': 'Quad Right',
            'calf_left': 'Calf Left',
            'calf_right': 'Calf Right',
        }