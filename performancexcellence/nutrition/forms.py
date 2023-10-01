from django import forms
from .models import AntropometricData

class AntropometricDataForm(forms.ModelForm):
    class Meta:
        model = AntropometricData
        fields = [
            'date',
            'height',
            'weight',
            'body_fat',
            'lean_mass',
            'left_arm',
            'right_arm',
            'trunk',
            'left_leg',
            'right_leg',
            'head',
            'metabolism',
            'obs'
        ]
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'yyyy-MM-dd'}),
            'height': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'body_fat': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'lean_mass': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'left_arm': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'right_arm': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'trunk': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'left_leg': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'right_leg': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'head': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'metabolism': forms.TextInput(attrs={'class': 'form-control'}),
            'obs': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'date': 'Data (yyyy-MM-dd)',
            'height': 'Altura (m)',
            'weight': 'Peso (kg)',
            'body_fat': 'Gordura Corporal (%)',
            'lean_mass': 'Massa Magra (kg)',
            'left_arm': 'Braço Esquerdo (cm)',
            'right_arm': 'Braço Direito (cm)',
            'trunk': 'Tronco (cm)',
            'left_leg': 'Perna Esquerda (cm)',
            'right_leg': 'Perna Direita (cm)',
            'head': 'Cabeça (cm)',
            'metabolism': 'Metabolismo',
            'obs': 'Observações'
        }